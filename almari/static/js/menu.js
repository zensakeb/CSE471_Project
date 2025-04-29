document.addEventListener("DOMContentLoaded", function(){
    const btn = document.getElementById("menu-button"),
          menu = document.getElementById("submenu");
    btn.addEventListener("click", e => {
      e.stopPropagation();
      menu.classList.toggle("show");
    });
    document.addEventListener("click", () => menu.classList.remove("show"));
  });
  