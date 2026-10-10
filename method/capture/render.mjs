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
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const ext = ct => /pdf/i.test(ct) ? 'pdf' : /html/i.test(ct) ? 'html' : /json/i.test(ct) ? 'json' : /xml/i.test(ct) ? 'xml' : 'bin';

let browser;
try { browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {}); }
catch { browser = await chromium.launch(); }
const version = browser.version();

async function one(it) {
  const dir = path.join(run, it.dir);
  const rec = { n: it.n, url: it.url, rendered_at: new Date().toISOString().replace(/\.\d+Z$/, 'Z'), browser: `Chromium ${version}` };
  const ctx = await browser.newContext({ userAgent: UA, extraHTTPHeaders: { 'Accept-Language': 'ar,en;q=0.8' }, viewport: { width: 1366, height: 900 } });
  const page = await ctx.newPage();
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
await Promise.all([worker(), worker(), worker(), worker()]);
await browser.close();
fs.writeFileSync(path.join(run, 'phase2.json'), JSON.stringify(out, null, 0));
const ok = out.filter(r => !r.error && r.status && r.status < 400).length;
console.log(`rendered ${out.length}; status<400 ${ok}; other ${out.length - ok}`);
