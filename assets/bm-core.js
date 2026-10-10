/* Exact finite-set BM calculations. No expression evaluation or remote service. */
(function(root){
'use strict';
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;}
class Q{
 constructor(n,d=1n){if(!d)throw Error('A fraction cannot have denominator zero.');if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
 static parse(value){const s=String(value).trim();if(s.length>128)throw Error('Keep each number to 128 characters or fewer.');
  if(/^[+-]?\d+\s*\/\s*[+-]?\d+$/.test(s)){const[a,b]=s.split('/');return new Q(BigInt(a.trim()),BigInt(b.trim()));}
  const m=s.match(/^([+-]?)(\d+(?:\.\d*)?|\.\d+)(?:[eE]([+-]?\d+))?$/);
  if(!m)throw Error(`“${s}” is not a number. Use a decimal or a fraction such as 1/3.`);
  const exp=Number(m[3]||0);if(Math.abs(exp)>50)throw Error('Exponents must be between −50 and 50.');
  const[whole,part='']=m[2].split('.');const n=BigInt((whole||'0')+part)*(m[1]==='-'?-1n:1n),scale=part.length-exp;
  return scale>=0?new Q(n,10n**BigInt(scale)):new Q(n*10n**BigInt(-scale));
 }
 add(q){return new Q(this.n*q.d+q.n*this.d,this.d*q.d);}sub(q){return new Q(this.n*q.d-q.n*this.d,this.d*q.d);}
 div(q){return new Q(this.n*q.d,this.d*q.n);}cmp(q){const v=this.n*q.d-q.n*this.d;return v<0n?-1:v>0n?1:0;}
 toString(){return this.d===1n?String(this.n):`${this.n}/${this.d}`;}
}
const zero=new Q(0n),two=new Q(2n);
function csv(text){
 if(text.length>60000)throw Error('This checker accepts at most 60,000 characters.');
 const rows=[];let row=[],field='',quoted=false,closed=false;
 const put=()=>{row.push(field.trim());field='';closed=false;};const end=()=>{put();if(row.some(Boolean))rows.push(row);row=[];};
 text=text.replace(/^\uFEFF/,'').replace(/\r\n?/g,'\n');
 for(let i=0;i<text.length;i++){const c=text[i];
  if(quoted){if(c==='"'){if(text[i+1]==='"'){field+='"';i++;}else{quoted=false;closed=true;}}else field+=c;continue;}
  if(c===','){put();continue;}if(c==='\n'){end();continue;}
  if(closed){if(!/\s/.test(c))throw Error('Only a comma or a new line may follow a closing CSV quote.');continue;}
  if(c==='"'){if(field.trim())throw Error('Quotes must surround the whole CSV field.');field='';quoted=true;}else field+=c;
 }
 if(quoted)throw Error('A quoted CSV field is missing its closing quote.');end();return rows;
}
function parse(text,checkDynamics=true){
 const rows=csv(text),header=rows.shift();
 if(!header||header.join(',').toLowerCase()!=='state,representation,task,next')throw Error('Use the header: state,representation,task,next');
 if(!rows.length)throw Error('Add at least one state below the header.');if(rows.length>200)throw Error('This finite checker supports up to 200 states.');
 const seen=new Set(),states=rows.map((r,i)=>{
  if(r.length!==4)throw Error(`Data row ${i+1}: expected four CSV fields; leave the final field empty for an undefined transition.`);
  const[id,representation,task,next]=r;if(!id||!representation)throw Error(`Data row ${i+1}: state and representation labels cannot be empty.`);
  if(id.length>160||representation.length>160)throw Error(`Data row ${i+1}: labels must be at most 160 characters.`);
  if(seen.has(id))throw Error(`State “${id}” occurs more than once.`);seen.add(id);
  let value;try{value=Q.parse(task);}catch(e){throw Error(`Task at state “${id}”: ${e.message}`);}
  return{id,representation,value,next:next||null};
 });
 if(checkDynamics)for(const s of states)if(s.next!==null&&!seen.has(s.next))throw Error(`State “${s.id}” points to unknown next state “${s.next}”. Add that state or leave next empty.`);
 return states;
}
function groups(states,key){const m=new Map();for(const s of states){const k=key(s);if(!m.has(k))m.set(k,[]);m.get(k).push(s);}return[...m.values()];}
function analyze(text,checkDynamics=true){
 const states=parse(text,checkDynamics),byId=new Map(states.map(s=>[s.id,s])),fibres=groups(states,s=>s.representation);
 let witness=null,domainWitness=null,closureWitness=null,diameter=zero;
 const fibreResults=fibres.map(f=>{
  let min=f[0].value,max=f[0].value;for(const s of f){if(s.value.cmp(min)<0)min=s.value;if(s.value.cmp(max)>0)max=s.value;}
  const width=max.sub(min);if(width.cmp(diameter)>0)diameter=width;
  if(!witness){const other=f.find(s=>s.value.cmp(f[0].value)!==0);if(other)witness=[f[0],other];}
  if(checkDynamics){const undefinedState=f.find(s=>s.next===null),definedState=f.find(s=>s.next!==null);
   if(undefinedState&&definedState&&!domainWitness)domainWitness=[undefinedState,definedState];
   if(definedState){const target=byId.get(definedState.next).representation,other=f.find(s=>s.next!==null&&byId.get(s.next).representation!==target);if(other&&!closureWitness)closureWitness=[definedState,other];}
  }
  return{label:f[0].representation,states:f.map(s=>s.id),min,max,diameter:width,error:width.div(two),decoder:min.add(max).div(two)};
 });
 let partition=groups(states,s=>JSON.stringify([s.representation,s.value.toString()]));const taskGroups=partition.length;let refinementRounds=0;
 if(checkDynamics)while(true){const cls=new Map();partition.forEach((g,i)=>g.forEach(s=>cls.set(s.id,i)));
  const refined=partition.flatMap(g=>groups(g,s=>s.next===null?'undefined':String(cls.get(s.next))));
  if(refined.length===partition.length)break;partition=refined;refinementRounds++;
 }
 return{states,byId,fibres:fibreResults,staticPass:!witness,staticWitness:witness,checkDynamics,domainWitness,closureWitness,
  dynamicPass:checkDynamics?!domainWitness&&!closureWitness:null,diameter,error:diameter.div(two),partition:partition.map(g=>g.map(s=>s.id)),taskGroups,refinementRounds,definedTransitions:states.filter(s=>s.next!==null).length};
}
// Conditional scalar Schur enclosure; operator assumptions must be certified separately.
function schur(input){
 const keys=['a0lo','a0hi','a1lo','a1hi','d','b2'],q={};for(const n of keys)q[n]=Q.parse(input[n]);
 if(q.a0lo.cmp(q.a0hi)>0||q.a1lo.cmp(q.a1hi)>0)throw Error('Each Ritz lower endpoint must be no larger than its upper endpoint.');
 if(q.a0lo.cmp(q.a1hi)>0)throw Error('The Ritz intervals cannot contain ordered ground and first-excited energies.');
 if(q.b2.cmp(zero)<0)throw Error('The squared coupling bound cannot be negative.');
 if(q.d.cmp(q.a1hi)<=0||q.d.cmp(q.a0hi)<=0)throw Error('This scalar shortcut requires the omitted-sector floor to exceed both Ritz upper endpoints.');
 const l0=q.a0lo.sub(q.b2.div(q.d.sub(q.a0lo))),l1=q.a1lo.sub(q.b2.div(q.d.sub(q.a1lo))),rawLower=l1.sub(q.a0hi),upper=q.a1hi.sub(l0);
 if(upper.cmp(zero)<0)throw Error('These inputs produce inconsistent spectral bounds.');
 return{q,l0,l1,rawLower,lower:rawLower.cmp(zero)<0?zero:rawLower,upper,positive:rawLower.cmp(zero)>0};
}
const api={Q,csv,parse,analyze,schur};if(typeof module!=='undefined'&&module.exports)module.exports=api;root.BMCalc=api;
})(typeof window!=='undefined'?window:globalThis);
