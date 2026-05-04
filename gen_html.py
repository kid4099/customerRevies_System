import json

with open('D:/OneDrive/桌面/Cowork/系統客服回饋報告/april_full.json','r',encoding='utf-8') as f:
    d = json.load(f)

data_js = json.dumps(d, ensure_ascii=False)

css = """
:root{--bg:#FFFFFF;--s:#F7F9FA;--b:#E0E7EF;--t:#102A43;--td:#455A64;
      --g:#4ECDC4;--y:#F9A825;--r:#EF5350;--bl:#0099CC;--o:#FF9100;--tl:#4ECDC4;
      --sf:#EF5350;--cl:#0099CC;--pr:#4ECDC4}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:"Noto Sans TC","Montserrat","Segoe UI","PingFang TC",sans-serif;background:var(--bg);color:var(--t);min-height:100vh;line-height:1.6}
.hdr{background:linear-gradient(135deg,#4ECDC4 0%,#0099CC 100%);padding:28px 40px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px}
.hdr h1{font-size:26px;font-weight:700;color:#fff;letter-spacing:1.5px}
.sub{color:rgba(255,255,255,.8);font-size:13px;margin-top:4px}
.dbadge{background:rgba(255,255,255,.2);border:1px solid rgba(255,255,255,.35);border-radius:20px;padding:8px 18px;font-size:13px;color:#fff;backdrop-filter:blur(4px)}
.dbadge span{color:rgba(255,255,255,.75)}
.srow{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;padding:24px 40px;background:var(--s);border-bottom:1px solid var(--b)}
.sc{background:#fff;border:1px solid var(--b);border-radius:16px;padding:20px 24px;text-align:center;box-shadow:0 2px 12px rgba(0,0,0,.04)}
.scn{font-size:36px;font-weight:700;line-height:1;margin-bottom:6px;background:linear-gradient(135deg,#4ECDC4,#0099CC);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.scl{font-size:12px;color:var(--td);text-transform:uppercase;letter-spacing:1.5px;font-weight:600}
.sec{padding:28px 40px;border-bottom:1px solid var(--b)}
.sh{display:flex;align-items:center;gap:12px;margin-bottom:20px}
.snum{width:30px;height:30px;border-radius:50%;background:linear-gradient(135deg,#4ECDC4,#0099CC);display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;color:#fff;flex-shrink:0}
.stit{font-size:18px;font-weight:700;color:var(--t)}
.stit small{font-size:12px;color:var(--td);font-weight:400;margin-left:8px}
.leg{display:flex;gap:16px;margin-bottom:16px;flex-wrap:wrap;font-size:12px;color:var(--td)}
.li{display:flex;align-items:center;gap:6px}
.dot{width:10px;height:10px;border-radius:50%}
.sgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(285px,1fr));gap:10px}
.scard{background:#fff;border:1px solid var(--b);border-radius:14px;padding:14px 18px;display:flex;align-items:center;gap:12px;transition:box-shadow .2s,border-color .2s;box-shadow:0 2px 8px rgba(0,0,0,.04)}
.scard:hover{box-shadow:0 4px 18px rgba(0,153,204,.12);border-color:#4ECDC4}
.tl{width:14px;height:14px;border-radius:50%;flex-shrink:0}
.tl.green{background:var(--g);box-shadow:0 0 8px rgba(78,205,196,.5)}
.tl.yellow{background:var(--y);box-shadow:0 0 8px rgba(249,168,37,.5)}
.tl.red{background:var(--r);box-shadow:0 0 8px rgba(239,83,80,.5)}
.tl.flash{animation:fl .8s infinite}
@keyframes fl{0%,100%{opacity:1;box-shadow:0 0 12px var(--r)}50%{opacity:.2}}
.sn{font-size:12px;flex:1;min-width:0;line-height:1.4;color:var(--td);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.savg{font-size:18px;font-weight:700;flex-shrink:0}
.scnt{font-size:11px;color:var(--td);flex-shrink:0}
.sbg{height:4px;background:var(--s);border-radius:2px;margin-top:4px}
.sfill{height:4px;border-radius:2px}
.abadge{background:var(--r);color:#fff;font-size:10px;padding:3px 10px;border-radius:20px;flex-shrink:0;animation:fl .8s infinite;white-space:nowrap}
.sdist{display:flex;flex-direction:column;gap:8px;max-width:600px}
.sdb{display:flex;align-items:center;gap:10px;font-size:13px}
.sdlbl{width:24px;text-align:right;font-weight:700;color:var(--td)}
.sdbg{flex:1;height:20px;background:var(--s);border-radius:4px;overflow:hidden}
.sdfill{height:100%;border-radius:4px;display:flex;align-items:center;padding-left:8px;font-size:11px;color:#fff;font-weight:600}
.sdpct{width:80px;text-align:right;font-weight:700;color:var(--td)}
.ktabs{display:flex;gap:8px;margin-bottom:16px;flex-wrap:wrap}
.kt{padding:7px 18px;border-radius:20px;border:1px solid var(--b);background:#fff;color:var(--td);cursor:pointer;font-size:13px;transition:all .2s;font-weight:500}
.kt.active.safety{background:rgba(239,83,80,.08);border-color:var(--sf);color:var(--sf)}
.kt.active.clean{background:rgba(0,153,204,.08);border-color:var(--cl);color:var(--cl)}
.kt.active.process{background:rgba(78,205,196,.08);border-color:var(--pr);color:var(--pr)}
.kt.active.all{background:rgba(0,153,204,.08);border-color:var(--bl);color:var(--bl)}
.kcloud{display:flex;flex-wrap:wrap;gap:12px;align-items:center;min-height:80px}
.ktag{display:inline-flex;align-items:center;gap:6px;border-radius:20px;padding:8px 18px;cursor:pointer;transition:transform .15s;border:1px solid transparent;position:relative}
.ktag:hover{transform:scale(1.06)}
.ktag.safety{background:rgba(239,83,80,.08);border-color:rgba(239,83,80,.3);color:var(--sf)}
.ktag.clean{background:rgba(0,153,204,.08);border-color:rgba(0,153,204,.3);color:var(--cl)}
.ktag.process{background:rgba(78,205,196,.08);border-color:rgba(78,205,196,.3);color:var(--pr)}
.kcnt{background:rgba(0,0,0,.07);border-radius:10px;padding:1px 7px;font-size:11px}
.kpri{position:absolute;top:-7px;right:-4px;background:var(--r);color:#fff;font-size:9px;padding:1px 5px;border-radius:4px;font-weight:700}
.kdp{margin-top:16px;background:#fff;border:1px solid var(--b);border-radius:14px;padding:18px;display:none;box-shadow:0 2px 12px rgba(0,0,0,.06)}
.kdp.open{display:block}
.kdp h4{font-size:14px;margin-bottom:10px;color:var(--t)}
.ptag{display:inline-block;background:var(--s);border:1px solid var(--b);border-radius:8px;padding:3px 10px;font-size:12px;margin:3px;font-family:monospace;color:#0099CC;font-weight:600}
.vwrap{overflow-x:auto}
.vt{width:100%;border-collapse:collapse;font-size:13px}
.vt th{background:var(--s);border:1px solid var(--b);padding:12px 16px;text-align:left;color:var(--td);font-size:11px;text-transform:uppercase;letter-spacing:1.2px;white-space:nowrap;font-weight:700}
.vt td{border:1px solid var(--b);padding:12px 16px;vertical-align:middle;color:var(--t)}
.vt tr:hover td{background:rgba(78,205,196,.04)}
.vbw{display:flex;align-items:center;gap:8px;min-width:160px}
.vbbg{flex:1;height:8px;background:var(--s);border-radius:4px;overflow:hidden;border:1px solid var(--b)}
.vbfill{height:100%;border-radius:4px}
.vpct{font-size:13px;font-weight:700;min-width:48px;text-align:right}
.vpl{font-family:monospace;font-size:14px;font-weight:700;color:#0099CC;letter-spacing:1px}
.vkl{display:flex;flex-wrap:wrap;gap:4px}
.vkc{font-size:11px;padding:2px 8px;border-radius:10px;background:rgba(239,83,80,.08);border:1px solid rgba(239,83,80,.25);color:var(--sf)}
.ebtn{background:#fff;border:1px solid var(--b);color:var(--td);border-radius:20px;padding:5px 14px;cursor:pointer;font-size:11px;transition:all .2s}
.ebtn:hover,.ebtn.active{border-color:var(--bl);color:var(--bl);background:rgba(0,153,204,.06)}
.cr{display:none}
.cr.open{display:table-row}
.cb{background:var(--s);border-radius:12px;padding:14px}
.ci{border-bottom:1px solid var(--b);padding:10px 0;font-size:12px;display:flex;gap:12px;align-items:flex-start}
.ci:last-child{border-bottom:none}
.ctxt{color:var(--td);line-height:1.6}
.rvgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:12px}
.rvc{background:#fff;border:1px solid var(--b);border-radius:14px;padding:16px 18px;box-shadow:0 2px 8px rgba(0,0,0,.04)}
.rvc.s1,.rvc.s2{border-left:4px solid var(--r)}
.rvc.s3{border-left:4px solid var(--y)}
.rvc.s4,.rvc.s5{border-left:4px solid var(--g)}
.rvmeta{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
.rvst{font-size:11px;color:var(--td)}
.rvtxt{font-size:13px;color:var(--t);line-height:1.6}
.rvplate{font-family:monospace;font-size:12px;color:#0099CC;font-weight:600}
.mgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px}
.mc{background:#fff;border:1px solid var(--b);border-radius:12px;padding:14px 18px}
.mcname{font-size:12px;color:var(--td);margin-bottom:6px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.mcavg{font-size:22px;font-weight:700;background:linear-gradient(135deg,#4ECDC4,#0099CC);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.mcbar{height:6px;background:var(--s);border-radius:3px;margin-top:6px}
.mcfill{height:6px;border-radius:3px;background:linear-gradient(90deg,#4ECDC4,#0099CC)}
.mccnt{font-size:11px;color:var(--td);margin-top:4px}
footer{text-align:center;padding:24px;color:var(--td);font-size:12px;border-top:1px solid var(--b);background:var(--s)}
@media(max-width:768px){.srow{grid-template-columns:repeat(2,1fr);padding:16px}.sec,.hdr{padding:20px 16px}.sgrid{grid-template-columns:1fr}}
"""

js = """
const DATA = %s;
// 評分分佈
(function(){
  const sd=DATA.scoreDist,total=DATA.total;
  const colors={'5':'#4ECDC4','4':'#0099CC','3':'#F9A825','2':'#FF9100','1':'#EF5350'};
  const cont=document.getElementById('sdist');
  [5,4,3,2,1].forEach(s=>{
    const cnt=sd[s]||0;
    const pct=(cnt/total*100).toFixed(1);
    cont.innerHTML+=`<div class="sdb"><span class="sdlbl">${s}&#9733;</span>
      <div class="sdbg"><div class="sdfill" style="width:${pct}%%;background:${colors[s]}">${pct>8?pct+'%%':''}</div></div>
      <span class="sdpct">${cnt} (${pct}%%)</span></div>`;
  });
})();
// 站點
let stD=[...DATA.stations];
function renderStations(arr){
  const sg=document.getElementById('sg');sg.innerHTML='';
  arr.forEach(s=>{
    const cls=s.avg>=4?'green':s.avg>=3?'yellow':'red';
    const flash=s.last3bad?' flash':'';
    const ac=s.avg>=4?'var(--g)':s.avg>=3?'var(--y)':'var(--r)';
    const fc=s.avg>=4?'#4ECDC4':s.avg>=3?'#F9A825':'#EF5350';
    const badge=s.last3bad?'<span class="abadge">連續低評</span>':'';
    sg.innerHTML+=`<div class="scard"><div class="tl ${cls}${flash}"></div>
      <div style="flex:1;min-width:0"><div class="sn" title="${s.name}">${s.name}</div>
      <div class="sbg"><div class="sfill" style="width:${(s.avg/5*100).toFixed(0)}%%;background:${fc}"></div></div></div>
      <span class="scnt">${s.count}筆</span>
      <span class="savg" style="color:${ac}">${s.avg}</span>${badge}</div>`;
  });
}
function sortStations(by){
  if(by==='avg') stD.sort((a,b)=>b.avg-a.avg);
  else if(by==='count') stD.sort((a,b)=>b.count-a.count);
  else stD.sort((a,b)=>a.name.localeCompare(b.name,'zh-Hant'));
  renderStations(stD);
}
renderStations(stD);
// 關鍵字
const KWS=[
  {name:'安全帽異味',cat:'clean',count:9,phrases:['安全帽臭','帽子臭','安全帽請清潔','安全帽又臭']},
  {name:'APP/流程繁瑣',cat:'process',count:7,phrases:['APP','程序複雜','麻煩','照片上傳']},
  {name:'電力不足',cat:'safety',count:6,phrases:['電瓶沒電','電量只有','差點沒電','爛電池都沒電'],priority:true},
  {name:'擋風板眩光',cat:'clean',count:6,phrases:['擋風板','眩光','炫光']},
  {name:'客服回應',cat:'process',count:6,phrases:['客服沒有回應','客服不在','真人客服']},
  {name:'保養維護',cat:'process',count:6,phrases:['保養訊息','需要保養','車很髒']},
  {name:'車廂開啟問題',cat:'process',count:4,phrases:['車廂無法開啟','車廂打不開','車廂關不緊','車廂開不了']},
  {name:'鑰匙感應',cat:'process',count:4,phrases:['鑰匙打不開','無法感應']},
  {name:'輪胎/安全危險',cat:'safety',count:2,phrases:['後輪沒紋路','輪胎沒氣','騎起來晃動'],priority:true},
  {name:'避震異音',cat:'safety',count:3,phrases:['避震有問題','有異音','龍頭轉向不穩']},
  {name:'車廂積水',cat:'clean',count:2,phrases:['電池上面都是水']},
  {name:'計費爭議',cat:'process',count:2,phrases:['超時','計費不合理']},
];
let curCat='all',openKW=null;
function fk(cat,el){
  document.querySelectorAll('.kt').forEach(e=>e.className='kt '+e.dataset.cat);
  el.classList.add('active');
  curCat=cat;renderKW();
  document.getElementById('kd').classList.remove('open');openKW=null;
}
function renderKW(){
  const kc=document.getElementById('kc');kc.innerHTML='';
  KWS.filter(k=>curCat==='all'||k.cat===curCat).forEach(k=>{
    const sz=12+k.count*1.8;
    const pri=k.priority?'<span class="kpri">HIGH</span>':'';
    kc.innerHTML+=`<div class="ktag ${k.cat}" style="font-size:${sz.toFixed(0)}px" onclick="showKD('${k.name}')">${k.name}<span class="kcnt">${k.count}</span>${pri}</div>`;
  });
}
function showKD(name){
  const k=KWS.find(x=>x.name===name);if(!k)return;
  const kd=document.getElementById('kd');
  if(openKW===name){kd.classList.remove('open');openKW=null;return;}
  openKW=name;
  kd.innerHTML=`<h4>「${k.name}」相關評論模式</h4>${k.phrases.map(p=>`<span class="ptag">${p}</span>`).join('')}
    <p style="font-size:12px;color:var(--td);margin-top:12px">共發現 <strong>${k.count}</strong> 筆相關回饋，建議優先關注</p>`;
  kd.classList.add('open');
}
renderKW();
// VQI
const vb=document.getElementById('vb');
DATA.vqi.forEach((v,i)=>{
  const c=v.vqi>=30?'var(--r)':v.vqi>=15?'var(--y)':'var(--g)';
  const w=Math.min(100,v.vqi*2);
  const rid='cr'+i;
  const rvSnippet=v.reviews.slice(0,1).map(r=>`<span class="vkc">${String(r).slice(0,25)}</span>`).join('');
  vb.innerHTML+=`<tr>
    <td style="font-weight:700;color:var(--td)">#${i+1}</td>
    <td><span class="vpl">${v.plate}</span></td>
    <td><div class="vbw"><div class="vbbg"><div class="vbfill" style="width:${w}%%;background:${c}"></div></div>
      <span class="vpct" style="color:${c}">${v.vqi}%%</span></div></td>
    <td style="font-weight:700">${v.hw}/${v.total}</td>
    <td><div class="vkl">${rvSnippet}</div></td>
    <td><button class="ebtn" onclick="toggleCR('${rid}')">詳情</button></td></tr>
  <tr class="cr" id="${rid}"><td colspan="6">
    <div class="cb">${v.reviews.map(r=>`<div class="ci"><span style="color:#F9A825;margin-right:6px">&#9888;</span><span class="ctxt">${r}</span></div>`).join('')}</div>
  </td></tr>`;
});
function toggleCR(id){document.getElementById(id).classList.toggle('open');}
// 車型
const mg=document.getElementById('mg');
DATA.models.sort((a,b)=>b.avg-a.avg).forEach(m=>{
  mg.innerHTML+=`<div class="mc"><div class="mcname" title="${m['車型']}">${m['車型']}</div>
    <div class="mcavg">${m['avg']}</div>
    <div class="mcbar"><div class="mcfill" style="width:${(m.avg/5*100).toFixed(0)}%%"></div></div>
    <div class="mccnt">${m['count']} 筆評論</div></div>`;
});
// 非預設評論
const STARS='★★★★★';
let rvF=0;
function renderRv(){
  const rvg=document.getElementById('rvg');
  const list=DATA.reviews.filter(r=>rvF===0||r.score===rvF);
  rvg.innerHTML='';
  list.forEach(r=>{
    const sc=Math.min(5,Math.max(1,r.score));
    const star=STARS.slice(0,sc)+'<span style="color:#ddd">'+STARS.slice(sc)+'</span>';
    const stn=r.station.replace('ZOCHA-','').replace('ZOCHA','').slice(0,20);
    rvg.innerHTML+=`<div class="rvc s${sc}">
      <div class="rvmeta"><span class="rvplate">${r.plate}</span>
        <span style="color:#F9A825;font-size:14px">${star}</span></div>
      <div class="rvtxt">${String(r.text).slice(0,150)}</div>
      <div class="rvst" style="margin-top:8px">${stn}</div></div>`;
  });
}
function filterRv(s,el){
  document.querySelectorAll('.rvfbtn').forEach(b=>b.classList.remove('active'));
  el.classList.add('active');rvF=s;renderRv();
}
renderRv();
""" % data_js

html = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ZOCHA 2026年4月份客戶評論看板</title>
<style>""" + css + """</style>
</head>
<body>
<header class="hdr">
  <div>
    <h1>&#x1F4CA; ZOCHA 4月份客戶評論看板</h1>
    <div class="sub">機車租賃服務 &#183; 2026年4月完整月度分析報告</div>
  </div>
  <div class="dbadge"><span>資料區間：</span>2026/04/01 &#8212; 2026/04/30</div>
</header>

<div class="srow">
  <div class="sc"><div class="scn">1,094</div><div class="scl">總評論數</div></div>
  <div class="sc"><div class="scn">3.85</div><div class="scl">整體平均星等</div></div>
  <div class="sc"><div class="scn">88</div><div class="scl">非預設評論數</div></div>
  <div class="sc"><div class="scn">55</div><div class="scl">服務站點數</div></div>
</div>

<div class="sec">
  <div class="sh"><div class="snum">0</div>
    <div class="stit">評分分佈總覽 <small>Score Distribution Overview</small></div></div>
  <div class="sdist" id="sdist"></div>
</div>

<div class="sec">
  <div class="sh"><div class="snum">1</div>
    <div class="stit">站點即時滿意度 <small>Instant CSAT per Station</small></div></div>
  <div class="leg">
    <div class="li"><div class="dot" style="background:var(--g)"></div>優質 (avg &ge; 4.0)</div>
    <div class="li"><div class="dot" style="background:var(--y)"></div>普通 (3.0 &ndash; 3.9)</div>
    <div class="li"><div class="dot" style="background:var(--r)"></div>警示 (avg &lt; 3.0)</div>
  </div>
  <div style="margin-bottom:12px;display:flex;gap:8px;flex-wrap:wrap">
    <button class="ebtn" onclick="sortStations('avg')">依平均分排序</button>
    <button class="ebtn" onclick="sortStations('count')">依評論數排序</button>
    <button class="ebtn" onclick="sortStations('name')">依站名排序</button>
  </div>
  <div class="sgrid" id="sg"></div>
</div>

<div class="sec">
  <div class="sh"><div class="snum">2</div>
    <div class="stit">關鍵字熱搜雲 <small>Keyword Frequency &amp; Alert</small></div></div>
  <div class="ktabs">
    <div class="kt active all" data-cat="all" onclick="fk('all',this)">全部</div>
    <div class="kt safety" data-cat="safety" onclick="fk('safety',this)">&#x26A0; 安全類（最高優先）</div>
    <div class="kt clean" data-cat="clean" onclick="fk('clean',this)">&#x1F6BF; 清潔類</div>
    <div class="kt process" data-cat="process" onclick="fk('process',this)">&#x1F4F1; 流程類</div>
  </div>
  <div class="kcloud" id="kc"></div>
  <div class="kdp" id="kd"></div>
</div>

<div class="sec">
  <div class="sh"><div class="snum">3</div>
    <div class="stit">車況品質指數 <small>Vehicle Quality Index (VQI)</small></div></div>
  <p style="font-size:13px;color:var(--td);margin-bottom:14px">
    公式：VQI = 車輛硬體負評數 &divide; 總訂單數 &times; 100%　|　僅列具硬體相關回饋之車牌
  </p>
  <div class="vwrap">
    <table class="vt">
      <thead><tr>
        <th>排名</th><th>車牌</th><th>VQI 指數</th>
        <th>硬體負評/總單</th><th>評論節錄</th><th>詳情</th>
      </tr></thead>
      <tbody id="vb"></tbody>
    </table>
  </div>
</div>

<div class="sec">
  <div class="sh"><div class="snum">4</div>
    <div class="stit">車型平均滿意度 <small>Model Satisfaction (&#8805;5 reviews)</small></div></div>
  <div class="mgrid" id="mg"></div>
</div>

<div class="sec">
  <div class="sh"><div class="snum">5</div>
    <div class="stit">非預設客戶評論 <small>Genuine Customer Feedback (88筆)</small></div></div>
  <div style="margin-bottom:12px;display:flex;gap:8px;flex-wrap:wrap">
    <button class="ebtn rvfbtn active" onclick="filterRv(0,this)">全部 (88)</button>
    <button class="ebtn rvfbtn" onclick="filterRv(1,this)">&#9733; 1星</button>
    <button class="ebtn rvfbtn" onclick="filterRv(2,this)">&#9733;&#9733; 2星</button>
    <button class="ebtn rvfbtn" onclick="filterRv(3,this)">&#9733;&#9733;&#9733; 3星</button>
    <button class="ebtn rvfbtn" onclick="filterRv(4,this)">&#9733;&#9733;&#9733;&#9733; 4星</button>
    <button class="ebtn rvfbtn" onclick="filterRv(5,this)">&#9733;&#9733;&#9733;&#9733;&#9733; 5星</button>
  </div>
  <div class="rvgrid" id="rvg"></div>
</div>

<footer>
  資料來源：2026/04/01 &ndash; 2026/04/30 客戶評論（共 1,094 筆）
  &nbsp;&#183;&nbsp; ZOCHA 租車服務品質監控系統 &nbsp;&#183;&nbsp; 生成時間：2026-05-04
</footer>
<script>""" + js + """</script>
</body>
</html>"""

out = 'D:/OneDrive/桌面/Cowork/系統客服回饋報告/4月份客戶評論看板.html'
with open(out, 'w', encoding='utf-8') as f:
    f.write(html)
print('DONE:', out)
