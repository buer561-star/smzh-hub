const { chromium } = require('/opt/node22/lib/node_modules/playwright/index.js');
const fs=require('fs');
(async () => {
  const b = await chromium.launch();
  const p = await b.newContext({viewport:{width:1440,height:1000}, ignoreHTTPSErrors:true}).then(c=>c.newPage());
  await p.goto('https://smzh.ch/de/',{waitUntil:'domcontentloaded',timeout:60000});
  try{await p.waitForLoadState('networkidle',{timeout:15000});}catch{}
  for(const l of ['Alle ablehnen','Alle annehmen']){const x=p.getByRole('button',{name:l});if(await x.count()){try{await x.first().click({timeout:1200});break;}catch{}}}
  const trigs=p.locator('nav.smzh-navbar [data-dropdown-trigger="true"]');
  const n=await trigs.count();
  const menus=[];
  for(let i=0;i<n;i++){
    const label=(await trigs.nth(i).innerText()).trim();
    await trigs.nth(i).click(); await p.waitForTimeout(500);
    const data = await p.evaluate(()=>{
      const w=document.querySelector('.dropdown-navigation-wrapper'); if(!w)return null;
      const inner=w.firstElementChild; const leftCol=inner.firstElementChild;
      const right=w.querySelector('.dropdown-nav-right');
      const leftItems=[...leftCol.children].map(d=>d.textContent.trim());
      const blocks=[...right.children];
      function links(el){return [...el.querySelectorAll('a[href^="/de"]')].map(a=>({text:a.textContent.trim().replace(/\s+/g,' '),href:a.getAttribute('href')})).filter(x=>x.text);}
      // promo (block0) links too (the default right content)
      const cats=leftItems.map((name,idx)=>({name, links: blocks[idx+1]?links(blocks[idx+1]):[]}));
      return {promo: links(blocks[0]), cats};
    });
    menus.push({label, ...data});
    await trigs.nth(i).click().catch(()=>{}); await p.waitForTimeout(250);
  }
  fs.writeFileSync('build/menu-structure.json', JSON.stringify(menus,null,1));
  // brief print
  menus.forEach(m=>{console.error(`\n${m.label}: promo=${m.promo.length}`);m.cats.forEach(c=>console.error(`   ${c.name}: ${c.links.length} links`));});
  await b.close();
})();
