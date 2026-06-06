// main.js — Permuta de Libros

// Auto-cerrar mensajes de Django después de 5 segundos
document.addEventListener('DOMContentLoaded', function () {
  const alerts = document.querySelectorAll('.alert');
  alerts.forEach(function (alert) {
    setTimeout(function () {
      alert.style.transition = 'opacity 0.6s';
      alert.style.opacity = '0';
      setTimeout(function () { alert.remove(); }, 600);
    }, 5000);
  });
});
