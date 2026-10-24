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

let browser;
try { browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {}); }
catch { browser = await chromium.launch(); }
const rec = { url, fetched_at: new Date().toISOString().replace(/\.\d+Z$/, 'Z') };
const ctx = await browser.newContext({ userAgent: UA, extraHTTPHeaders: { 'Accept-Language': 'en,ar;q=0.8' }, viewport: { width: 1366, height: 900 } });
const page = await ctx.newPage();
try {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForLoadState('networkidle', { timeout: 12000 }).catch(() => {});
  rec.status = resp ? resp.status() : null;
  rec.final_url = page.url();
  rec.title = await page.title().catch(() => '');
  const text = await page.evaluate(() => document.body ? document.body.innerText : '').catch(() => '');
  fs.writeFileSync(out, text);
  rec.text_sha256 = crypto.createHash('sha256').update(text).digest('hex');
  rec.text_chars = text.length;
} catch (e) {
  rec.error = String(e.message || e).split('\n')[0].slice(0, 200);
}
await browser.close();
console.log(JSON.stringify(rec));
