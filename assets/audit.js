'use strict';
document.addEventListener('DOMContentLoaded',async()=>{
 const $=id=>document.getElementById(id),esc=x=>String(x??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 let rows=[],sourceMap=new Map(),visible=100,filtered=[];
 const more=document.createElement('button');more.type='button';more.className='btn';more.id='audit-more';more.textContent='Show 100 more entries';$('audit-results').after(more);more.hidden=true;
 function render(){
  const terms=$('audit-query').value.toLowerCase().trim().split(/\s+/).filter(Boolean),framework=$('audit-framework').value,label=$('audit-label').value;
  filtered=rows.filter(r=>(!framework||r.framework===framework)&&(!label||r.classification===label)&&terms.every(t=>r._search.includes(t)));
  $('audit-status').textContent=`Showing ${Math.min(visible,filtered.length)} of ${filtered.length} matching entries (${rows.length} total).`;
  $('audit-results').innerHTML=filtered.slice(0,visible).map(r=>{
   const sources=r.sources.split(';').filter(Boolean).map(id=>{const source=sourceMap.get(id);return source?`<a href="${esc(source.url)}">${esc(id)}</a>`:esc(id);}).join(' · ');
   const fields=[['Statement',r.statement],['Assumptions',r.assumptions],['Evidence',r.evidence],['Dependencies',r.dependencies||'No inventory dependency specified'],['Remaining work / scope',r.remaining_work],['Source clause',r.clause],['Gates',r.gates||'No active completion gate']];
   return `<details class="audit-row" id="entry-${esc(r.id)}"><summary><span class="audit-id">${esc(r.id)}</span><span class="audit-name">${esc(r.name)}</span><span class="audit-label">${esc(r.classification)}</span></summary><div class="audit-detail"><p class="small">${esc(r.framework)} · ${esc(r.layer)} · ${esc(r.lifecycle)}</p><dl>${fields.map(([k,v])=>`<dt>${esc(k)}</dt><dd>${esc(v)}</dd>`).join('')}</dl><p>Source documents: ${sources}</p></div></details>`;
  }).join('')||'<p>No matching entries. Try a shorter search or remove a filter.</p>';
  more.hidden=visible>=filtered.length;
 }
 function reset(){visible=100;render();}
 try{
  const response=await fetch('downloads/bm-2026-10-23/BM_Completeness_Public_2026-10-23.json');if(!response.ok)throw Error('Ledger download failed.');
  const data=await response.json();
  const extraResponse=await fetch('downloads/bm-2026-11-13/BM_November_Result_Supplement.json');if(!extraResponse.ok)throw Error('Supplement download failed.');
  const extra=await extraResponse.json();data.inventory.push(...extra.inventory);data.sources.push(...extra.sources);
  rows=data.inventory.map(r=>({...r,_search:[r.id,r.name,r.framework,r.classification,r.lifecycle,r.statement,r.assumptions,r.evidence,r.remaining_work,r.sources].join(' ').toLowerCase()}));sourceMap=new Map(data.sources.map(s=>[s.id,s]));
  $('audit-query').addEventListener('input',reset);$('audit-framework').addEventListener('change',reset);$('audit-label').addEventListener('change',reset);more.addEventListener('click',()=>{visible+=100;render();});render();
 }catch(error){$('audit-status').textContent='The searchable ledger could not load. Use the dated JSON downloads above; the static summary remains available.';}
});
