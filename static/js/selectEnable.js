document.addEventListener('DOMContentLoaded', function() {
  // Lista de IDs de los selects que requieren mostrarPres
  const presSelects = [
      {reqId: 'entrevistaReq', presId: 'campoEntrevistaReq', resId: 'campoEntrevistaRes'},
      {reqId: 'evalMedicaReq', presId: 'campoEvalMedicaReq', resId: 'campoEvalMedicaRes'},
      {reqId: 'evalPsicoloReq', presId: 'campoEvalPsicoloReq', resId: 'campoEvalPsicoloRes'},
      {reqId: 'evalPsicomReq', presId: 'campoEvalPsicomReq', resId: 'campoEvalPsicomRes'},
      {reqId: 'evalTecniReq', presId: 'campoEvalTecniReq', resId: 'campoEvalTecniRes'},
      {reqId: 'evalConoReq', presId: 'campoEvalConoReq', resId: 'campoEvalConoRes'},
      {reqId: 'entrevistaFinReq', presId: 'campoEntrevistaFinReq', resId: 'campoEntrevistaFinRes'}
  ];

  // Lista de IDs de los selects que requieren mostrarRes
  const resSelects = [
      {presId: 'entrevistaPres', campoId: 'campoEntrevistaRes'},
      {presId: 'evalMedicaPres', campoId: 'campoEvalMedicaRes'},
      {presId: 'evalPsicoloPres', campoId: 'campoEvalPsicoloRes'},
      {presId: 'evalPsicomPres', campoId: 'campoEvalPsicomRes'},
      {presId: 'evalTecniPres', campoId: 'campoEvalTecniRes'},
      {presId: 'evalConoPres', campoId: 'campoEvalConoRes'},
      {presId: 'entrevistaFinPres', campoId: 'campoEntrevistaFinRes'}
  ];

  // Ejecuta mostrarPres para cada select en presSelects
  presSelects.forEach(function(select) {
      mostrarPres(select.reqId, select.presId, select.resId);
  });

  // Ejecuta mostrarRes para cada select en resSelects
  resSelects.forEach(function(select) {
      mostrarRes(select.presId, select.campoId);
  });
});

function mostrarPres(reqId, presId, resId) {
   var seleccion = document.getElementById(reqId).value;
   var campoPres = document.getElementById(presId);
   var present = campoPres.querySelector('select');
   var campoRes = document.getElementById(resId);
   var resultado = campoRes.querySelector('input');
 
   console.log(`mostrarPres called with reqId=${reqId}, presId=${presId}, resId=${resId}, seleccion=${seleccion}`);
 
   if (seleccion === "1") {
     campoPres.style.display = "block";
     campoRes.style.display = "block";
   } else {
     campoPres.style.display = "none";
     present.children[1].selected = true;
     campoRes.style.display = "none";
     if (resultado) {
       resultado.value = 'NO APLICA/NO PRESENTADA';
       resultado.disabled = true; 
     }
   }
 }
 
 function mostrarRes(presId, campoId) {
   var seleccion = document.getElementById(presId).value;
   var campo = document.getElementById(campoId).querySelector('input'); 
 
   console.log(`mostrarRes called with presId=${presId}, campoId=${campoId}, seleccion=${seleccion}`);
 
   if (seleccion === "1") {
     if (campo) {
       campo.disabled = false;
       campo.required =true;
     }
   } else {
     if (campo) {
       campo.value = 'NO APLICA/NO PRESENTADA';
       campo.disabled = true;
       campo.required = false;
     }
   }
 }
 
