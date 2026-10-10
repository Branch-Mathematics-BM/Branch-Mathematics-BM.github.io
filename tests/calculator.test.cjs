const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const root=path.resolve(__dirname,'..');
const {calculate,normalize}=require(root+'/assets/equation-worker');
const {Q,analyze,schur}=require(root+'/assets/bm-core');
let checks=0;function ok(v,msg){assert.ok(v,msg);checks++;}function eq(a,b){assert.deepEqual(a,b);checks++;}
let r=calculate({text:'x+y=10;x-y=2'});eq(r.substitutions,{x:'6',y:'4'});eq(r.system.checks[0].residuals,['0','0']);
eq(calculate({text:'x=2;y=x+1;x^2+y'}).rows[0].answer,'7');
eq(calculate({text:'x=2;diff(x^3,x)'}).rows[0].answer,'12');
ok(calculate({text:'x^2=4;x+1'}).rows[0].answer.includes('x=-2: -1'));
eq(calculate({text:'0.1+0.2'}).rows[0].answer,'0.3');
eq(calculate({text:'\\frac{1}{2}+\\frac{1}{3}'}).rows[0].answer,'5/6');
ok(calculate({text:'sin(x)=0'}).system.answer.includes('_n*pi'));
ok(calculate({text:'F=m*a'}).system.answer.includes('a*m'));
eq(calculate({text:'F=m*a;m=2;a=3'}).substitutions.F,'6');
ok(calculate({text:'x^2=-1'}).system.answer.includes('i'));
ok(calculate({text:'x/x=1'}).system.answer.includes('original expression domains'));
ok(calculate({text:'x=1;x=2'}).system.answer.includes('No solutions returned'));
ok(calculate({text:'1/0'}).rows[0].error);
ok(calculate({text:'∂t u+∇u=0'}).rows[0].error.includes('PDE'));
ok(calculate({text:'alert(1)'}).rows[0].error);
assert.throws(()=>calculate({text:''}));assert.throws(()=>calculate({text:'x=2',target:'x,x'}));checks+=2;
eq(Q.parse('1/3').add(Q.parse('1/6')).toString(),'1/2');eq(Q.parse('3e-2').toString(),'3/100');
const header='state,representation,task,next\n';
r=analyze(header+'a,L,0,a\nb,L,0,c\nc,R,1,c\nd,R,1,c');ok(r.staticPass);ok(!r.dynamicPass);eq(r.partition,[['a'],['b'],['c','d']]);
r=analyze(header+'a,L,-1,a\nb,L,1,b');eq(r.error.toString(),'1');eq(r.fibres[0].decoder.toString(),'0');ok(!r.staticPass);ok(r.dynamicPass);
r=analyze(header+'a,L,0,a\nb,L,0,');ok(r.domainWitness);ok(!r.dynamicPass);
r=analyze(header+'a,L,1/3,a\nb,L,2/6,b');ok(r.staticPass);eq(r.error.toString(),'0');
assert.throws(()=>analyze(header+'a,L,0,z'));assert.throws(()=>analyze(header+'a,L,0,a\na,R,1,a'));assert.throws(()=>Q.parse('1/0'));checks+=3;
eq(schur({a0lo:'0',a0hi:'0',a1lo:'12',a1hi:'12',d:'24',b2:'1'}).lower.toString(),'143/12');
// Independent pair-orbit oracle: compare all future observations/tasks and domain availability.
let seed=12345;const rand=n=>{seed=(seed*1664525+1013904223)>>>0;return seed%n;};
for(let trial=0;trial<50;trial++){
 const n=2+rand(5),states=Array.from({length:n},(_,i)=>({id:'s'+i,r:rand(3),t:rand(3),next:rand(n+1)-1}));
 const text=header+states.map(s=>[s.id,s.r,s.t,s.next<0?'':'s'+s.next].join(',')).join('\n');const result=analyze(text);
 const cls=new Map();result.partition.forEach((g,i)=>g.forEach(id=>cls.set(id,i)));
 function equivalent(i,j){const seen=new Set();while(true){const key=i+','+j;if(seen.has(key))return true;seen.add(key);const a=states[i],b=states[j];if(a.r!==b.r||a.t!==b.t||(a.next<0)!==(b.next<0))return false;if(a.next<0)return true;i=a.next;j=b.next;}}
 for(let i=0;i<n;i++)for(let j=0;j<n;j++)eq(cls.get('s'+i)===cls.get('s'+j),equivalent(i,j));
}
console.log('Calculator mathematical regression checks passed ('+checks+' assertions).');
