/* Exact scoped BM tools. Rational arithmetic, no eval, no external service. */
(function(root){
'use strict';
const core=typeof module!=='undefined'&&module.exports?require('./bm-core.js'):root.BMCalc;
const {Q,csv}=core,zero=new Q(0n),one=new Q(1n),two=new Q(2n);
const mul=(a,b)=>new Q(a.n*b.n,a.d*b.d),max=(a,b)=>a.cmp(b)>=0?a:b;
function number(x){if(typeof x==='number'&&!Number.isSafeInteger(x))throw Error('Use rational strings for non-integers; JSON numbers must be safe integers.');if(typeof x!=='number'&&typeof x!=='string')throw Error('Use integers or rational strings.');return Q.parse(x);}
function integer(x,min,maxValue,name){if(!['number','string'].includes(typeof x)||String(x).trim()==='')throw Error(`${name} must be an integer.`);const n=Number(x);if(!Number.isSafeInteger(n)||n<min||n>maxValue)throw Error(`${name} must be an integer from ${min} to ${maxValue}.`);return n;}
function matrix(a,n){if(!Array.isArray(a)||!a.length)throw Error('Supply a nonempty square matrix.');n=n??a.length;if(n>8||a.length!==n||a.some(r=>!Array.isArray(r)||r.length!==n))throw Error('Matrices must be square, share a dimension, and have at most eight rows.');return a.map(r=>r.map(number));}
function identity(n){return Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>i===j?one:zero));}
function trace(a){return a.reduce((v,r,i)=>v.add(r[i]),zero);}
function traceProduct(a,b){let v=zero;for(let i=0;i<a.length;i++)for(let j=0;j<a.length;j++)v=v.add(mul(a[i][j],b[j][i]));return v;}
function psd(a){
 const n=a.length,s=a.map(r=>r.slice()),pivots=[];
 for(let i=0;i<n;i++)for(let j=0;j<n;j++)if(a[i][j].cmp(a[j][i])!==0)throw Error('A certificate matrix is not real symmetric.');
 for(let k=0;k<n;k++){
  const d=s[k][k];if(d.cmp(zero)<0)throw Error('A required matrix is not positive semidefinite (negative exact pivot).');
  if(d.cmp(zero)===0){for(let j=k+1;j<n;j++)if(s[k][j].cmp(zero)!==0)throw Error('A zero PSD pivot has a nonzero residual row.');}
  else for(let i=k+1;i<n;i++)for(let j=i;j<n;j++){s[i][j]=s[i][j].sub(mul(s[i][k],s[k][j]).div(d));s[j][i]=s[i][j];}
  pivots.push(d.toString());
 }return pivots;
}
function verifyQuantum(c){
 if(!c||typeof c!=='object'||!Array.isArray(c.states)||!c.states.length||c.states.length>8)throw Error('Supply one certificate with one to eight signal states.');
 const states=c.states.map(a=>matrix(a)),n=states[0].length,r=states.length;
 if(states.some(a=>a.length!==n))throw Error('All signal states must share a dimension.');
 const statePivots=states.map(psd);if(states.some(a=>trace(a).cmp(one)!==0))throw Error('Every signal state must have trace one.');
 if(!Array.isArray(c.povm)||c.povm.length!==r)throw Error('Supply one POVM matrix per signal.');
 const povm=c.povm.map(a=>matrix(a,n)),povmPivots=povm.map(psd),id=identity(n);
 for(let i=0;i<n;i++)for(let j=0;j<n;j++)if(povm.reduce((v,a)=>v.add(a[i][j]),zero).cmp(id[i][j])!==0)throw Error('The POVM matrices do not sum to the identity.');
 const q=number(c.success_lower);if(q.cmp(zero)<0||q.cmp(one)>0)throw Error('The success lower bound must lie in [0,1].');
 const successes=states.map((a,i)=>traceProduct(a,povm[i]));if(successes.some(v=>v.cmp(q)<0))throw Error('The POVM does not meet the claimed success lower bound.');
 if(!Array.isArray(c.dual_weights)||c.dual_weights.length!==r)throw Error('Supply one dual weight per signal.');
 const weights=c.dual_weights.map(number);if(weights.some(w=>w.cmp(zero)<0)||weights.reduce((a,b)=>a.add(b),zero).cmp(one)!==0)throw Error('Dual weights must be nonnegative and sum to one.');
 const y=matrix(c.dual_matrix,n),slacks=states.map((a,i)=>psd(y.map((row,j)=>row.map((v,k)=>v.sub(mul(weights[i],a[j][k]))))));
 const upper=trace(y);if(upper.cmp(q)<0)throw Error('Primal and dual bounds contradict each other.');
 const lowError=max(zero,mul(two,one.sub(upper))),highError=mul(two,one.sub(q)),exact=q.cmp(upper)===0;
 if(exact&&c.expected_error!==undefined&&number(c.expected_error).cmp(highError)!==0)throw Error('The declared expected error disagrees with the verified optimum.');
 return {name:String(c.name||'Supplied certificate'),dimension:n,signals:r,exact,successInterval:[q.toString(),upper.toString()],errorInterval:[lowError.toString(),highError.toString()],successes:successes.map(String),pivots:{states:statePivots,povm:povmPivots,dualSlacks:slacks},method:'BM23-Q3 · exact rational primal/dual certificate',scope:'Classical labels encoded as the supplied quantum signal states; diagonal logical task algebra. This verifies witnesses, not a general quantum SDP.'};
}
function parseCausal(text){
 if(typeof text!=='string'||text.length>20000)throw Error('Use a state table of at most 20,000 characters.');
 const rows=csv(text),header=rows.shift();if(header?.join(',').toLowerCase()!=='state,task,next')throw Error('Use the header: state,task,next');
 if(!rows.length||rows.length>6)throw Error('Exact synthesis here supports one to six native states.');
 const seen=new Set(),states=rows.map((row,i)=>{if(row.length!==3)throw Error(`Row ${i+1}: expected state, task, next.`);const[id,v,next]=row;if(!id||id.length>80||seen.has(id))throw Error('Use distinct nonempty state labels of at most 80 characters.');seen.add(id);return{id,value:Q.parse(v),next};});
 const indices=new Map(states.map((s,i)=>[s.id,i]));for(const s of states){if(!indices.has(s.next))throw Error(`State “${s.id}” must name a supplied next state; this synthesis contract requires total dynamics.`);s.nextIndex=indices.get(s.next);}return states;
}
function synthesizeCausal(input){
 const states=parseCausal(input.text),n=states.length,budget=integer(input.budget,1,3,'State budget'),mode=input.mode;
 if(!['history','closed'].includes(mode))throw Error('Choose causal history or a closed current-state encoder.');
 const full=(1<<n)-1,cells=[];
 for(let mask=1;mask<=full;mask++){
  let min=null,maxValue=null,image=0;
  for(let i=0;i<n;i++)if(mask&(1<<i)){const v=states[i].value;min=min===null||v.cmp(min)<0?v:min;maxValue=maxValue===null||v.cmp(maxValue)>0?v:maxValue;image|=1<<states[i].nextIndex;}
  cells.push({mask,image,radius:maxValue.sub(min).div(two),decoder:min.add(maxValue).div(two)});
 }
 let best=[cells[full-1]],bestError=best[0].radius,enumerated=0;
 const frontier=[{budget:1,error:bestError.toString(),states:1}];
 for(let k=2;k<=budget;k++){
  if(bestError.cmp(zero)>0){
   const pool=cells.filter(c=>c.radius.cmp(bestError)<0).sort((a,b)=>a.radius.cmp(b.radius)||a.mask-b.mask),suffix=Array(pool.length+1).fill(0);
   for(let i=pool.length-1;i>=0;i--)suffix[i]=suffix[i+1]|pool[i].mask;
   function search(start,chosen,covered,cost){
    if(chosen.length===k){
     enumerated++;if(covered!==full)return;
     if(chosen.some(c=>!chosen.some(target=>(c.image&~target.mask)===0)))return;
     if(cost.cmp(bestError)<0){best=chosen.slice();bestError=cost;}return;
    }
    if((covered|suffix[start])!==full||pool.length-start<k-chosen.length)return;
    for(let i=start;i<pool.length;i++){
     const c=pool[i];if(c.radius.cmp(bestError)>=0)break;
     if(mode==='closed'&&(covered&c.mask))continue;
     search(i+1,[...chosen,c],covered|c.mask,max(cost,c.radius));
    }
   }
   search(0,[],0,zero);
  }
  frontier.push({budget:k,error:bestError.toString(),states:best.length});
 }
 const witness=best.map((c,i)=>({code:'q'+i,states:states.filter((_,j)=>c.mask&(1<<j)).map(s=>s.id),output:c.decoder.toString(),error:c.radius.toString(),next:'q'+best.findIndex(target=>(c.image&~target.mask)===0)}));
 const initialization=states.map((s,i)=>({state:s.id,code:'q'+best.findIndex(c=>c.mask&(1<<i))}));
 return {mode,budget,nativeStates:n,error:bestError.toString(),predictorStates:best.length,frontier,witness,initialization,enumeratedFamilies:enumerated,method:'BM20-C1–C3 · exhaustive exact invariant-cover synthesis',scope:'One total deterministic update, all supplied states allowed initially, one rational real-valued task, absolute error, unrestricted real outputs. History cells may overlap; closed-encoder cells form a partition.'};
}
function decayBudget(input){
 const M=number(input.M),L=number(input.L),epsilon=number(input.epsilon),p=integer(input.dimension,1,8,'Task dimension'),s=integer(input.actions,1,8,'Action count');
 if(M.cmp(zero)<0||L.cmp(zero)<0||L.cmp(one)>=0||epsilon.cmp(zero)<=0)throw Error('Require M ≥ 0, 0 ≤ L < 1, and ε > 0.');
 const half=epsilon.div(two);let K=0,tail=M;
 while(tail.cmp(half)>0){if(K>=64)throw Error('This browser tool limits forecast depth to 64. The theorem still applies; use the downloadable Python construction for a larger instance.');tail=mul(tail,L);K++;}
 const h=epsilon.div(new Q(BigInt(2*p))),ratio=M.div(h),J=(ratio.n+ratio.d-1n)/ratio.d+1n,Qlabels=(2n*J+1n)**BigInt(p);
 let nodes=0n,total=1n,canExpand=true;const terms=[];
 for(let r=1;r<=K;r++){nodes=1n+BigInt(s)*nodes;terms.push(nodes.toString());if(nodes*BigInt(Qlabels.toString().length)>2000n)canExpand=false;}
 if(canExpand)for(const exponent of terms)total+=Qlabels**BigInt(exponent);
 return{K,h:h.toString(),J:J.toString(),labels:Qlabels.toString(),tailBound:tail.toString(),guaranteedError:half.toString(),oracleAccuracy:epsilon.div(new Q(BigInt(4*p))).toString(),stateBound:canExpand?total.toString():null,stateBoundFormula:'1'+terms.map(exponent=>` + ${Qlabels}^${exponent}`).join(''),method:'BM23-I1 · uniform task-decay bound',scope:'Assumes the independently proved bound ||τ(f_w(x))||₂ ≤ M L^|w| and computable finite responses. This computes a sufficient state bound; it does not prove native decay, minimize states, or assert exact current-state closure.'};
}
const api={psd,matrix,verifyQuantum,parseCausal,synthesizeCausal,decayBudget};
if(typeof module!=='undefined'&&module.exports)module.exports=api;root.BMVerified=api;
})(typeof window!=='undefined'?window:globalThis);
