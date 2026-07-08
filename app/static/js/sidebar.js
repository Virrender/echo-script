const sidebar = document.getElementById("sidebar");

document.getElementById("open-sidebar").addEventListener("click", () => {
    sidebar.classList.remove("-translate-x-full");
});

document.getElementById("close-sidebar").addEventListener("click", () => {
    sidebar.classList.add("-translate-x-full");
});