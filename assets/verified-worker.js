'use strict';
importScripts('bm-core.js?v=20261023','bm-verified.js?v=20261023');
self.onmessage=event=>{try{
 const {tool,input}=event.data;
 if(!['verifyQuantum','synthesizeCausal','decayBudget'].includes(tool))throw Error('Unknown calculation.');
 self.postMessage({ok:true,result:BMVerified[tool](input)});
}catch(error){self.postMessage({ok:false,error:error.message});}};
