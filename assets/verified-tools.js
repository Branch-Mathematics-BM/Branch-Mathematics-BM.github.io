'use strict';
document.addEventListener('DOMContentLoaded',()=>{
 const $=id=>document.getElementById(id),esc=x=>String(x).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const jobs=new Map();let cases=null,casePromise=null;
 function stop(kind){const job=jobs.get(kind);if(job){job.worker.terminate();clearTimeout(job.timer);jobs.delete(kind);}$(kind+'-run').disabled=false;$(kind+'-stop').hidden=true;}
 function changed(kind){stop(kind);$(kind+'-result').textContent='Inputs changed. Run this tool to update the result.';$(kind+'-status').textContent='';}
 function run(kind,tool,input,render){
  stop(kind);$(kind+'-result').textContent='';$(kind+'-status').textContent='Calculating with exact rational arithmetic…';$(kind+'-run').disabled=true;$(kind+'-stop').hidden=false;
  try{
   const worker=new Worker('assets/verified-worker.js?v=20261023');
   const timer=setTimeout(()=>{if(jobs.get(kind)?.worker!==worker)return;stop(kind);$(kind+'-status').textContent='The time limit was reached. Increase it under Advanced or use the downloadable reference program.';},Number($('time-limit').value));
   jobs.set(kind,{worker,timer});
   worker.onmessage=event=>{if(jobs.get(kind)?.worker!==worker)return;stop(kind);if(event.data.ok){$(kind+'-result').innerHTML=render(event.data.result);$(kind+'-status').textContent='Exact calculation complete.';}else $(kind+'-status').textContent=event.data.error;};
   worker.onerror=()=>{if(jobs.get(kind)?.worker!==worker)return;stop(kind);$(kind+'-status').textContent='The exact tool could not start. Refresh and try again.';};
   worker.postMessage({tool,input});
  }catch(error){stop(kind);$(kind+'-status').textContent=error.message;}
 }
 for(const kind of ['causal','quantum','decay']){
  $(kind+'-stop').addEventListener('click',()=>{stop(kind);$(kind+'-status').textContent='Calculation stopped.';});
  $(kind+'-form').addEventListener('input',()=>changed(kind));
 }
 $('causal-form').addEventListener('submit',event=>{
  event.preventDefault();run('causal','synthesizeCausal',{text:$('causal-data').value,budget:$('causal-budget').value,mode:$('causal-mode').value},r=>{
   let html=`<div class="result-metrics"><div><strong>${esc(r.error)}</strong><span>Optimal worst-case error</span></div><div><strong>${r.predictorStates}</strong><span>Predictor states used</span></div><div><strong>${r.mode==='history'?'History':'Closed encoder'}</strong><span>Chosen contract</span></div></div>`;
   html+='<div class="table-wrap"><table class="table"><caption>Exact predictor witness</caption><thead><tr><th>Code</th><th>Compatible native states</th><th>Output</th><th>Next code</th><th>Cell error</th></tr></thead><tbody>';
   html+=r.witness.map(w=>`<tr><td>${esc(w.code)}</td><td>${esc(w.states.join(', '))}</td><td>${esc(w.output)}</td><td>${esc(w.next)}</td><td>${esc(w.error)}</td></tr>`).join('')+'</tbody></table></div>';
   html+=`<p>Initialization: ${esc(r.initialization.map(v=>v.state+' → '+v.code).join('; '))}.</p><p>Budget frontier: ${esc(r.frontier.map(v=>v.budget+' state'+(v.budget===1?'':'s')+': error '+v.error).join('; '))}.</p><p class="small">${esc(r.method)}. ${esc(r.scope)}</p>`;return html;
  });
 });
 $('causal-example').addEventListener('click',()=>{$('causal-data').value='state,task,next\n0,2,3\n1,2,1\n2,3,1\n3,0,2';$('causal-budget').value='2';$('causal-mode').value='history';changed('causal');});
 function quantumRender(r){return `<div class="result-metrics"><div><strong>${r.exact?esc(r.errorInterval[0]):esc(r.errorInterval.join(' to '))}</strong><span>${r.exact?'Exact recovery optimum':'Certified error interval'}</span></div><div><strong>${r.signals}</strong><span>Signal states</span></div><div><strong>${r.dimension}</strong><span>Output dimension</span></div></div><p>Primal/dual success interval: [${esc(r.successInterval.join(', '))}]. Every density matrix, measurement, probability weight, and dual slack passed exact checks.</p><p class="small">${esc(r.method)}. ${esc(r.scope)}</p>`;}
 $('quantum-form').addEventListener('submit',event=>{event.preventDefault();try{const input=JSON.parse($('quantum-data').value);run('quantum','verifyQuantum',input,quantumRender);}catch(error){changed('quantum');$('quantum-status').textContent='Invalid certificate JSON: '+error.message;}});
 async function loadCases(){
  if(cases)return cases;
  if(!casePromise)casePromise=fetch('downloads/bm-2026-10-23/BM_Quantum_Certificates_2026-10-23.json').then(response=>{if(!response.ok)throw Error('The published examples could not be downloaded. You can still paste a certificate.');return response.json();}).then(data=>{
   cases=data.certificates;const select=$('quantum-case');select.replaceChildren();cases.forEach((item,i)=>{const option=document.createElement('option');option.value=String(i);option.textContent=item.name;select.append(option);});return cases;
  }).catch(error=>{casePromise=null;throw error;});
  return casePromise;
 }
 $('quantum-tools').addEventListener('toggle',()=>{if($('quantum-tools').open)loadCases().catch(error=>{$('quantum-status').textContent=error.message;});});
 $('quantum-load').addEventListener('click',async()=>{try{const data=await loadCases();$('quantum-data').value=JSON.stringify(data[Number($('quantum-case').value)||0],null,2);changed('quantum');}catch(error){$('quantum-status').textContent=error.message;}});
 $('decay-form').addEventListener('submit',event=>{
  event.preventDefault();run('decay','decayBudget',{M:$('decay-M').value,L:$('decay-L').value,epsilon:$('decay-epsilon').value,dimension:$('decay-dimension').value,actions:$('decay-actions').value},r=>`<div class="result-metrics"><div><strong>${r.K}</strong><span>Forecast depth K</span></div><div><strong>${esc(r.guaranteedError)}</strong><span>Guaranteed task error</span></div><div><strong>${esc(r.h)}</strong><span>Grid spacing h</span></div></div><h3>Sufficient finite state bound</h3><pre class="answer exact-large">${esc(r.stateBound||r.stateBoundFormula)}</pre><p>Output labels: ${esc(r.labels)}. Tail bound at K: ${esc(r.tailBound)}. Required accuracy of each initial response coordinate: ${esc(r.oracleAccuracy)}.</p><p class="small">${esc(r.method)}. ${esc(r.scope)} Initialization may select more than one valid code for the same native state.</p>`);
 });
 function openTarget(){const id=location.hash.slice(1);if(['causal-tools','quantum-tools','decay-tools'].includes(id)){$('advanced').open=true;$(id).open=true;}}
 openTarget();window.addEventListener('hashchange',openTarget);
 document.addEventListener('bm-session-restored',()=>{for(const kind of ['causal','quantum','decay'])changed(kind);});
});
