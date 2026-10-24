(() => {
  const button = document.getElementById('themeToggle');
  try { document.body.classList.toggle('dark', localStorage.getItem('portfolioTheme') === 'dark'); } catch (_) {}
  button.addEventListener('click', () => {
    const dark = document.body.classList.toggle('dark');
    try { localStorage.setItem('portfolioTheme', dark ? 'dark' : 'light'); } catch (_) {}
    button.setAttribute('aria-label', dark ? 'Switch to light theme' : 'Switch to dark theme');
  });
})();
