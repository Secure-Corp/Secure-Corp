/*DARK MODE*/
const themeSwitchCheckbox = document.querySelector(".theme-switch__checkbox");

themeSwitchCheckbox.addEventListener("change", () => {
    document.body.classList.toggle("active", themeSwitchCheckbox.checked);
});
