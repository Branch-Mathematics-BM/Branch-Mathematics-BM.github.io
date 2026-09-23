
const pages=[
 ["Home","index.html"],["BM","branch-mathematics.html"],["GURF","gurf.html"],["Steadman","steadman.html"],["Encyclopedia","encyclopedia.html"],["Theorems","theorems.html"],["Research","research.html"],["Calculator","calculator.html"],["Book","book.html"]
];
function mountChrome(){
 const cur=location.pathname.split('/').pop()||'index.html';
 const header=document.querySelector('[data-site-header]');
 if(header) header.innerHTML=`<header class="site-header"><div class="wrap nav"><a class="brand" href="index.html"><span class="brand-mark">BM</span><span>Branch Mathematics</span></a><button class="menu" aria-label="Toggle navigation" aria-expanded="false" aria-controls="primary-navigation">Menu</button><nav id="primary-navigation" class="navlinks">${pages.map(([n,u])=>`<a href="${u}" ${cur===u?'aria-current="page"':''}>${n}</a>`).join('')}</nav></div></header>`;
 const btn=document.querySelector('.menu'); if(btn) btn.onclick=()=>{const open=btn.closest('.nav').classList.toggle('open');btn.setAttribute('aria-expanded',String(open));};
 const footer=document.querySelector('[data-site-footer]');
 if(footer) footer.innerHTML=`<footer class="site-footer"><div class="wrap footer-grid"><div><strong>Branch Mathematics / GURF</strong><div class="small">Public technical reference · rebuilt 22 September 2026</div></div><div class="footer-links"><a href="definitions.html">Definitions</a><a href="equations.html">Equations</a><a href="structures.html">Structures</a><a href="passports.html">Passports</a><a href="roots.html">Roots</a><a href="status.html">Status</a><a href="changelog.html">Changelog</a></div></div></footer>`;
}
function mountRegistry(){
 const host=document.querySelector('[data-registry]'); if(!host||!window.BM_REGISTRIES)return;
 let all=[...BM_REGISTRIES.T,...BM_REGISTRIES.W,...BM_REGISTRIES.FI];
 const q=document.querySelector('[data-registry-search]');
 function draw(){const s=(q?.value||'').toLowerCase().trim(); const rows=all.filter(x=>!s||(`${x.id} ${x.title} ${x.kind}`).toLowerCase().includes(s));host.innerHTML=rows.map(x=>`<div class="registry-row" id="${x.id.toLowerCase()}"><div class="id">${x.id}</div><div>${x.title}</div><div class="kind">${x.kind}</div></div>`).join('')||'<p>No matching entries.</p>'}
 if(q) q.addEventListener('input',draw); draw();
}
document.addEventListener('DOMContentLoaded',()=>{mountChrome();mountRegistry();});
