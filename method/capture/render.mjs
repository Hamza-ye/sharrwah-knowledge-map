// Phase 2: render web pages in Chromium; keep the DOM after scripts run and the visible text.
// For items the raw fetch could not get, also keep the body the browser received.
// Usage: node render.mjs RUN_DIR LIST_JSON
import { createRequire } from 'module';
import fs from 'fs';
import path from 'path';
import crypto from 'crypto';
const require = createRequire(import.meta.url);
let pw;
try { pw = require(process.env.PLAYWRIGHT_MODULE || 'playwright'); }
catch { pw = require('/opt/node22/lib/node_modules/playwright'); }
const { chromium } = pw;

const [run, listPath] = process.argv.slice(2);
const list = JSON.parse(fs.readFileSync(listPath, 'utf8'));
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36';

// This session's browser fails some sites' own requests through its proxy (HTTP 400, or aborted), which left
// pages empty or showing only an error text: BigCommerce's Help Center, Zid's pricing pages. So every request is
// made by Playwright's own request client and its answer handed to the page. Redirects are handed over as they
// CAPTURE_EXPAND=1 opens, one at a time, what a page keeps closed until a click, such as FAQ answers, and keeps
// every line that appears: each <details>, and each control marked aria-expanded="false" that is neither a link
// nor a submit button. An FAQ often closes one answer as it opens the next, hence one at a time.
const EXPAND = process.env.CAPTURE_EXPAND === '1';
async function expandClosed(page) {
  if (!EXPAND) return [];
  const text = () => page.evaluate(() => document.body ? document.body.innerText : '').catch(() => '');
  const lines = s => s.split('\n').map(l => l.trim()).filter(Boolean);
  const seen = new Set(lines(await text()));
  const added = [];
  const start = page.url();
  const count = await page.evaluate(() => {
    const els = [...document.querySelectorAll('details:not([open]) > summary, [aria-expanded="false"]')]
      .filter(el => !el.closest('a[href]') && !el.matches('[type=submit], input, select'));
    els.forEach((el, i) => el.setAttribute('data-capture-toggle', String(i)));
    return els.length;
  }).catch(() => 0);
  for (let i = 0; i < Math.min(count, 200); i++) {
    const ok = await page.evaluate(i => {
      const el = document.querySelector(`[data-capture-toggle="${i}"]`);
      if (!el) return false;
      try { el.click(); } catch (e) { return false; }
      return true;
    }, i).catch(() => false);
    if (!ok) continue;
    await page.waitForTimeout(300);
    if (page.url() !== start) break;          // a click that navigates ends the opening
    for (const l of lines(await text())) if (!seen.has(l)) { seen.add(l); added.push(l); }
  }
  return added;
}

// come, so the page follows them itself. CAPTURE_ROUTE=0 turns this off.
const ROUTE = process.env.CAPTURE_ROUTE !== '0';
async function routeRequests(page) {
  if (!ROUTE) return;
  await page.route('**/*', async route => {
    try { await route.fulfill({ response: await route.fetch({ maxRedirects: 0 }) }); }
    catch { await route.continue().catch(() => {}); }
  });
}
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const ext = ct => /pdf/i.test(ct) ? 'pdf' : /html/i.test(ct) ? 'html' : /json/i.test(ct) ? 'json' : /xml/i.test(ct) ? 'xml' : 'bin';

let browser;
try { browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {}); }
catch { browser = await chromium.launch(); }
const version = browser.version();

async function one(it) {
  const dir = path.join(run, it.dir);
  const rec = { n: it.n, url: it.url, rendered_at: new Date().toISOString().replace(/\.\d+Z$/, 'Z'), browser: `Chromium ${version}`, routed: ROUTE };
  const ctx = await browser.newContext({ userAgent: UA, extraHTTPHeaders: { 'Accept-Language': process.env.CAPTURE_LANG || 'ar,en;q=0.8' }, viewport: { width: 1366, height: 900 } });
  const page = await ctx.newPage();
  await routeRequests(page);
  try {
    const resp = await page.goto(it.url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForLoadState('networkidle', { timeout: 12000 }).catch(() => {});
    rec.status = resp ? resp.status() : null;
    rec.final_url = page.url();
    rec.title = await page.title().catch(() => '');
    const html = await page.content();
    fs.writeFileSync(path.join(dir, 'rendered.html'), html);
    const text = await page.evaluate(() => document.body ? document.body.innerText : '').catch(() => '');
    fs.writeFileSync(path.join(dir, 'text.txt'), text);
    rec.text_chars = text.length;
    if (EXPAND) {                            // the lines a click shows, apart from the page as first shown
      const added = await expandClosed(page);
      rec.expanded_lines = added.length;
      if (added.length) fs.writeFileSync(path.join(dir, 'expanded.txt'), added.join('\n') + '\n');
    }
    if (it.keep_body && resp) {
      const body = await resp.body().catch(() => null);
      if (body && body.length) {
        const name = `raw-browser.${ext(resp.headers()['content-type'] || '')}`;
        fs.writeFileSync(path.join(dir, name), body);
        rec.browser_body = name; rec.browser_body_sha256 = sha(body);
        rec.browser_headers = resp.headers();
      }
    }
  } catch (e) {
    rec.error = String(e.message || e).split('\n')[0].slice(0, 200);
  }
  await ctx.close();
  fs.writeFileSync(path.join(dir, 'render.json'), JSON.stringify(rec, null, 1));
  return rec;
}

const out = [];
let i = 0;
async function worker() { while (i < list.length) { const it = list[i++]; out.push(await one(it)); } }
await Promise.all(Array.from({ length: Number(process.env.CAPTURE_WORKERS || 4) }, worker));
await browser.close();
fs.writeFileSync(path.join(run, 'phase2.json'), JSON.stringify(out, null, 0));
const ok = out.filter(r => !r.error && r.status && r.status < 400).length;
console.log(`rendered ${out.length}; status<400 ${ok}; other ${out.length - ok}`);
