/* One isolated worker per calculation; the page enforces a hard time limit. */
'use strict';
if(typeof importScripts==='function')importScripts('vendor/nerdamer-2.0.0.js');
const engine=typeof nerdamer!=='undefined'?nerdamer:require('./vendor/nerdamer-2.0.0.js');
const allowed=new Set('sin cos tan asin acos atan atan2 sinh cosh tanh sec csc cot exp log ln sqrt abs sign factorial factor expand simplify diff integrate definite_integral limit sum product determinant invert transpose dot cross vector matrix solve solveeqs gcd lcm mod floor ceil round min max'.split(' '));
function normalize(input){
 let s=input.trim().replace(/[−–]/g,'-').replace(/[×·]/g,'*').replace(/÷/g,'/').replace(/π/g,'pi').replace(/√\s*\(/g,'sqrt(');
 const superDigits={'⁰':'0','¹':'1','²':'2','³':'3','⁴':'4','⁵':'5','⁶':'6','⁷':'7','⁸':'8','⁹':'9','⁻':'-'};
 s=s.replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+/g,x=>'^('+[...x].map(c=>superDigits[c]).join('')+')');
 if(/[∂∇∫]/.test(s))throw Error('This notation needs a declared differential problem. Use diff(expression,variable) or integrate(expression,variable) for supported calculus; general PDEs are not solved here.');
 s=s.replace(/^\$\$?|\$\$?$/g,'').replace(/^\\[([]|\\[)\]]$/g,'');
 if(s.includes('\\')){try{s=engine.convertFromLaTeX(s).toString();}catch{throw Error('Could not convert this LaTeX. Paste plain math, such as x^2 or diff(x^3,x).');}}
 if(/[:{}'"`<>]|=>/.test(s))throw Error('Use mathematical expressions and = equations, without programming statements or inequalities.');
 for(const m of s.matchAll(/([\p{L}_][\p{L}\p{N}_]*)\s*\(/gu))if(!allowed.has(m[1]))throw Error(`“${m[1]}(…)” is not a supported function. For multiplication use *, for example x*(x+1).`);
 return s;
}
function outerEquals(s){let depth=0,found=[];for(let i=0;i<s.length;i++){if('(['.includes(s[i]))depth++;if(')]'.includes(s[i]))depth--;if(depth<0)throw Error('Check the closing brackets.');if(s[i]==='='&&depth===0)found.push(i);}if(depth!==0)throw Error('Check the opening and closing brackets.');if(found.length>1)throw Error('Use one = per equation, and separate equations with semicolons.');return found[0]??-1;}
function residuals(equations,substitutions){
 return equations.map(eq=>{try{const i=outerEquals(eq),l=engine(eq.slice(0,i),substitutions).toString(),r=engine(eq.slice(i+1),substitutions).toString();return engine(`(${l})-(${r})`).expand().simplify().toString();}catch{return 'not verified';}});
}
function calculate(payload){
 if(typeof payload.text!=='string'||!payload.text.trim())throw Error('Paste at least one expression or equation.');
 if(payload.text.length>6000)throw Error('Please use at most 6,000 characters per calculation.');
 const chunks=payload.text.split(';').map(s=>s.trim()).filter(Boolean);if(chunks.length>30)throw Error('Please use at most 30 expressions or equations at once.');
 const requested=String(payload.target||'').split(',').map(s=>s.trim()).filter(Boolean);
 if(requested.length>12||requested.some(x=>!/^[_\p{L}][_\p{L}\p{N}]*$/u.test(x))||new Set(requested).size!==requested.length)throw Error('Optional unknowns must be distinct symbol names separated by commas, such as x,y.');
 const parsed=[],rows=[];
 for(const original of chunks){try{const normalized=normalize(original),equals=outerEquals(normalized);parsed.push({original,normalized,equals});}catch(e){rows.push({input:original,error:e.message});}}
 const equations=parsed.filter(p=>p.equals>=0),expressions=parsed.filter(p=>p.equals<0);let substitutions={},alternatives=[],system=null;
 if(equations.length){
  const sources=equations.map(p=>p.normalized);
  try{
   const detected=[...new Set(equations.flatMap(p=>[...engine(p.normalized.slice(0,p.equals)).variables(),...engine(p.normalized.slice(p.equals+1)).variables()]))].sort();
   if(detected.length>12)throw Error('This browser tool supports at most 12 unknowns per system.');
   const lhs=equations.length===1?equations[0].normalized.slice(0,equations[0].equals).trim():'';
   const variables=requested.length?requested:(detected.includes(lhs)?[lhs]:detected);
   if(!variables.length){const rs=residuals(sources,{});system={input:sources.join('; '),answer:rs.every(x=>x==='0')?'Identity on the original expression domains.':'The constant equations are not all equal.',method:'Constant equality check',note:'Cancelled denominators and other original domain restrictions still apply.'};}
   else if(sources.length===1&&variables.length===1){
    const result=engine.solve(sources[0],variables[0]);const vals=result.toArray().map(x=>x.toString());
    const isAll=vals.includes('all'),checks=vals.filter(v=>v!=='all').map(v=>({value:v,residual:residuals(sources,{[variables[0]]:v})[0]}));
    system={input:sources[0],answer:isAll?`${variables[0]}: all values in the original expression domain`:vals.length?`${variables[0]} ∈ { ${vals.join(', ')} }`:'No solutions returned by the solver.',method:`Single-equation solver · unknown ${variables[0]}`,note:'A solver result is not a completeness guarantee. Other symbols are parameters. Original domain restrictions apply. _n denotes an arbitrary integer in periodic families.',checks,partial:!!result.partial||!!(result.unsolved?.length)};
    alternatives=checks.filter(c=>c.residual==='0'&&engine(c.value).variables().length===0).map(c=>({[variables[0]]:c.value}));
    if(vals.length===1&&!isAll&&!result.partial&&alternatives.length===1)substitutions=alternatives[0];
   }else{
    const solution=engine.solveSystem(sources,variables);const sets=solution.elements.map(d=>Object.fromEntries([...d.entries()].map(([k,v])=>[k,v.toString()])));
    const checks=sets.map(values=>({values,residuals:residuals(sources,values)}));
    system={input:sources.join('; '),answer:sets.length?sets.map((s,i)=>(sets.length>1?`Solution ${i+1}: `:'')+Object.entries(s).map(([k,v])=>`${k} = ${v}`).join(', ')).join('\n'):'No solutions returned by the solver.',method:`System solver · unknowns ${variables.join(', ')}`,note:'Free symbols remain parameters. Nonlinear or numerical results may be incomplete; residual checks and original domain restrictions matter.',checks};
    alternatives=checks.filter(c=>c.residuals.every(x=>x==='0')&&Object.values(c.values).every(v=>engine(v).variables().length===0)).map(c=>c.values);
    if(sets.length===1&&alternatives.length===1)substitutions=alternatives[0];
   }
  }catch(e){system={input:sources.join('; '),error:`Could not solve this system: ${e.message}`,note:'The equations may be unsupported or may need a choice of unknowns in Advanced. This is not evidence that no mathematical solution exists.'};}
 }
 if(system&&rows.some(r=>r.error))system.note=(system.note||'')+' Some inputs could not be parsed; this system result uses only the accepted equations.';
 for(const p of expressions){try{
  const symbolic=engine(p.normalized);
  const evaluateWith=values=>symbolic.variables?engine(symbolic.toString(),values):symbolic;
  const result=evaluateWith(substitutions);let answer=result.toString(),approx=null;
  if(alternatives.length>1&&symbolic.variables?.().length){answer=alternatives.map(values=>{try{return Object.entries(values).map(([k,v])=>`${k}=${v}`).join(', ')+': '+evaluateWith(values).toString();}catch(e){return Object.entries(values).map(([k,v])=>`${k}=${v}`).join(', ')+': undefined ('+e.message+')';}}).join('\n');}
  if(/^integrate\(/.test(p.normalized))answer+=' + C (constant of integration)';
  if(result.variables?.().length===0&&typeof result.evaluate==='function'){const v=result.evaluate().toString();if(v!==result.toString())approx=v;}
  rows.push({input:p.original,answer,approx,method:alternatives.length>1&&symbolic.variables?.().length?'Expression evaluated on returned solution branches':Object.keys(substitutions).length?'Symbolic operation, then solved values substituted':'Symbolic expression evaluation'});
 }catch(e){rows.push({input:p.original,error:e.message});}}
 return{system,rows,substitutions,note:'Results use Nerdamer 2.0.0. Symbols have no automatic units; trigonometric angles are radians. This is a symbolic calculation, not an automatic proof of a physical model.'};
}
if(typeof self!=='undefined'&&typeof importScripts==='function')self.onmessage=e=>{try{self.postMessage({ok:true,result:calculate(e.data)});}catch(error){self.postMessage({ok:false,error:error.message});}};
if(typeof module!=='undefined'&&module.exports)module.exports={calculate,normalize,outerEquals};
