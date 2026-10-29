// Session harness: attach to the capture Chrome (started by capture/chrome.sh) over CDP and record one run
// under <platform>/raw/runs/<run-id>/ (PLATFORM=<platform folder>, e.g. zid):
//   trace.zip        Playwright trace: DOM snapshots (incl. shadow DOM), network with request and response bodies,
//                    console
//   actions.jsonl    one row per step: intent, start/end time, url, title, outcome, error
//   steps/NNN.aria.yaml, NNN.text.txt, NNN.html, NNN.png   accessibility snapshot, visible text, rendered HTML and
//                    screenshot after each step (child frames: steps/NNN.frame-K.*)
//   run.json         run metadata: platform, label, tool versions, time range, network path
// Nothing is intercepted or stopped: every request the pages make goes through and is held in the trace.
import { chromium } from 'playwright-core';
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import crypto from 'node:crypto';

const require = createRequire(import.meta.url);
const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const CDP = process.env.CDP_URL || 'http://127.0.0.1:9230';
// Hosts of each platform that answer Cloudflare's /cdn-cgi/trace: where the platform sees this browser from.
const PROBE = {
  zid: ['dashboard.zid.sa', 'hermod.zid.sa', 'zid.sa'],
  bigcommerce: ['www.bigcommerce.com', 'support.bigcommerce.com'],
};
// Platforms whose hosts answer no /cdn-cgi/trace: an address of the platform that states where it places this browser.
const GEO = {
  woocommerce: ['https://public-api.wordpress.com/geo/'],
};

// steps/NNN.text.txt: the text a sighted reader sees, in document order. Walks the composed tree (shadow
// roots, and the nodes slotted into them), skips elements CSS hides, breaks lines around block boxes, and
// keeps aria-hidden text (it is on screen). Form fields show their value (the placeholder when empty); a password
// field shows the dots the screen shows, one per character (its value is in the accessibility snapshot).
const VISIBLE_TEXT = () => {
  const out = [];
  const nl = () => { if (out.length && out[out.length - 1] !== '\n') out.push('\n'); };
  const BLOCK = /^(block|flex|grid|list-item|table|table-row|table-caption|flow-root|inline-block|inline-flex|inline-grid)$/;
  const walk = (n) => {
    if (n.nodeType === 3) { const t = n.nodeValue.replace(/\s+/g, ' '); if (t.trim()) out.push(t); return; }
    if (n.nodeType === 11) { for (const c of n.childNodes) walk(c); return; }
    if (n.nodeType !== 1) return;
    const tag = n.localName;
    if (tag === 'script' || tag === 'style' || tag === 'noscript' || tag === 'template') return;
    if (tag === 'slot') { const a = n.assignedNodes({ flatten: true }); for (const c of (a.length ? a : n.childNodes)) walk(c); return; }
    const display = getComputedStyle(n).display;
    // display: contents boxes have no box of their own: walk through them.
    if (display !== 'contents' && n.checkVisibility && !n.checkVisibility({ visibilityProperty: true })) return;
    const block = tag === 'br' || BLOCK.test(display);
    if (block) nl();
    if (tag === 'input' || tag === 'textarea' || tag === 'select') {
      const type = (n.getAttribute('type') || '').toLowerCase();
      if (type === 'hidden') return;
      if (type === 'password') { if (n.value) out.push(` [${'•'.repeat(n.value.length)}] `); else if (n.placeholder) out.push(` [${n.placeholder}] `); }
      else if (tag === 'select') { const o = n.selectedOptions && n.selectedOptions[0]; if (o) out.push(` [${o.textContent.trim()}] `); }
      else if (type === 'checkbox' || type === 'radio') out.push(n.checked ? ' [x] ' : ' [ ] ');
      else if (n.value) out.push(` [${n.value}] `);
      else if (n.placeholder) out.push(` [${n.placeholder}] `);
      if (block) nl();
      return;
    }
    for (const c of (n.shadowRoot ? n.shadowRoot.childNodes : n.childNodes)) walk(c);
    if (block) nl();
  };
  walk(document.body);
  return out.join('').replace(/[ \t]+/g, ' ').replace(/ ?\n ?/g, '\n').replace(/\n{2,}/g, '\n').trim() + '\n';
};

export async function openRun({ label, script = null, extra = null, viewport = { width: 1440, height: 900 } }) {
  const platform = process.env.PLATFORM;
  if (!platform || !fs.existsSync(path.join(ROOT, platform))) throw new Error('PLATFORM must name a platform folder of this repository (e.g. zid)');
  const runId = new Date().toISOString().replace(/[-:]/g, '').replace(/\.\d+Z$/, 'Z') + '-' + label;
  const dir = path.join(ROOT, platform, 'raw', 'runs', runId);
  fs.mkdirSync(path.join(dir, 'steps'), { recursive: true });

  const browser = await chromium.connectOverCDP(CDP);
  // RUN_CONTEXT=fresh: a new browser context without the profile's cookies or storage (a first visit, as
  // a visitor with no remembered choices); default: the capture profile.
  const freshContext = process.env.RUN_CONTEXT === 'fresh';
  const context = freshContext ? await browser.newContext() : browser.contexts()[0];
  // The network path this browser uses, as the platform's Cloudflare edge sees it, or as the platform's geo address answers.
  let network = null;
  try {
    const probe = await context.newPage();
    network = { via: GEO[platform] ? `browser ${GEO[platform].join(' ')}` : 'browser <host>/cdn-cgi/trace', hosts: {} };
    for (const h of PROBE[platform] || []) {
      try {
        const r = await probe.goto(`https://${h}/cdn-cgi/trace`, { timeout: 20000 });
        const kv = r && r.ok() ? Object.fromEntries((await probe.evaluate(() => document.body.innerText)).split('\n').map((l) => l.split('='))) : {};
        network.hosts[h] = kv.loc ? { ip: kv.ip || '', loc: kv.loc, colo: kv.colo, http: kv.http } : { status: r ? r.status() : null };
      } catch (e) { network.hosts[h] = { error: String(e.message || e).split('\n')[0].slice(0, 120) }; }
    }
    for (const u of GEO[platform] || []) {
      try {
        const r = await probe.goto(u, { timeout: 20000 });
        const g = r && r.ok() ? JSON.parse(await probe.evaluate(() => document.body.innerText)) : null;
        network.hosts[new URL(u).host] = g ? { loc: g.country_short, answer: g } : { status: r ? r.status() : null };
      } catch (e) { network.hosts[new URL(u).host] = { error: String(e.message || e).split('\n')[0].slice(0, 120) }; }
    }
    const first = Object.values(network.hosts).find((x) => x.loc) || {};
    Object.assign(network, { ip: first.ip, loc: first.loc, colo: first.colo, http: first.http });
    await probe.close();
  } catch {}
  // RUN_ADOPT_PAGE=<address prefix>: the run takes over the open tab whose address starts with it (a page a person
  // left in a state a new tab would not reach, such as a ticked CAPTCHA) and leaves that tab open at the end.
  const adoptPrefix = process.env.RUN_ADOPT_PAGE || null;
  let page = adoptPrefix ? context.pages().find((p) => p.url().startsWith(adoptPrefix)) || null : null;
  if (adoptPrefix && !page) throw new Error(`no open tab starts with ${adoptPrefix}`);
  const adopted = !!page;
  if (!page) page = await context.newPage();
  await page.setViewportSize(viewport);
  let cdp = await context.newCDPSession(page);

  const actions = fs.createWriteStream(path.join(dir, 'actions.jsonl'));
  let stepNo = 0;

  await context.tracing.start({ screenshots: false, snapshots: true, sources: false, title: runId });
  const started = new Date().toISOString();

  async function step(intent, fn, { settleMs = 1500, fullPage = true, readyTimeout = 120000, target = null } = {}) {
    stepNo += 1;
    const id = String(stepNo).padStart(3, '0');
    const t_start = new Date().toISOString();
    let outcome = 'ok', error = null, response = null;
    // A tab grows over a long run: collect garbage every 25 steps.
    if (stepNo % 25 === 0) await cdp.send('HeapProfiler.collectGarbage').catch(() => {});
    // A page that was closed, or whose main frame was detached, is replaced by a new page; the row records it.
    let page_replaced = null;
    if (page.isClosed() || page.mainFrame().isDetached()) {
      page_replaced = page.isClosed() ? 'page closed' : 'main frame detached';
      await page.close().catch(() => {});
      page = await context.newPage();
      await page.setViewportSize(viewport);
      cdp = await context.newCDPSession(page);
    }
    try { response = await fn(page); } catch (e) { outcome = 'failed'; error = String(e.message || e).split('\n')[0].slice(0, 300); }
    // Ready = a main landmark or a dialog has rendered content, bounded by readyTimeout.
    const t_ready0 = Date.now();
    const ready = await page.waitForFunction(() => { return [...document.querySelectorAll('main, [role=main], [role=dialog]')].some((m) => m.innerText && m.innerText.trim().length > 0); }, null, { timeout: readyTimeout }).then(() => true).catch(() => false);
    const ready_s = (Date.now() - t_ready0) / 1000;
    await page.waitForLoadState('networkidle', { timeout: 10000 }).catch(() => {});
    await new Promise((r) => setTimeout(r, settleMs));
    let aria;
    try { aria = await page.locator('body').ariaSnapshot({ timeout: 15000 }); } catch (e) { aria = `# aria snapshot failed: ${e.message}`; }
    fs.writeFileSync(path.join(dir, 'steps', `${id}.aria.yaml`), aria);
    // What the page visibly states: the accessibility tree leaves out text marked aria-hidden.
    try { fs.writeFileSync(path.join(dir, 'steps', `${id}.text.txt`), await page.evaluate(VISIBLE_TEXT)); } catch (e) { fs.writeFileSync(path.join(dir, 'steps', `${id}.text.txt`), `# visible text failed: ${e.message}\n`); }
    // Child frames: each frame's HTML, accessibility tree and visible text. The frames shown on the page are waited
    // for together; a frame whose element has no size (a hidden utility frame, such as Zid's changelog.zid.sa/utilities
    // and HubSpot's feedback-web-fetcher, which never show text) is not waited for.
    const frames = [];
    const kids = [...page.frames().filter((f) => f !== page.mainFrame()).entries()].filter(([, fr]) => fr.url() && fr.url() !== 'about:blank');
    const tf = Date.now();
    const waits = await Promise.all(kids.map(async ([, fr]) => {
      const box = await fr.frameElement().then((el) => el.boundingBox()).catch(() => null);
      if (!box || !box.width || !box.height) return [false, null, false];
      return fr.waitForFunction(() => !!(document.body && document.body.innerText && document.body.innerText.trim().length > 0), null, { timeout: 20000 })
        .then(() => [true, (Date.now() - tf) / 1000, true]).catch(() => [false, (Date.now() - tf) / 1000, true]);
    }));
    for (const [i, [k, fr]] of kids.entries()) {
      const furl = fr.url();
      const rec = { index: k, url: furl.split('?')[0], name: fr.name() || null };
      [rec.ready, rec.ready_s, rec.shown] = waits[i];
      try { fs.writeFileSync(path.join(dir, 'steps', `${id}.frame-${k}.aria.yaml`), await fr.locator('body').ariaSnapshot({ timeout: 8000 })); rec.aria = true; } catch { rec.aria = false; }
      try { fs.writeFileSync(path.join(dir, 'steps', `${id}.frame-${k}.text.txt`), await fr.evaluate(VISIBLE_TEXT)); rec.text = true; } catch { rec.text = false; }
      try { const fh = await fr.content(); fs.writeFileSync(path.join(dir, 'steps', `${id}.frame-${k}.html`), fh); rec.html_bytes = Buffer.byteLength(fh); } catch { rec.html_bytes = null; }
      frames.push(rec);
    }
    // Rendered HTML of the main frame (no shadow roots, no iframes; the trace has those).
    let html_bytes = null;
    try { const html = await page.content(); fs.writeFileSync(path.join(dir, 'steps', `${id}.html`), html); html_bytes = Buffer.byteLength(html); } catch {}
    // A page that scrolls inside an inner container gives only the viewport to a full-page screenshot: grow the
    // viewport to the tallest scroll container, take the shot, restore.
    let shot = true, shot_px = null, shot_container = null, shot_error = null;
    try {
      let target = viewport.height;
      if (fullPage) {
        const tall = await page.evaluate(() => {
          let max = document.documentElement.scrollHeight, who = 'document';
          for (const el of document.querySelectorAll('*')) {
            const cs = getComputedStyle(el);
            if (/(auto|scroll)/.test(cs.overflowY) && el.scrollHeight > el.clientHeight + 10) {
              const h = el.scrollHeight + Math.max(0, el.getBoundingClientRect().top);
              if (h > max) { max = h; who = el.tagName.toLowerCase() + '.' + String(el.className).split(' ')[0]; }
            }
          }
          return { max, who };
        });
        target = Math.min(Math.ceil(tall.max), 20000); shot_container = tall.who;
      }
      if (target > viewport.height) { await page.setViewportSize({ width: viewport.width, height: target }); await new Promise((r) => setTimeout(r, 1500)); }
      await page.screenshot({ path: path.join(dir, 'steps', `${id}.png`), timeout: 30000 });
      shot_px = [viewport.width, target];
    } catch (e) { shot = false; shot_error = String(e.message || e).split('\n')[0].slice(0, 200); }
    await page.setViewportSize(viewport).catch(() => {});
    const row = {
      step: stepNo, intent, target, t_start, t_end: new Date().toISOString(), url: page.url(),
      title: await page.title().catch(() => null), lang: await page.evaluate(() => document.documentElement.lang || null).catch(() => null),
      http_status: response && typeof response.status === 'function' ? response.status() : null,
      outcome, error, ...(page_replaced ? { page_replaced } : {}), ready, ready_s, screenshot: shot, screenshot_px: shot_px, screenshot_container: shot_container, screenshot_error: shot_error, html_bytes, frames,
    };
    actions.write(JSON.stringify(row) + '\n');
    return row;
  }

  async function close() {
    await context.tracing.stop({ path: path.join(dir, 'trace.zip') });
    actions.end();
    const meta = {
      run_id: runId, platform, label, kind: 'browser', started, extra,
      script: script ? { path: path.relative(ROOT, script), sha256: crypto.createHash('sha256').update(fs.readFileSync(script)).digest('hex') } : null, ended: new Date().toISOString(),
      network, context: freshContext ? 'fresh (no cookies or storage)' : 'capture profile', browser_version: browser.version(), playwright_core: require('playwright-core/package.json').version,
      node: process.version, cdp: CDP, viewport, ...(adopted ? { adopted_page: adoptPrefix } : {}),
    };
    fs.writeFileSync(path.join(dir, 'run.json'), JSON.stringify(meta, null, 2));
    if (!adopted) await page.close().catch(() => {});
    if (freshContext) await context.close().catch(() => {});
    await browser.close(); // disconnects; the capture Chrome keeps running
    return dir;
  }

  return { runId, dir, get page() { return page; }, context, step, close };
}
