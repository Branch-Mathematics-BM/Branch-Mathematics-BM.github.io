
function uniq(a){return [...new Set(a)]}
function analyseBM(){
 const p=document.getElementById('problem').value.trim();
 const tasks=document.getElementById('tasks').value.split(',').map(x=>x.trim()).filter(Boolean);
 const receiver=document.getElementById('receiver').value.trim()||'declared receiver';
 const scope=document.getElementById('scope').value;
 const l=p.toLowerCase();
 let branches=[];
 if(/∂|nabla|laplac|navier|pde|fluid|heat|wave|differential/.test(l)) branches.push('Continuum / PDE');
 if(/matrix|linear|eigen|kernel|operator|vector/.test(l)) branches.push('Linear / operator');
 if(/gauge|yang|wilson|su\(|field|connection|curvature/.test(l)) branches.push('Gauge / geometric');
 if(/quantum|hilbert|density|channel|observable/.test(l)) branches.push('Quantum');
 if(/markov|stochastic|probab|random/.test(l)) branches.push('Stochastic');
 if(/optimi|minimi|maximi|cost|efficien/.test(l)) branches.push('Optimization / cost');
 if(/control|feedback|receiver|response/.test(l)) branches.push('Response / control');
 if(!branches.length) branches=['Native problem branch','Task/receiver branch','Representation branch'];
 branches=uniq(branches);
 let ops=['declare domains and admissibility','identify task equivalence','test factorization through proposed representation'];
 if(scope==='dynamic') ops.push('test Dynamic Closure: ker R ⊆ ker(R∘f) and domain saturation');
 if(scope==='relational') ops.push('test equality of reduced successor-image sets');
 if(scope==='approx') ops.push('compute fibre/task diameter and decoder error bounds');
 const passport=[`Receiver: ${receiver}`,`Tasks: ${tasks.length?tasks.join('; '):'not specified — add explicit obligations'}`,'Required type/domain compatibility','Required law/regime context','Required future/continuation obligations if reused'];
 const leaves=branches.map((b,i)=>`L${i+1}: ${b} result with provenance + domain`).join('\n');
 const rootState=tasks.length?'Candidate Root only after every Passport obligation passes.':'Not Root-admissible: task obligations are underspecified.';
 const out=`BM ANALYSIS WORKSHEET\n\nProblem\n${p||'[enter an equation or system]'}\n\nSuggested Branches\n- ${branches.join('\n- ')}\n\nOperations / tests\n- ${ops.join('\n- ')}\n\nInteractions\n- Cross-Branch translations must declare true domains.\n- No structure is inherited merely because an input possessed it.\n- Joint realizability must be checked; separate feasibility is insufficient.\n\nLeaves\n${leaves}\n\nPassport\n- ${passport.join('\n- ')}\n\nTree / Response\nAssemble only mutually compatible Leaves into a lawful realization. Export a typed Response to ${receiver}.\n\nRoot status\n${rootState}\n\nImportant\nThis browser tool organizes a BM treatment. It does not prove the native mathematics or certify a theorem.`;
 document.getElementById('calc-output').textContent=out;
}
document.addEventListener('DOMContentLoaded',()=>document.getElementById('analyse')?.addEventListener('click',analyseBM));
