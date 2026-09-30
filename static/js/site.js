const header = document.querySelector('.site-header');
const toggle = document.querySelector('.menu-toggle');
toggle?.addEventListener('click', () => {
  const open = header.classList.toggle('open');
  toggle.setAttribute('aria-expanded', open);
});
document.querySelectorAll('nav a').forEach(link => link.addEventListener('click', () => header.classList.remove('open')));
