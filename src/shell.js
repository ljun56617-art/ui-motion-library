// Shared page shell: renders specimen captions, copy buttons, pause control and demo helpers.
(function () {
  const isFrozen = (stage) =>
    document.body.classList.contains('paused') || stage.closest('.sp').classList.contains('off');

  const U = {
    // Repeats while the specimen is on screen and motion is not paused.
    loop(stage, fn, ms) { setInterval(() => { if (!isFrozen(stage)) fn(); }, ms); },
    // Same as loop, but stops for good once the viewer has interacted with this stage.
    auto(stage, fn, ms) { U.loop(stage, () => { if (!stage.dataset.touched) fn(); }, ms); },
    frame(stage, fn) {
      const step = (t) => { if (!isFrozen(stage)) fn(t); requestAnimationFrame(step); };
      requestAnimationFrame(step);
    },
    tween(ms, fn, done) {
      const start = performance.now();
      const step = (now) => {
        const p = Math.min(1, (now - start) / ms);
        fn(p);
        if (p < 1) requestAnimationFrame(step); else if (done) done();
      };
      requestAnimationFrame(step);
    },
    easeOut: (p) => 1 - Math.pow(1 - p, 3),
  };

  const cards = [...document.querySelectorAll('.sp')];
  const toc = document.querySelector('.toc');

  function addText(parent, tag, cls, text) {
    const el = document.createElement(tag);
    if (cls) el.className = cls;
    el.textContent = text;
    parent.appendChild(el);
    return el;
  }

  async function copyPrompt(btn, promptEl) {
    try {
      await navigator.clipboard.writeText(promptEl.textContent);
      btn.textContent = '已复制';
    } catch (err) {
      // Clipboard refused (some embedded views): select the text so the viewer can copy it by hand.
      const range = document.createRange();
      range.selectNodeContents(promptEl);
      const sel = getSelection();
      sel.removeAllRanges();
      sel.addRange(range);
      btn.textContent = '已选中';
    }
    setTimeout(() => { btn.textContent = '复制'; }, 1600);
  }

  cards.forEach((card, i) => {
    const d = card.dataset;
    card.id = 's' + (i + 1);
    const no = String(i + 1).padStart(2, '0');
    const meta = addText(card, 'div', 'meta', '');
    const head = addText(meta, 'div', 'meta-h', '');
    addText(head, 'span', 'no', no);
    addText(head, 'h3', '', d.name);
    addText(head, 'span', 'en', d.en);
    addText(meta, 'p', 'use', d.use);
    if (d.params) addText(meta, 'div', 'params', d.params);
    const pr = addText(meta, 'div', 'pr', '');
    addText(pr, 'b', '', '一句话让 AI 做');
    const promptEl = addText(pr, 'p', '', d.prompt);
    const btn = addText(pr, 'button', '', '复制');
    btn.type = 'button';
    btn.setAttribute('aria-label', '复制「' + d.name + '」的提示词');
    btn.addEventListener('click', () => copyPrompt(btn, promptEl));
    const stage = card.querySelector('.stage');
    if (d.hint) addText(stage, 'span', 'hint', d.hint);
    if (toc) { const a = addText(toc, 'a', '', d.name); a.href = '#' + card.id; }
  });

  // Delegated open / close for popup-style demos.
  document.addEventListener('click', (e) => {
    const t = e.target.closest('[data-toggle],[data-open],[data-close]');
    if (!t) return;
    const stage = t.closest('.stage');
    if (t.hasAttribute('data-toggle')) stage.classList.toggle('on');
    else if (t.hasAttribute('data-open')) stage.classList.add('on');
    else stage.classList.remove('on');
  });
  // Esc closes the popup in the stage used last, even if a click left focus on the page body.
  let lastStage = null;
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && lastStage) lastStage.classList.remove('on');
  });
  const markTouched = (e) => {
    const stage = e.target.closest && e.target.closest('.stage');
    if (stage) { stage.dataset.touched = '1'; lastStage = stage; }
  };
  document.addEventListener('pointerdown', markTouched, true);
  document.addEventListener('focusin', markTouched, true);

  // On phones the tab row scrolls sideways: keep the current page's tab in view.
  const tabs = document.querySelector('.tabs');
  const currentTab = tabs.querySelector('[aria-current]');
  if (currentTab) tabs.scrollLeft = currentTab.offsetLeft - tabs.offsetLeft - 12;

  // Pause control; viewers who asked for reduced motion start paused.
  const pause = document.getElementById('pauseAll');
  function setPaused(v) {
    document.body.classList.toggle('paused', v);
    pause.textContent = v ? '继续动效' : '暂停动效';
    pause.setAttribute('aria-pressed', String(v));
  }
  pause.addEventListener('click', () => setPaused(!document.body.classList.contains('paused')));
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) setPaused(true);

  // Run page demos, then watch visibility: pause off-screen specimens, auto-open on first view.
  cards.forEach((card) => {
    const stage = card.querySelector('.stage');
    const fn = window.demo[card.dataset.demo];
    if (card.dataset.demo && !fn) console.error('missing demo: ' + card.dataset.demo);
    if (fn) fn(stage, U);
  });
  const seen = new WeakSet();
  const io = new IntersectionObserver((entries) => {
    entries.forEach((en) => {
      en.target.classList.toggle('off', !en.isIntersecting);
      if (!en.isIntersecting || seen.has(en.target)) return;
      seen.add(en.target);
      const stage = en.target.querySelector('.stage');
      setTimeout(() => {
        if (stage.dataset.touched) return;
        if (en.target.hasAttribute('data-auto')) stage.classList.add('on');
        stage.dispatchEvent(new Event('inview'));
      }, 450);
    });
  }, { threshold: 0.15 });
  cards.forEach((c) => io.observe(c));
})();
