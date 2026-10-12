// Render a page and write its anchors (text TAB href) to OUT. Prints status JSON like page_text.mjs.
import { createRequire } from 'module';
import fs from 'fs';
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
const rec = { url };
try {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForLoadState('networkidle', { timeout: 12000 }).catch(() => {});
  rec.status = resp ? resp.status() : null; rec.final_url = page.url();
  const links = await page.evaluate(() => Array.from(document.querySelectorAll('a[href]')).map(a => (a.innerText || '').replace(/\s+/g, ' ').trim() + '\t' + a.href));
  fs.writeFileSync(out, links.join('\n') + '\n');
} catch (e) { rec.error = String(e.message || e).split('\n')[0].slice(0, 200); }
await browser.close();
console.log(JSON.stringify(rec));
