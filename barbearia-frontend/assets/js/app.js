// Corte&Cia — comportamentos de interface compartilhados
document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.querySelector('[data-menu-toggle]');
  var scrim = document.querySelector('[data-nav-scrim]');

  function closeNav() { document.body.classList.remove('nav-open'); }
  function openNav() { document.body.classList.add('nav-open'); }

  if (toggle) {
    toggle.addEventListener('click', function () {
      document.body.classList.toggle('nav-open');
    });
  }
  if (scrim) {
    scrim.addEventListener('click', closeNav);
  }

  // Fecha o menu ao navegar em telas pequenas
  document.querySelectorAll('.nav-item').forEach(function (link) {
    link.addEventListener('click', function () {
      if (window.innerWidth <= 860) closeNav();
    });
  });

  // Tabs de perfil na tela de login (apenas visual)
  document.querySelectorAll('.role-tabs').forEach(function (group) {
    group.querySelectorAll('button').forEach(function (btn) {
      btn.addEventListener('click', function () {
        group.querySelectorAll('button').forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');
      });
    });
  });

  // Feedback simples ao "enviar" formulários estáticos deste protótipo
  document.querySelectorAll('form[data-demo-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = form.querySelector('button[type="submit"]');
      if (!btn) return;
      var original = btn.textContent;
      btn.textContent = 'Salvo ✓';
      setTimeout(function () { btn.textContent = original; }, 1600);
    });
  });
});
