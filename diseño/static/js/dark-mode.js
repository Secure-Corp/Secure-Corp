/*DARK MODE*/
const swith = document.querySelector(".theme-switch");

swith.addEventListener("click", e=>{
    swith.classList.toggle("active");
    document.body.classList.toggle("active");
})