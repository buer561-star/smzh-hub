const { chromium } = require('/opt/node22/lib/node_modules/playwright/index.js');
const fs = require('fs');
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport:{width:1440,height:1000}, ignoreHTTPSErrors:true });
  const p = await ctx.newPage();
  await p.goto('https://smzh.ch/de/', { waitUntil:'domcontentloaded', timeout:60000 });
  try { await p.waitForLoadState('networkidle',{timeout:15000}); } catch {}
  for (const l of ['Alle ablehnen','Alle annehmen']) { const x=p.getByRole('button',{name:l}); if(await x.count()){try{await x.first().click({timeout:1500});break;}catch{}} }
  const triggers = p.locator('nav.smzh-navbar [data-dropdown-trigger="true"]');
  const n = await triggers.count();
  const menus = [];
  for (let i=0;i<n;i++){
    const label = (await triggers.nth(i).innerText()).trim();
    await triggers.nth(i).click();
    await p.waitForTimeout(700);
    // hover each left category to force any lazy right-columns into DOM
    const cats = p.locator('.dropdown-navigation-wrapper .group\\/sublinks');
    const cn = await cats.count();
    for (let j=0;j<cn;j++){ try{ await cats.nth(j).hover({timeout:800}); await p.waitForTimeout(150);}catch{} }
    const html = await p.evaluate(() => {
      const w = document.querySelector('.dropdown-navigation-wrapper');
      return w ? w.outerHTML : null;
    });
    menus.push({ index:i, label, html });
    console.error(`menu ${i} "${label}": ${html?html.length:'NULL'} chars, cats=${cn}`);
    // close by clicking again
    await triggers.nth(i).click().catch(()=>{});
    await p.waitForTimeout(300);
  }
  fs.writeFileSync('build/menus.json', JSON.stringify(menus,null,1));
  await b.close();
})();
