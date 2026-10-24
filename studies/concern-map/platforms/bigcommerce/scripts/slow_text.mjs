// Like page_text.mjs, but waits up to WAIT_MS (default 40000) for the body text to stop growing. Usage: node slow_text.mjs URL OUT
import { createRequire } from 'module';
import fs from 'fs';
import crypto from 'crypto';
const require = createRequire(import.meta.url);
let pw;
try { pw = require(process.env.PLAYWRIGHT_MODULE || 'playwright'); }
catch { pw = require('/opt/node22/lib/node_modules/playwright'); }
const { chromium } = pw;
const [url, out] = process.argv.slice(2);
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36';
const browser = await chromium.launch();
const ctx = await browser.newContext({ userAgent: UA, extraHTTPHeaders: { 'Accept-Language': 'en,ar;q=0.8' }, viewport: { width: 1366, height: 900 } });
const page = await ctx.newPage();
const rec = { url, fetched_at: new Date().toISOString().replace(/\.\d+Z$/, 'Z') };
try {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  rec.status = resp ? resp.status() : null;
  const limit = Date.now() + Number(process.env.WAIT_MS || 40000);
  let last = -1, stable = 0, text = '';
  while (Date.now() < limit) {
    await page.waitForTimeout(1500);
    text = await page.evaluate(() => document.body ? document.body.innerText : '').catch(() => '');
    if (text.length > 200 && text.length === last) { if (++stable >= 3) break; } else stable = 0;
    last = text.length;
  }
  rec.final_url = page.url(); rec.title = await page.title().catch(() => '');
  fs.writeFileSync(out, text);
  rec.text_sha256 = crypto.createHash('sha256').update(text).digest('hex'); rec.text_chars = text.length;
} catch (e) { rec.error = String(e.message || e).split('\n')[0].slice(0, 200); }
await browser.close();
console.log(JSON.stringify(rec));
