const navigationBar = document.getElementById("nav-bar");

function navigationBarTick() {
    navigationBar.style.display = window.scrollY ? "block" : "none";
}

function tick() {
    navigationBarTick();
}

(function () {
    setInterval(function () {
        tick();
    }, 1000 / 10);
})();