const themeSwitchCheckbox = document.querySelector(".theme-switch__checkbox");

const savedTheme = localStorage.getItem('dark-mode');
if (savedTheme) {
    if (savedTheme === 'enabled') {
        document.body.classList.add("active");
        themeSwitchCheckbox.checked = true;
    }
} else {

    const userPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    if (userPrefersDark) {
        document.body.classList.add("active");
        themeSwitchCheckbox.checked = true;
    }
}

themeSwitchCheckbox.addEventListener("change", () => {
    if (themeSwitchCheckbox.checked) {
        document.body.classList.add("active");
        localStorage.setItem('dark-mode', 'enabled');
    } else {
        document.body.classList.remove("active");
        localStorage.setItem('dark-mode', 'disabled');
    }
});