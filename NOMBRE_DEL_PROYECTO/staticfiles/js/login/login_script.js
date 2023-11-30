// Contenido de tu archivo JS
$(document).ready(function () {
  $("#toggleDarkMode").click(function () {
    $("body").toggleClass("dark-mode");
    $("body").toggleClass("bg-light");
    $(".login-container").toggleClass("dark-mode-login");
  });
});
