
window.addEventListener('scroll',function () {
    let navbar = document.getElementById('navbar-h-detect')
    navbar.classList.toggle("sticky",window.scrollY > 0)
    console.log("scroll")
})