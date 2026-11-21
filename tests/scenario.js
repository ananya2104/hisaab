(async () => {
  const out = []; const log = (...a) => out.push(a.map(x => typeof x === 'string' ? x : JSON.stringify(x)).join(' '));
  try {
    await new Promise(r => setTimeout(r, 400));
    log('AI mode', AI.mode, 'store', Store.mode);
    await runImport('csv', SAMPLE_CSV, 'demo csv');
    await runImport('sms', SAMPLE_SMS, 'demo sms');
    const M = model();
    log('txns', S.txns.length, 'months', M.months, 'full', M.full, 'asOf', M.asOf);
    log('income', Math.round(M.income), 'spend', Math.round(M.spend), 'surplus', Math.round(M.surplus), 'free', Math.round(M.free), 'rate', M.rate.toFixed(1));
    log('cats', Object.fromEntries(Object.entries(M.spendByCat).map(([k,v])=>[k,Math.round(v)])));
    log('recurring', M.recurring.map(r => r.merchant + ':' + r.kind + ':' + Math.round(r.monthly) + ':' + r.alerts.map(a=>a.type).join('+')));
    log('nudges', M.nudges.map(n => n.level + ' ' + n.text));
    log('goals', M.goals.map(g => g.name + ' req ' + Math.round(g.required) + ' alloc ' + Math.round(g.alloc) + ' eta ' + g.eta + ' ' + g.onTrack));
    log('review needed', S.txns.filter(t => t.needsReview).map(t => t.merchant));
    log('cat sources', S.txns.reduce((a, t) => (a[t.catSource] = (a[t.catSource] || 0) + 1, a), {}));
    log('uncategorised Other', S.txns.filter(t => t.category === 'Other').map(t => t.merchant + '|' + t.source));
    log('sms parsed', S.txns.filter(t => t.source.startsWith('sms')).length);
    log('budgets', S.profile.budgets);
    const sim = simulate([{ kind: 'cut_category_pct', category: 'Food delivery', pct: 30 }, { kind: 'cancel_subscription', merchant: 'CULTFIT' }, { kind: 'change_rent', amount: 3000 }]);
    log('sim', sim.applied, Math.round(sim.deltaMonthly), sim.goals.map(g => g.name + ' ' + g.baseEta + '→' + g.newEta));
    const lr = learnRule('ANKIT SHARMA', 'Dining out', 'user'); log('learn', lr);
    for (const t of ['home','import','txns','subs','plan','whatif','review','coach']) { RT.tab = t; render(); log('tab', t, 'ok', $('#main').innerText.length); }
    await askCoach('Which stock should I buy with my surplus?'); log('guard', S.chat[S.chat.length-1].guard === true);
    await askCoach('What if I cut dining out by 30%?'); log('coach reply', S.chat[S.chat.length-1].content); log('blocked question kept out of history', !JSON.stringify(window.__lastInput).includes('Which stock'));
    await generateReview('2026-10'); const rv = S.reviews['2026-10']; log('review checks', rv.checks.map(c=>c.raw+':'+c.ok));
    const f = reviewFacts('2026-10'); log('facts', f.income, f.spend, f.saved, f.savingsRatePct);
    log('trace entries', RT.trace.length, RT.trace.slice(0, 12).map(e => e.kind + ':' + e.text.slice(0, 80)));
    const ff = futureFacts(); log('future gap', ff.gapBuiltUp, 'foodgap', ff.gapFoodDelivery, 'drift', ff._d.builtUp, ff._d.notes, ff._d.goals.map(g=>g.name+':'+g.reached), 'plan', ff._p.builtUp, ff._p.notes, ff._p.goals.map(g=>g.name+':'+g.reached));
    await writeLetters(); log('letters', S.future && S.future.checks.drift.map(c=>c.raw+':'+c.ok), S.future && S.future.checks.plan.map(c=>c.raw+':'+c.ok));
    RT.futureSelf='plan'; await askFuture('Did we make the Goa trip?'); log('future chat', S.futureChat.map(m=>m.role+':'+m.content));
    await askFuture('Which stock should I buy?'); log('future guard', S.futureChat[S.futureChat.length-1].guard);
    RT.tab='future'; render(); log('tab future', $('#main').innerText.length);
    await new Promise(r => setTimeout(r, 1200)); log('db saved', Object.keys(__docs), (Object.values(__docs)[0]||{}).state ? 'yes' : 'no');
  } catch (e) { log('TEST EXCEPTION', e.stack || e.message); }
  log('ERRORS', window.__errs);
  const pre = document.createElement('pre'); pre.id = 'TESTOUT'; pre.textContent = out.join('\n'); document.body.appendChild(pre);
})();
