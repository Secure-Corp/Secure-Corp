const inps = document.querySelectorAll('form .datosCand');
const cat = document.querySelectorAll('form .catalogo');
let env = document.getElementById('enviar');
env.addEventListener("click", enviar);
const evaluaciones = document.querySelectorAll('form .evaluacion');
document.formulario.addEventListener("input", validacion, false);



function validarInputs() {
    let valido = true;
    for (let x = 0; x < inps.length; x++) {
        if (inps[x].value.trim() == '' || !inps[x].validity.valid) {
            valido = false;
            inps[x].style.background='#FFDDDD';
            //break;
        } else {
            inps[x].style.background='#FFFFFF';
        }
    }
    return valido;
}


function validarCatalogos() {
    let valid = true;
    for (let y = 0; y < cat.length; y++) {
        if (cat[y].selectedIndex == 0 || !cat[y].validity.valid) {
            valid = false;
            cat[y].style.background='#FFDDDD';
            //break;
        } else {
            cat[y].style.background='#FFFFFF';
        }
    }
    return valid;
}


function validacion(e) {
    let elemento = e.target;
    if (elemento.validity.valid) {
        elemento.style.background='#FFFFFF';
    } else {
        elemento.style.background='#FFDDDD';
    }
}


function validarEvaluaciones() {
    let valido = true;
    for (let z = 0; z < evaluaciones.length; z++) {

        if (evaluaciones[z].selectedIndex == 0 || !evaluaciones[z].validity.valid) {
            valido = false;
            evaluaciones[z].style.background='#FFDDDD';
            z += 2;

        } else if (evaluaciones[z].selectedIndex == 2) {

            if (evaluaciones[z+1].selectedIndex == 0 || !evaluaciones[z+1].validity.valid) {
                valido = false;
                evaluaciones[z+1].style.background='#FFDDDD';
                z += 2;

            } else if (evaluaciones[z+1].selectedIndex == 2) {
                if (evaluaciones[z+2].value.trim() == '' || !evaluaciones[z+2].validity.valid) {
                    valido = false;
                    evaluaciones[z+2].style.background='#FFDDDD';
                    z += 2;
                    
                } else {
                    z += 2;
                }
                
            } else {
                z += 2;
            }
            
        } else {
            z += 2;
        }
        
    }
    return valido;
}


function enviar() {
    event.preventDefault();
    if (validarInputs() && validarCatalogos() && validarEvaluaciones()) {
        alert("Valores válidos.");
        document.formulario.submit();
    } else {
        alert("Debes llenar correctamente los campos.");
    }
}