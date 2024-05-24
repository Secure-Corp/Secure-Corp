let ubicacionPrincipal = document.documentElement.scrollHeight - window.pageYOffset;
let $nav = document.querySelector("nav");


window.addEventListener("scroll", function () {

    let desplazamientoActual = window.pageYOffset;

    if (ubicacionPrincipal >= desplazamientoActual) {

        $nav.style.top = "0px";

    } else {

        $nav.style.top = "-100px";
    }


    ubicacionPrincipal = desplazamientoActual;
});

