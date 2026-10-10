'use strict';
document.addEventListener('DOMContentLoaded',()=>{
 const $=id=>document.getElementById(id),esc=x=>String(x).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const examples={system:'x+y=10; x-y=2',algebra:'factor(x^2-1); expand((x+1)^3); x^2=4',calculus:'diff(x^3,x); integrate(x^2,x); diff(sin(x),x)',values:'x=2; y=x+1; x^2+y; sqrt(2)'};
 const finiteExamples={future:'a,left,0,a\nb,left,0,c\nc,right,1,c\nd,right,1,c',exact:'a,left,0,c\nb,left,0,d\nc,right,1,a\nd,right,1,b',loss:'a,low,-1,a\nb,low,1,b\nc,high,3,c\nd,high,5,d',partial:'a,same,0,a\nb,same,0,'};
 let worker=null,timer=null,answerText='',requestId=0;
 function stop(){requestId++;if(worker)worker.terminate();worker=null;clearTimeout(timer);$('calculate').disabled=false;$('cancel').hidden=true;}
 function invalidate(){stop();answerText='';$('quick-result').hidden=true;$('copy-result').disabled=true;$('download-result').disabled=true;$('quick-status').textContent='Inputs changed. Press Enter or Calculate to update the answer.';}
 function download(name,text,type='text/plain'){const url=URL.createObjectURL(new Blob([text],{type})),a=document.createElement('a');a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}
 function renderRow(row){
  let out=`<article class="answer-row"><h3>${esc(row.input)}</h3>`;
  if(row.error)out+=`<p class="error-message">${esc(row.error)}</p>`;else out+=`<pre class="answer">${esc(row.answer)}</pre>`;
  if(row.approx)out+=`<p class="small">Approximate: ${esc(row.approx)}</p>`;
  if(row.method)out+=`<p class="small">${esc(row.method)}</p>`;
  if(row.checks){const checks=row.checks.map(c=>c.residual!==undefined?`${c.value}: residual ${c.residual}`:Object.entries(c.values).map(([k,v])=>`${k}=${v}`).join(', ')+': residuals '+c.residuals.join(', '));out+=`<details><summary>Substitution checks</summary><pre class="validation">${esc(checks.join('\n'))}</pre><p class="small">Zero residuals confirm the substituted equalities after symbolic simplification. They do not restore cancelled domain restrictions or prove that all solutions were found.</p></details>`;}
  if(row.partial)out+='<p class="error-message">The solver marked this result as partial or unresolved.</p>';
  if(row.note)out+=`<p class="small">${esc(row.note)}</p>`;return out+'</article>';
 }
 function renderQuick(result){
  const rows=[...(result.system?[result.system]:[]),...result.rows];$('quick-result').innerHTML=rows.map(renderRow).join('')+`<p class="small">${esc(result.note)}</p>`;$('quick-result').hidden=false;
  answerText=rows.map(r=>`${r.input}\n${r.error||r.answer}${r.approx?'\nApproximate: '+r.approx:''}${r.note?'\n'+r.note:''}`).join('\n\n')+'\n\n'+result.note;
  $('copy-result').disabled=false;$('download-result').disabled=false;$('quick-status').textContent=rows.some(r=>r.error)?'Finished with an input or solver limitation shown below.':'Calculation complete.';
 }
 function run(){
  stop();answerText='';$('quick-result').hidden=true;$('copy-result').disabled=true;$('download-result').disabled=true;
  if(!$('equations-input').value.trim()){$('quick-status').textContent='Paste an expression or equation first.';$('equations-input').focus();return;}
  const id=requestId;$('quick-status').textContent='Calculating…';$('calculate').disabled=true;$('cancel').hidden=false;
  try{worker=new Worker('assets/equation-worker.js');
   timer=setTimeout(()=>{if(id!==requestId)return;stop();$('quick-status').textContent='The time limit was reached. Try a smaller system or increase the limit under Advanced.';},Number($('time-limit').value));
   worker.onmessage=e=>{if(id!==requestId)return;stop();if(e.data.ok)renderQuick(e.data.result);else $('quick-status').textContent=e.data.error;};
   worker.onerror=()=>{if(id!==requestId)return;stop();$('quick-status').textContent='The calculation engine could not start. Refresh this page and try again.';};
   worker.postMessage({text:$('equations-input').value,target:$('solve-for').value});
  }catch{stop();$('quick-status').textContent='This browser could not start the calculation worker. Use a current browser with JavaScript enabled.';}
 }
 $('quick-form').addEventListener('submit',e=>{e.preventDefault();run();});
 $('equations-input').addEventListener('keydown',e=>{if(e.key==='Enter'&&!e.shiftKey&&!e.isComposing){e.preventDefault();run();}});
 for(const id of ['equations-input','solve-for','time-limit'])$(id).addEventListener('input',invalidate);
 document.querySelectorAll('[data-example]').forEach(button=>button.addEventListener('click',()=>{$('equations-input').value=examples[button.dataset.example];$('solve-for').value='';run();}));
 $('cancel').addEventListener('click',()=>{stop();$('quick-status').textContent='Calculation stopped.';});
 $('clear').addEventListener('click',()=>{$('equations-input').value='';invalidate();$('quick-status').textContent='';$('equations-input').focus();});
 $('copy-result').addEventListener('click',async()=>{try{await navigator.clipboard.writeText(answerText);$('quick-status').textContent='Answer copied.';}catch{$('quick-status').textContent='Clipboard access was unavailable. Use Download answer instead.';}});
 $('download-result').addEventListener('click',()=>download('BM-calculation.txt',answerText));
 function runFinite(){
  $('finite-error').textContent='';$('finite-result').textContent='';
  try{const r=BMCalc.analyze($('state-data').value,$('check-dynamics').checked);let witnesses=[];
   if(r.staticWitness){const[a,b]=r.staticWitness;witnesses.push(`Task counterexample: ${a.id} and ${b.id} both look like “${a.representation}”, but their task values are ${a.value} and ${b.value}.`);}
   if(r.domainWitness){const[a,b]=r.domainWitness;witnesses.push(`Domain counterexample: ${a.id} has no next state, but ${b.id} does. Both have the same observation.`);}
   if(r.closureWitness){const[a,b]=r.closureWitness;witnesses.push(`Evolution counterexample: ${a.id} goes to observation “${r.byId.get(a.next).representation}”, while ${b.id} goes to “${r.byId.get(b.next).representation}”. They currently share an observation.`);}
   let html=`<div class="result-metrics"><div><strong>${r.staticPass?'Pass':'Fail'}</strong><span>Exact task sufficiency</span></div><div><strong>${r.dynamicPass===null?'Not requested':r.dynamicPass?'Pass':'Fail'}</strong><span>Dynamic closure</span></div><div><strong>${esc(r.error)}</strong><span>Best worst-case task error</span></div></div>`;
   html+=witnesses.map(w=>`<p class="callout warn">${esc(w)}</p>`).join('');
   if(r.checkDynamics&&!r.definedTransitions)html+='<p>No transitions were supplied. The partial-domain closure test passes vacuously; no future evolution is asserted.</p>';
   html+='<h3>What each observation can recover</h3><div class="table-wrap" role="region" aria-label="Fibre results" tabindex="0"><table class="table"><thead><tr><th>Observation</th><th>States</th><th>Task range</th><th>Optimal midpoint decoder</th><th>Worst error</th></tr></thead><tbody>';
   html+=r.fibres.map(f=>`<tr><td>${esc(f.label)}</td><td>${esc(f.states.join(', '))}</td><td>[${esc(f.min)}, ${esc(f.max)}]</td><td>${esc(f.decoder)}</td><td>${esc(f.error)}</td></tr>`).join('')+'</tbody></table></div>';
   html+=`<p class="small">For one real-valued task with absolute error and unrestricted real-valued decoders, the exact minimax error is half the largest fibre diameter: ${esc(r.diameter)} / 2 = ${esc(r.error)}.</p><h3>Smallest refinement for this table</h3><p>${r.fibres.length} original observation classes → ${r.partition.length} refined classes (${r.partition.length-r.fibres.length} additional classes). ${r.checkDynamics?'This refinement preserves the task and closes the declared partial dynamics.':'This refinement preserves the task; dynamics were not checked.'}</p><ul>`;
   html+=r.partition.map((g,i)=>`<li>Class ${i+1}: ${esc(g.join(', '))}</li>`).join('')+'</ul><p class="small">This is the coarsest refinement of the supplied representation satisfying the selected conditions on the complete finite table. It does not certify a model outside those states.</p>';
   $('finite-result').innerHTML=html;
  }catch(e){$('finite-error').textContent=e.message;}
 }
 $('finite-form').addEventListener('submit',e=>{e.preventDefault();runFinite();});
 $('load-finite').addEventListener('click',()=>{$('state-data').value='state,representation,task,next\n'+finiteExamples[$('finite-example').value];runFinite();});
 for(const id of ['state-data','check-dynamics'])$(id).addEventListener('input',()=>{$('finite-result').textContent='Inputs changed. Run exact BM checks again.';$('finite-error').textContent='';});
 let spectralRequest=0;const cache={};
 async function spectrum(){
  const id=++spectralRequest,g=$('geometry').value,b=$('coupling').value;const path=`downloads/steadman-yang-mills-2026-10-09/${g}_certificates.json`;
  $('spectral-status').textContent='Loading the published certificate…';$('spectral-result').textContent='';
  try{if(!cache[g]){const response=await fetch(path);if(!response.ok)throw Error('Certificate download failed.');cache[g]=await response.json();}if(id!==spectralRequest)return;
   const data=cache[g],r=data.cases.find(c=>c.beta===b);if(!r?.certified)throw Error('No certified case found for this selection.');
   $('spectral-result').innerHTML=`<pre class="answer">${esc(r.gap_interval[0])} ≤ Δ / c_K ≤ ${esc(r.gap_interval[1])}</pre><p>${data.plaquettes} plaquettes · ${data.retained_dimension} retained states · open boundary</p><p>Crude omitted-sector floor: ${esc(r.crude_tail_floor)}<br>Selected floor interval: [${esc(r.improved_tail_floor.join(', '))}]</p><p><a href="${path}">View exact rational certificate JSON →</a></p>`;
   $('spectral-status').textContent='Published finite-geometry certificate loaded.';
  }catch(e){if(id===spectralRequest)$('spectral-status').textContent=e.message+' Retry by changing the selection.';}
 }
 $('spectral').addEventListener('toggle',()=>{if($('spectral').open)spectrum();});for(const id of ['geometry','coupling'])$(id).addEventListener('change',spectrum);
 const inputIds=['equations-input','solve-for','time-limit','state-data','geometry','coupling'];
 function session(){return{format:'BM-calculator-session',version:1,inputs:Object.fromEntries(inputIds.map(id=>[id,$(id).value])),checkDynamics:$('check-dynamics').checked};}
 function restore(data){
  if(data?.format!=='BM-calculator-session'||data.version!==1||typeof data.inputs!=='object'||data.inputs===null||typeof data.checkDynamics!=='boolean')throw Error('Not a supported BM calculator session.');
  for(const id of inputIds){const value=data.inputs[id],element=$(id);if(typeof value!=='string'||value.length>(element.maxLength>0?element.maxLength:60000))throw Error('Invalid or oversized session input.');if(element.tagName==='SELECT'&&![...element.options].some(o=>o.value===value))throw Error('Invalid saved selection.');}
  for(const id of inputIds)$(id).value=data.inputs[id];$('check-dynamics').checked=data.checkDynamics;invalidate();$('finite-result').textContent='Restored inputs. Run the checker to calculate their result.';if($('spectral').open)spectrum();
 }
 $('save-session').addEventListener('click',()=>{try{localStorage.setItem('bm-calculator-v1',JSON.stringify(session()));$('session-status').textContent='Inputs saved on this browser.';}catch{$('session-status').textContent='Browser storage is unavailable. Export the session instead.';}});
 $('load-session').addEventListener('click',()=>{try{const value=localStorage.getItem('bm-calculator-v1');if(!value)throw Error('No saved session on this browser.');restore(JSON.parse(value));$('session-status').textContent='Saved inputs restored.';}catch(e){$('session-status').textContent=e.message;}});
 $('export-session').addEventListener('click',()=>download('BM-calculator-session.json',JSON.stringify(session(),null,2),'application/json'));
 $('import-session').addEventListener('change',async e=>{const file=e.target.files[0];if(!file)return;try{if(file.size>150000)throw Error('Session files must be smaller than 150 KB.');restore(JSON.parse(await file.text()));$('session-status').textContent='Session imported. Press Calculate when ready.';}catch(e){$('session-status').textContent=e.message;}finally{$('import-session').value='';}});
});
