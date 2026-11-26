'use strict';
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict'),path=require('node:path');
const root=path.resolve(__dirname,'..');
function element(){return {value:'',textContent:'',innerHTML:'',hidden:false,listeners:{},addEventListener(t,f){this.listeners[t]=f;},after(){}};}
const elements=Object.fromEntries(['audit-query','audit-framework','audit-label','audit-status','audit-results'].map(x=>[x,element()]));
let init,more;
const document={getElementById:x=>elements[x],createElement:()=>more=element(),addEventListener:(t,f)=>{init=f;}};
const fetch=async url=>({ok:true,json:async()=>JSON.parse(fs.readFileSync(path.join(root,url),'utf8'))});
vm.runInNewContext(fs.readFileSync(path.join(root,'assets/audit.js'),'utf8'),{document,fetch,Map,String,Error});
(async()=>{
 await init();
 assert.match(elements['audit-status'].textContent,/677 total/);
 assert.equal(more.hidden,false);
 elements['audit-query'].value='NOV01-N3';elements['audit-query'].listeners.input();
 assert.match(elements['audit-results'].innerHTML,/Separate receiver quotients can fail jointly/);
 assert.match(elements['audit-results'].innerHTML,/BM_Set_Valued_Seed_Closure_and_Branching_2026-11-01.md/);
 assert.match(elements['audit-status'].textContent,/1 of 1 matching/);
 assert.equal(more.hidden,true);
 elements['audit-query'].value='';elements['audit-label'].value='Missing equation';elements['audit-label'].listeners.change();
 assert.match(elements['audit-status'].textContent,/7 of 7 matching/);
 elements['audit-label'].value='';elements['audit-query'].value='NOV01-F2';elements['audit-query'].listeners.input();
 assert.match(elements['audit-results'].innerHTML,/Minimal autonomous task quotient/);
 console.log('Audit loads both dated ledgers and filters their source-linked results correctly.');
})().catch(e=>{console.error(e);process.exitCode=1;});
