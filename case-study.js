(() => {
  'use strict';
  const input = document.getElementById('import-hours');
  if (!input) return;
  const $ = id => document.getElementById(id);
  const initialWorking = [{driver: 'DEMO-004', hours: 24}, {driver: 'DEMO-005', hours: 30}];
  const newStaging = () => [{driver: 'DEMO-001', hours: 32}, {driver: 'DEMO-002', hours: null}, {driver: 'DEMO-003', hours: 28}];
  let working = initialWorking.map(row => ({...row}));
  let staged = newStaging();
  let committed = false;
  function render() {
    if (committed) return;
    const raw = input.value.trim();
    const hours = input.valueAsNumber;
    const valid = raw !== '' && Number.isFinite(hours) && hours >= 0 && hours <= 168 && input.validity.valid;
    input.setAttribute('aria-invalid', String(!valid));
    $('import-issues').textContent = valid ? '0' : '1';
    if (!valid) {
      $('import-row-error').textContent = raw === '' ? 'Hours are required.' : 'Enter 0–168 hours in quarter-hour increments.';
      $('import-result-title').textContent = 'Staged — correction needed';
      $('import-result-text').textContent = 'Three rows are staged. One row needs correction. The two existing working records remain unchanged.';
      return;
    }
    // This is a standalone, in-memory illustration; no operational records exist here.
    staged[1].hours = hours;
    working.push(...staged);
    staged = [];
    committed = true;
    input.disabled = true;
    $('import-row-error').textContent = 'Valid — revalidated and committed';
    $('import-working').textContent = String(working.length);
    $('import-staged').textContent = String(staged.length);
    $('import-result-title').textContent = 'Revalidated → automatically committed';
    $('import-result-text').textContent = `All three fictional rows passed this example’s checks. DEMO-002 has ${hours} paid hours. The three staged rows were added once to the two existing demonstration records, giving five working records. Nothing was saved outside this page.`;
    $('import-result-title').closest('.import-result').classList.add('is-complete');
  }
  input.addEventListener('change', render);
  $('import-reset').addEventListener('click', () => {
    committed = false;
    working = initialWorking.map(row => ({...row}));
    staged = newStaging();
    input.disabled = false;
    input.value = '';
    $('import-staged').textContent = '3';
    $('import-working').textContent = '2';
    $('import-result-title').closest('.import-result').classList.remove('is-complete');
    render();
    input.focus();
  });
})();
