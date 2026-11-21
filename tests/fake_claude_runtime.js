window.__errs = [];
window.addEventListener('error', e => window.__errs.push('ERR: ' + e.message + ' @' + e.lineno));
window.addEventListener('unhandledrejection', e => window.__errs.push('REJ: ' + (e.reason && (e.reason.stack || e.reason.message) || e.reason)));
// fake claude runtime: db + user + sample (with tool use)
const __docs = {};
window.claude = { use: async name => {
  await new Promise(r => setTimeout(r, 50));
  if (name === 'db') return { collection: p => ({ doc: k => ({ get: async () => __docs[p + '/' + k] || null, set: async v => { __docs[p + '/' + k] = v; } }) }) };
  if (name === 'user') return { id: async () => 'u123' };
  if (name === 'tts') return { speak: async () => {}, stop: () => {}, onState: () => {} };
  if (name === 'dictation') return { start: async () => {}, stop: async () => {}, onFinal: () => {}, onState: () => {}, onPartial: () => {} };
  if (name === 'sample') {
    const f = async (input, opts = {}) => {
      if (opts.tools) {
        const T = n => opts.tools.find(t => t.name === n);
        if (T('get_future_projection')) { const fp = await T('get_future_projection').execute({ self: 'plan' }); const txt = `I built ₹${fp.builtUpBy2031NoReturns.toLocaleString('en-IN')} by ${fp.month}.`; opts.onText && opts.onText({ text: txt }); return { text: txt }; }
        const ov = await T('get_overview').execute({});
        const sim = await T('simulate_what_if').execute({ changes: [{ kind: 'cut_category_pct', category: 'Dining out', pct: 30 }, { kind: 'cut_category_pct', category: 'Food delivery', pct: 30 }] });
        const nd = await T('create_nudge').execute({ text: 'Food delivery is running hot this month.', level: 'warn' });
        const rec = await T('list_recurring').execute({});
        const txt = `Income ₹${ov.income}. Cutting saves ₹${sim.extraPerYear}/yr. Recurring: ${rec.length}.`;
        opts.onText && opts.onText({ text: txt });
        return { text: txt };
      }
      return { text: 'Headline: you saved ₹99,999 this month (12%).' };
    };
    f.json = async (prompt) => {
      if (prompt.includes('ITEMS:')) { const items = JSON.parse(prompt.split('ITEMS:')[1]); return items.map(it => ({ id: it.id, category: /RAMESH/.test(it.payee) ? 'Rent' : /ANKIT/.test(it.payee) ? 'Transfers' : /MEGHANA/.test(it.payee) ? 'Dining out' : /GOPAL/.test(it.payee) ? 'Groceries' : /URBAN/.test(it.payee) ? 'Home & services' : 'Other', confidence: /RAMESH/.test(it.payee) ? 0.7 : 0.9, reason: 'test' })); }
      if (prompt.includes('two short letters')) { const f = JSON.parse(prompt.split('FACTS: ')[1]); return { drift: `Hi, it's me in ${f.month}. I built ₹${f.drift.builtUpBy2031NoReturns.toLocaleString('en-IN')}, and spent ₹${f.drift.fiveYearTotals.foodDelivery.toLocaleString('en-IN')} on food delivery. Also ₹12,34,567 made up.`, plan: `I built ₹${f.plan.builtUpBy2031NoReturns.toLocaleString('en-IN')}, assuming no investment returns. That is ₹${f.gapBuiltUp.toLocaleString('en-IN')} more.` }; }
      if (prompt.includes('LINES:')) return [{ line: 0, date: '2026-11-14', amount: 1250, direction: 'debit', payee: 'SRI LAKSHMI TIFFINS' }];
      return {};
    };
    return f;
  }
  return null;
} };
