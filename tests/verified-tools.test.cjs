'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const {Q,uniformGap}=require('../assets/bm-core.js');
const {calculate,splitStatements}=require('../assets/equation-worker.js');
const V=require('../assets/bm-verified.js');
let checks=0;function eq(a,b){assert.deepEqual(a,b);checks++;}function ok(a){assert.ok(a);checks++;}function rejects(fn){assert.throws(fn);checks++;}
eq(splitStatements('x+y=\n10\nx-y=2\n(x+\n y)^2'),['x+y= 10','x-y=2','(x+  y)^2']);
eq(calculate({text:'x+y=10\nx-y=2\nx*y'}).rows[0].answer,'24');
eq(calculate({text:'x=2\n(x+1)^2'}).rows[0].answer,'9');
eq(calculate({text:'diff(\n x^3,\n x\n)'}).rows[0].answer,'3*x^2');
eq(calculate({text:'2\n-3'}).rows.map(r=>r.answer),['2','-3']);
eq(calculate({text:'determinant(matrix([1,2],\n[3,4]))'}).rows[0].answer,'-2');
eq(calculate({text:'expand(diff(c^3-3*b*c*d+3*a*d^2,a)*b+diff(c^3-3*b*c*d+3*a*d^2,b)*c+diff(c^3-3*b*c*d+3*a*d^2,c)*d)'}).rows[0].answer,'0');
const certFile=path.resolve(__dirname,'../downloads/bm-2026-10-23/BM_Quantum_Certificates_2026-10-23.json');
const certs=JSON.parse(fs.readFileSync(certFile,'utf8')).certificates;
for(const cert of certs){const r=V.verifyQuantum(cert);ok(r.exact);eq(r.errorInterval,[String(cert.expected_error),String(cert.expected_error)]);}
function corrupt(change){const c=JSON.parse(JSON.stringify(certs[0]));change(c);rejects(()=>V.verifyQuantum(c));}
corrupt(c=>c.success_lower='1');corrupt(c=>c.states[0][0][0]='2');corrupt(c=>c.states[0]=[[1,1],[1,0]]);corrupt(c=>c.states[1][0][1]='0');corrupt(c=>c.povm[0][0][0]='4/5');corrupt(c=>c.dual_weights=['1','1']);corrupt(c=>c.dual_matrix=[[0,0],[0,0]]);corrupt(c=>c.success_lower=.9);corrupt(c=>c.expected_error='0');corrupt(c=>c.success_lower=true);
// Independent PSD oracle: all principal minors, not the Schur algorithm.
function det(a){if(!a.length)return 1;if(a.length===1)return a[0][0];return a[0].reduce((sum,v,j)=>sum+(j%2?-1:1)*v*det(a.slice(1).map(r=>r.filter((_,k)=>k!==j))),0);}
function principalPSD(a){for(let mask=1;mask<(1<<a.length);mask++){const ids=a.map((_,i)=>i).filter(i=>mask&(1<<i));if(det(ids.map(i=>ids.map(j=>a[i][j])))<0)return false;}return true;}
for(const [n,range] of [[2,[-2,-1,0,1,2]],[3,[-1,0,1]]]){
 const positions=[];for(let i=0;i<n;i++)for(let j=i;j<n;j++)positions.push([i,j]);
 for(let code=0;code<range.length**positions.length;code++){let x=code;const a=Array.from({length:n},()=>Array(n).fill(0));for(const [i,j] of positions){a[i][j]=a[j][i]=range[x%range.length];x=Math.floor(x/range.length);}let pass=true;try{V.psd(V.matrix(a));}catch{pass=false;}eq(pass,principalPSD(a));}
}
const demo='state,task,next\n0,2,3\n1,2,1\n2,3,1\n3,0,2';
const history=V.synthesizeCausal({text:demo,budget:2,mode:'history'}),closed=V.synthesizeCausal({text:demo,budget:2,mode:'closed'});
eq(history.error,'1');eq(closed.error,'3/2');
function witness(r,task,next){
 const index=new Map(r.witness.map((w,i)=>[w.code,i])),limit=Q.parse(r.error);
 for(let i=0;i<task.length;i++){
  let native=i,code=index.get(r.initialization[i].code);const seen=new Set();
  while(!seen.has(native+','+code)){
   seen.add(native+','+code);const w=r.witness[code];ok(w.states.includes(String(native)));
   const e=Q.parse(String(task[native])).sub(Q.parse(w.output));ok(e.cmp(limit)<=0&&e.cmp(new Q(-limit.n,limit.d))>=0);
   if(r.mode==='closed')eq(code,index.get(r.initialization[native].code));
   native=next[native];code=index.get(w.next);
  }
 }
}
witness(history,[2,2,3,0],[3,1,1,2]);witness(closed,[2,2,3,0],[3,1,1,2]);
// Independent machine oracle: enumerate updates and initial encodings, then
// follow native/predictor pairs. No cell-family search is used.
function brute(task,next,mode){const n=task.length;let best=Infinity;
 for(let f=0;f<4;f++)for(let seed=0;seed<(1<<n);seed++){
  const transition=[f&1,(f>>1)&1],initial=Array.from({length:n},(_,i)=>(seed>>i)&1);
  if(mode==='closed'&&next.some((j,i)=>initial[j]!==transition[initial[i]]))continue;
  const cells=[new Set(),new Set()];
  for(let i=0;i<n;i++){let x=i,q=initial[i];const seen=new Set();while(!seen.has(x+','+q)){seen.add(x+','+q);cells[q].add(x);x=next[x];q=transition[q];}}
  const error=Math.max(...cells.map(c=>c.size?(Math.max(...[...c].map(i=>task[i]))-Math.min(...[...c].map(i=>task[i])))/2:0));best=Math.min(best,error);
 }return String(best===Math.floor(best)?best:best*2+'/2');
}
let oracleCases=0;
for(let f=0;f<27;f++)for(let t=0;t<27;t++){
 let a=f,b=t;const next=[],task=[];for(let i=0;i<3;i++){next.push(a%3);a=Math.floor(a/3);task.push(b%3);b=Math.floor(b/3);}
 const text='state,task,next\n'+task.map((v,i)=>[i,v,next[i]].join(',')).join('\n');
 for(const mode of ['history','closed']){const r=V.synthesizeCausal({text,budget:2,mode});eq(r.error,brute(task,next,mode));witness(r,task,next);oracleCases++;}
}
rejects(()=>V.synthesizeCausal({text:demo,budget:4,mode:'history'}));rejects(()=>V.synthesizeCausal({text:'state,task,next\na,1,',budget:2,mode:'history'}));rejects(()=>V.synthesizeCausal({text:demo,budget:2,mode:'garbage'}));
const decay=V.decayBudget({M:'1',L:'1/2',epsilon:'1/8',dimension:2,actions:2});
eq(decay.K,4);eq(decay.h,'1/32');eq(decay.J,'33');eq(decay.labels,'4489');eq(decay.tailBound,'1/16');eq(decay.guaranteedError,'1/16');eq(decay.oracleAccuracy,'1/64');eq(decay.stateBound,'6056811824360306133893955506225902598921014295965922837');
eq(V.decayBudget({M:'0',L:'1/2',epsilon:'1/8',dimension:2,actions:2}).stateBound,'1');
rejects(()=>V.decayBudget({M:1,L:1,epsilon:'1/8',dimension:2,actions:2}));
rejects(()=>V.decayBudget({M:1,L:'1/2',epsilon:0,dimension:2,actions:2}));
rejects(()=>V.decayBudget({M:1,L:'1/2',epsilon:'1/8',dimension:0,actions:2}));
eq(uniformGap('0').lowerExpression,'2');eq(uniformGap('3/64').lowerExpression,'1/2');eq(uniformGap('-3/64').lowerExpression,'1/2');ok(!uniformGap('0.1').applicable);eq(uniformGap('0.00348').radicand,'2893/3125');rejects(()=>uniformGap('invalid'));
const summary={passed:true,assertions:checks,independentMachineCases:oracleCases,quantumOptima:certs.length,independentPSDCases:854};
console.log(JSON.stringify(summary,null,2));
