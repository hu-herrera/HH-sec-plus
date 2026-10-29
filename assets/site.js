const toggle = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navegacion');
if (toggle && navigation) {
  const closeMenu = () => {
    toggle.setAttribute('aria-expanded', 'false');
    navigation.classList.remove('is-open');
  };
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded', String(open));
    navigation.classList.toggle('is-open', open);
  });
  navigation.addEventListener('click', event => {
    if (event.target.closest('a')) closeMenu();
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      closeMenu();
      toggle.focus();
    }
  });
  window.matchMedia('(min-width: 641px)').addEventListener('change', closeMenu);
}

const message = document.querySelector('#contacto-mensaje');
document.querySelectorAll('a[data-servicio]').forEach(link => {
  link.addEventListener('click', () => {
    if (message && !message.value.trim()) message.value = `Me interesa: ${link.dataset.servicio}.\n\n`;
  });
});
