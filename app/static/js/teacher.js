document.addEventListener("DOMContentLoaded", function() {
    const menuToggle = document.getElementById("menu-toggle");
    const wrapper = document.getElementById("wrapper");
    const sidebarLinks = document.querySelectorAll("#sidebar-wrapper .list-group-item");

    menuToggle.addEventListener("click", function() {
        wrapper.classList.toggle("toggled");
    });

    // Mobile এ click করলে auto close
    sidebarLinks.forEach(link => {
        link.addEventListener("click", function() {
            if (window.innerWidth < 768) {
                wrapper.classList.remove("toggled");
            }
        });
    });
});