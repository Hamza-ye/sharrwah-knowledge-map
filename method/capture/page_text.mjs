// Working copy of one page's visible text, for reading and quoting while a study runs.
// It renders the page in Chromium, writes document.body.innerText to OUT_TXT, and prints
// {url, final_url, status, title, fetched_at, text_sha256, text_chars} as one JSON line.
// Working copies are not evidence: cited pages are captured afterwards with fetch_raw.py and render.mjs.
// Usage: node page_text.mjs URL OUT_TXT
import { createRequire } from 'module';
import fs from 'fs';
import crypto from 'crypto';
const require = createRequire(import.meta.url);
let pw;
try { pw = require(process.env.PLAYWRIGHT_MODULE || 'playwright'); }
catch { pw = require('/opt/node22/lib/node_modules/playwright'); }
const { chromium } = pw;

const [url, out] = process.argv.slice(2);
if (!url || !out) { console.error('usage: node page_text.mjs URL OUT_TXT'); process.exit(2); }
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

let browser;
try { browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {}); }
catch { browser = await chromium.launch(); }
const rec = { url, fetched_at: new Date().toISOString().replace(/\.\d+Z$/, 'Z'), routed: ROUTE };
const ctx = await browser.newContext({ userAgent: UA, extraHTTPHeaders: { 'Accept-Language': 'en,ar;q=0.8' }, viewport: { width: 1366, height: 900 } });
const page = await ctx.newPage();
await routeRequests(page);
try {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForLoadState('networkidle', { timeout: 12000 }).catch(() => {});
  rec.status = resp ? resp.status() : null;
  rec.final_url = page.url();
  rec.title = await page.title().catch(() => '');
  let text = await page.evaluate(() => document.body ? document.body.innerText : '').catch(() => '');
  if (EXPAND) {
    const added = await expandClosed(page);
    rec.expanded = added.length;
    if (added.length) text += '\n----- shown on a click (CAPTURE_EXPAND=1) -----\n' + added.join('\n') + '\n';
  }
  fs.writeFileSync(out, text);
  rec.text_sha256 = crypto.createHash('sha256').update(text).digest('hex');
  rec.text_chars = text.length;
} catch (e) {
  rec.error = String(e.message || e).split('\n')[0].slice(0, 200);
}
await browser.close();
console.log(JSON.stringify(rec));
