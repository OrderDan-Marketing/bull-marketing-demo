# -*- coding: utf-8 -*-
"""Generate the 5 service sub-pages from data. Run: python build_pages.py
(2026-09-09 起只剩紫版:頁面同時載入 style.css + theme-purple.css,purple/ 僅留轉址殘檔)"""
import html as H, os, time
CSS_V = time.strftime('%Y%m%d%H%M')  # 每次重產都換版本號,避免 GitHub Pages/瀏覽器快取舊 CSS

NAV = '''<header>
  <div class="wrap nav">
    <a class="logo" href="index.html"><img src="assets/logo.webp" alt="牛排行銷 BULL MARKETING"></a>
    <ul id="menu">
      <li class="has-sub"><a href="index.html#services">五大服務</a>
        <ul class="sub">
          <li><a href="web.html">網站建置|雅芬</a></li>
          <li><a href="crm.html">LINE 會員系統|可芳</a></li>
          <li><a href="visual.html">視覺設計|豐澤</a></li>
          <li><a href="video.html">短影音|David</a></li>
          <li><a href="ads.html">廣告投放|丹丹</a></li>
        </ul>
      </li>
      <li><a href="index.html#integration">整合方式</a></li>
      <li><a href="index.html#projects">實際案例</a></li>
      <li><a href="index.html#plans">方案</a></li>
      <li><a href="index.html#faq">常見問題</a></li>
    </ul>
    <a class="btn btn-gold" href="#contact">預約免費診斷</a>
    <button class="burger" aria-label="選單" onclick="document.getElementById('menu').classList.toggle('open')"><span></span><span></span><span></span></button>
  </div>
</header>'''

LEAD = open('index.html', encoding='utf-8').read()
LEAD = LEAD[LEAD.index('<!-- 8 LEAD FORM -->'):LEAD.index('</section>', LEAD.index('<!-- 8 LEAD FORM -->')) + 10]

FOOT = '''<footer>
  <div class="wrap">
    <img src="assets/logo.webp" alt="牛排行銷">
    <div class="slogan">行銷不走彎路,就是捷徑。</div>
    <div>© 2026 牛排行銷 BULL MARKETING</div>
  </div>
</footer>
<div class="mbar">
  <a class="tel" href="tel:0900000000">☎ 來電</a>
  <a class="line" href="#" onclick="alert('LINE 官方帳號連結待接');return false;">LINE</a>
  <a class="form" href="#contact">預約免費診斷</a>
</div>
<script src="app.js"></script>
</body>
</html>'''

ALL = [
    ('web', '網站建置', '雅芬', 'WEBSITE'),
    ('crm', 'LINE 會員系統', '可芳', 'CRM'),
    ('visual', '視覺設計', '豐澤', 'VISUAL'),
    ('video', '短影音', 'David', 'VIDEO'),
    ('ads', '廣告投放', '丹丹', 'ADS'),
]

def chips(items):
    return '<div class="chips">' + ''.join(f'<span>{H.escape(x)}</span>' for x in items) + '</div>'

def steps_html(steps):
    out = []
    for i, (t, d, tags) in enumerate(steps, 1):
        out.append(f'''<div class="step reveal"><div class="no">{i:02d}</div><div><h3>{H.escape(t)}</h3><p>{H.escape(d)}</p>{chips(tags) if tags else ''}</div></div>''')
    return '<div class="steps">' + ''.join(out) + '</div>'

def vd_cards(items):  # (title, who, [li html...]) 三欄卡(video/visual/web 共用)
    return '<div class="vd-grid3">' + ''.join(
        f'<div class="vd-card reveal"><h3>{H.escape(t)}</h3><div class="who">{H.escape(w)}</div><ul>'
        + ''.join(f'<li>{x}</li>' for x in lis) + '</ul></div>' for t, w, lis in items) + '</div>'

def vd_aud(items):  # (title, goal, [chips])
    return '<div class="vd-grid3">' + ''.join(
        f'<div class="vd-card reveal"><h3>{H.escape(t)}</h3><div class="who">{H.escape(g)}</div>{chips(c)}</div>'
        for t, g, c in items) + '</div>'

def other_links(key):
    return '<div class="other-svc">' + ''.join(
        f'<a href="{k}.html">{n}<span>→</span></a>' for k, n, _, _ in ALL if k != key) + '</div>'

def page(key, name, owner, tag, hero_sub, owner_desc, stats, steps, cases_html, todo=None,
         owner_img=None, after_hero='', extra_html=''):
    stats_html = ''.join(f'<div><b>{H.escape(v)}</b><span>{H.escape(l)}</span></div>' for v, l in stats)
    av_html = (f'<div class="av photo"><img src="{owner_img}" alt="{H.escape(owner)}"></div>' if owner_img
               else f'<div class="av">{owner[0]}</div>')
    doc = f'''<!DOCTYPE html>
<html lang="zh-Hant-TW">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name}|牛排行銷 BULL MARKETING</title>
<meta name="description" content="牛排行銷 {name} 服務流程與實際案例。">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&family=Noto+Serif+TC:wght@600;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css?v={CSS_V}">
<link rel="stylesheet" href="theme-purple.css?v={CSS_V}">
</head>
<body>
{NAV}
<section class="sub-hero" id="top">
  <div class="wrap">
    <div class="crumb"><a href="index.html">首頁</a> / <a href="index.html#services">五大服務</a> / {name}</div>
    <div class="grid">
      <div>
        <div class="eyebrow">{tag}|五大服務之一</div>
        <h1 class="serif">{name}</h1>
        <p class="sub">{hero_sub}</p>
        <div class="cta" style="display:flex;gap:14px;flex-wrap:wrap">
          <a class="btn btn-gold" href="#contact">預約免費診斷 →</a>
          <a class="btn btn-ghost" href="#cases">看實際案例</a>
        </div>
        <div class="stats">{stats_html}</div>
      </div>
      <div class="owner reveal">
        {av_html}
        <div><b>{owner}</b><small>{tag} LEAD</small><p>{owner_desc}</p></div>
      </div>
    </div>
  </div>
</section>
{after_hero}
<section id="process">
  <div class="wrap">
    <div class="eyebrow">01|Service Process</div>
    <h2 class="h2">服務流程</h2>
    <p class="lead">從第一次談到交付,每一步做什麼、你會拿到什麼。</p>
    {steps_html(steps)}
  </div>
</section>

<section id="cases" style="background:#fff">
  <div class="wrap">
    <div class="eyebrow">02|Case Studies</div>
    <h2 class="h2">實際案例</h2>
    {cases_html}
    {('<div class="todo"><b>' + todo[0] + '</b>' + todo[1] + '</div>') if todo else ''}
  </div>
</section>
{extra_html}
<section>
  <div class="wrap">
    <div class="eyebrow">Integrate</div>
    <h2 class="h2">搭配其他服務,效果加乘</h2>
    <p class="lead">{name}只是其中一段;接上其他四段,才是會轉單的行銷。</p>
    {other_links(key)}
  </div>
</section>

{LEAD}
{FOOT}'''
    open(f'{key}.html', 'w', encoding='utf-8').write(doc)
    print('wrote', key)

# ================= ADS (丹丹) — real data =================
ads_steps = [
    ('分析產業別', '每個產業的受眾行為、競爭態勢、旺淡季節奏都不同。投放前先研究產業特性與競品策略,依現況量身打造投放框架,不套模板。', ['競品分析', '受眾研究', '季節性策略', '市場定位']),
    ('確認網站追蹤代碼及串接完整性', '核心差異化。追蹤沒埋好,所有優化都是瞎猜——親自檢查並建置 GTM、Meta Pixel + CAPI、GA4 到伺服器端追蹤,確保每一筆轉換都被正確記錄。', ['GTM', 'Meta Pixel + CAPI', 'GA4', 'Server-Side Tracking']),
    ('依照銷售漏斗設立廣告活動', '一個活動塞多個目標是最常見的預算浪費。依漏斗每一層設立目標明確的獨立活動:品牌認知/觸及 → 流量/互動/名單 → 購買/表單/來電,讓演算法精準學習。', ['曝光→互動→轉換', '獨立活動', '目標明確']),
    ('建置客製 AI 助理,日追蹤績效', 'n8n 自動化串接各平台數據,AI 助理每日監控指標異常、產出優化建議——績效即時通知、名單即時傳送,從「週報等結果」升級為「每日即時反應」。', ['n8n 自動化', 'AI 績效監控', '每日異常偵測', '名單即時傳送']),
    ('維持穩定銷售循環', '廣告不是一次性衝刺。再行銷受眾經營、素材持續迭代、預算動態調配,把投放轉化為長期穩定的營收成長動力。', ['再行銷受眾', '素材迭代', '預算動態調配']),
]
ads_results = [
    ('Google', '綜合型', '2025.08~10|看護服務', '$213,278', '每天都有成交|目標動作:撥打電話;關鍵字點擊成本 20 元/次,為同業的 60%(業主調查)'),
    ('FB Google', '綜合型', '2025.04~09|餐飲實業', '$164,884', '網站人流成長 40 倍(1,500 → 60,000 人/半年)|網站新客成長 25 倍(800 → 20,000 人/半年)'),
    ('FB', '綜合型', '2025.03~05|冷凍食品電商', '$377,000', '3 月底 ROAS <3 拉升至 >4.5|4 月 ROAS 6.5|5 月 ROAS 7.1'),
    ('FB', '綜合型', '2022~2023|保健食品', '$14,400,000', '一半占比顯示標籤為成效出色,轉換 ROAS 約 2.5~3.5'),
    ('Google', '綜合型', '2022~2023|保健食品', '$3,600,000', '純 Ads 轉換 ROAS 2.5,實際轉換 ROAS 約 3~3.5'),
    ('FB', '綜合型', '2025.08|宗教用品電商', '$77,340', '營收 30%'),
    ('蝦皮', '流量', '2024.10~2025.02|蝦皮家電賣場', '$581,200', '廣告 ROAS 9.4~12.7、營收 ROAS 11.8~20.1(逐月)'),
    ('FB', '流量', '2025.01~09|網紅部落客導購', '$156,487', 'ROAS 均值 20~60|經銷商毛利門檻需 >12|網紅 IP 加持'),
    ('FB', '填表', '2025.04~09|交友聯誼 A', '$250,198', '每 100 位名單比請業務便宜|填表成本 273 元/位'),
    ('FB', '填表', '2025.04~09|交友聯誼 B', '$300,388', '每 200 位名單比請業務便宜|填表成本 160 元/位'),
    ('FB', '填表', '2025.07~09|B2B 行銷 CRM', '$31,215', '比請人還便宜|填表成本 240 元/位;總點擊 826 次、填表 130 人,提交率 15.7%'),
]
ads_inds = [   # 不列品牌名,同類合併、相鄰排列(Dan 2026-09-09)
    ('看護長照・人力仲介', '8 家看護派遣業者(北中南)+外籍人力仲介', ['Google Ads', 'SEO', '網站設計']),
    ('室內設計', '台南與高雄 兩家空間設計公司', ['Facebook Ads', 'Google Ads', '網站設計', 'SEO']),
    ('餐飲食品・食品電商', '飯店集團與自有食品品牌+冷凍食品電商+歐陸食品電商', ['Facebook Ads', 'Google Ads', '電商通路運營']),
    ('電商零售', '宗教用品電商', ['Facebook Ads', 'Google Ads']),
    ('餐飲平台・CRM 系統', '餐飲揪團平台+LINE CRM 系統商', ['Facebook Ads']),
    ('交友服務', '兩家交友聯誼平台', ['Facebook Ads']),
    ('個人品牌・服務業', '房仲業務個人品牌+健身房+音樂教學工作室+網紅經紀公司', ['Facebook Ads', '短影音']),
    ('運動時尚', '高爾夫服飾品牌', ['短影音', 'Facebook Ads']),
    ('金融・能源', '貸款理財顧問+太陽能儲能業者', ['Google Ads', 'SEO']),
]
def res_table(rows):
    tr = ''
    for pf, kind, period, amt, res in rows:
        pfs = ''.join(f'<span class="pf">{p}</span>' for p in pf.split())
        tr += f'<tr><td>{pfs}</td><td>{kind}廣告</td><td>{H.escape(period)}</td><td class="money">{amt}</td><td>{H.escape(res)}</td></tr>'
    return f'''<div class="tbl-wrap"><table class="res"><thead><tr><th>平台</th><th>廣告類型</th><th>期別|產業</th><th>投廣總額</th><th>成績</th></tr></thead><tbody>{tr}</tbody></table></div>'''
def ind_grid(items):
    return '<div class="ind-grid">' + ''.join(
        f'<div class="ind reveal"><small>{H.escape(i)}</small><b>{H.escape(n)}</b>{chips(t)}</div>' for i, n, t in items) + '</div>'

ads_cases = f'''<p class="lead">投廣成績——平台、期別、金額、結果,一列一案。</p>
{res_table(ads_results)}
<h3 style="font-size:24px;margin-top:56px">跨產業實戰紀錄</h3>
<p class="lead">服務橫跨多種產業,廣告投放 × 技術整合雙軌並行。</p>
{ind_grid(ads_inds)}'''

page('ads', '廣告投放', '丹丹', 'ADS',
     '會寫追蹤代碼的廣告投手。行銷背景出身,從追蹤埋設、廣告投放到 AI 自動化優化,一站式整合——追蹤沒埋好,所有優化都是瞎猜。',
     '簡單廣告營銷 Founder。Google / Meta 雙平台代操(15% 服務費,90% 流程自動化),廣告帳戶健檢,異常監測系統自動通報。',
     [('1,000萬+', '年度管理廣告預算 (NTD)'), ('1億+', '累計協助客戶營收 (NTD)'), ('20+', '跨產業客戶')],
     ads_steps, ads_cases, owner_img='assets/dandan.webp')

# ================= WEB (雅芬) — 內容來源:projects\BNI行銷產業鏈\雅芬\(富瑞分會 10 分鐘簡報 pptx 逐字稿 pptx_text.md + 網站設計作品集.txt + 人像,2026-09-09) =================
YF = 'assets/yafen'

def note_grid(items):  # (label, title, desc, [chips]) → 4 欄卡:小標籤/粗標題/內文/標籤
    return '<div class="ind-grid">' + ''.join(
        f'<div class="ind reveal"><small>{H.escape(l)}</small><b>{H.escape(t)}</b><p>{H.escape(d)}</p>{chips(c) if c else ""}</div>'
        for l, t, d, c in items) + '</div>'

web_after_hero = f'''
<section>
  <div class="wrap">
    <div class="eyebrow">Services</div>
    <h2 class="h2">核心服務</h2>
    <p class="lead">從零建站、舊站升級到搜尋排名——不只做出網站,更要做出能被找到、被信任、帶來詢問的品牌主場。</p>
    {vd_cards([
        ('新網站建置', 'NEW WEBSITE', ['從零開始,打造符合品牌調性的專業網站', '一頁式銷售網 / 企業形象官網 / 電商(購物車、金流)', '文案架構、RWD 版型、基礎 SEO 一次到位', '品牌色與版型與 <a href="visual.html">視覺設計</a> 同步']),
        ('舊站升級維護', 'UPGRADE & MAINTAIN', ['優化手機體驗、提升速度,全面升級網站表現', '既有平台導入視覺、突破系統限制', '表單、系統串接,接進 <a href="crm.html">LINE 會員系統</a>', '首年微調換圖,長期維護有人接']),
        ('SEO 優化', 'SEO', ['定期更新內容,提升品牌活力與搜尋排名', '被搜尋到、提高詢問與成交', '預埋 GA / GTM,<a href="ads.html">廣告投放</a>追得到每一筆轉換', '從成交開始規劃,用數據持續優化']),
    ])}
  </div>
</section>

<section style="background:#fff">
  <div class="wrap">
    <div class="eyebrow">Pain Point</div>
    <h2 class="h2">社群平台只是「租來的入口」</h2>
    <p class="lead">觸及、規則、帳號權限,都由平台決定。</p>
    {note_grid([
        ('01', '觸及率不穩定', '辛苦發文,粉絲不一定看得到。', None),
        ('02', '平台規則說變就變', '流量不穩,成本可能提高。', None),
        ('03', '帳號可能被限制', '被檢舉、誤判,都可能影響營運。', None),
        ('04', '社群是租的,官網是自己的', '別把唯一入口交給別人!', None),
    ])}
    <div class="vd-hl" style="grid-template-columns:1fr;margin-top:22px"><div class="reveal"><small>官網 × 社群 分工</small><b>「社群負責曝光,官網負責承接信任與詢問!」</b><p style="color:rgba(255,255,255,.8);font-size:15px">廣告與短影音把人帶進來,官網把信任與詢問接住——這也是五段服務裡網站排在基礎建設的原因。</p></div></div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="eyebrow">Brand Asset</div>
    <h2 class="h2">打造品牌資產,掌控成長未來</h2>
    <p class="lead">有官網的品牌 vs 僅依賴社群的品牌。</p>
    <div class="web-vs">
      <div class="vd-card reveal"><h3>有官網的品牌</h3><div class="who">BRAND ASSET</div><ul><li><b>營收穩定</b>:建立自有流量,持續成長</li><li><b>掌握會員名單</b>:累積客戶資產,精準經營</li><li>內容、SEO、名單都累積在自己的網域</li></ul></div>
      <div class="vs reveal">VS</div>
      <div class="vd-card bad reveal"><h3>僅依賴社群</h3><div class="who">RISK</div><ul><li><b>無預警停權</b>:平台規則變動,帳號隨時消失</li><li><b>客戶瞬間歸零</b>:所有客戶流量,一夕歸零</li><li>觸及、規則、權限都在別人手上</li></ul></div>
    </div>
  </div>
</section>

<section style="background:#fff">
  <div class="wrap">
    <div class="eyebrow">Why Me</div>
    <h2 class="h2">為什麼選擇雅芬?</h2>
    <p class="lead">從你的經營痛點出發,打造真正有用的網站。</p>
    {note_grid([
        ('01', '從成交開始規劃', '依照客戶需求與消費流程,打造能帶來詢問的網站。', ['消費流程', '詢問']),
        ('02', '用數據持續優化', '追蹤訪客行為與網站成效,讓每次調整都有依據。', ['GA', '成效追蹤']),
        ('03', '把流量帶回自己的主場', '擺脫只靠社群的風險,累積品牌自己的客戶與內容。', ['自有流量', '內容資產']),
        ('04', '懂設計,更懂你的生意', '從設計與業務顧問角度,協助釐清問題、提升成交機會。', ['設計', '業務顧問']),
    ])}
  </div>
</section>
'''

web_sites = [   # 網站設計作品集.txt:不同產業的成交型官網範本(可以修改)
    ('site01', '形象官網設計', '一頁式形象官網', 'https://onepage01.senxuorii.com/'),
    ('site02', '企業官網', '一頁式企業官網', 'https://onepage02.senxuorii.com/'),
    ('site04', '餐飲品牌官網', '一頁式餐飲品牌', 'https://onepage04.senxuorii.com/'),
    ('site05', '宮廟網站設計', '一頁式宮廟官網', 'https://onepage05.senxuorii.com/'),
    ('site06', '工程網站設計', '一頁式工程公司', 'https://onepage06.senxuorii.com/'),
    ('site07', '空間設計官網', '品牌型多頁官網', 'https://brandedwebsite02.senxuorii.com/'),
]
web_cases = f'''<p class="lead">不同產業的成交型官網範本——每一套都能直接改成你的官網。點開看桌機與手機版。</p>
<div class="web-gallery">{''.join(f'<a class="reveal" href="{u}" target="_blank" rel="noopener"><div class="shot"><img class="d" src="{YF}/{k}-d.webp" alt="{H.escape(t)} 桌機版" loading="lazy"><img class="m" src="{YF}/{k}-m.webp" alt="{H.escape(t)} 手機版" loading="lazy"></div><div class="cap"><div><b>{H.escape(t)}</b><span>{H.escape(d)}</span></div><i>開啟範本 ↗</i></div></a>' for k, t, d, u in web_sites)}</div>
<h3 style="font-size:24px;margin-top:56px">已交付作品</h3>
<p class="lead">客戶一律以產業描述呈現。</p>
{vd_aud([
    ('醫美診所', '多頁官網+活動頁', ['12 項服務選單', '活動價目頁', '海外服務專區']),
    ('手作蛋糕・花藝', 'IG 官方帳號 自動回覆選單', ['客製訂購', '作品集', '創業課程']),
    ('行李箱品牌', '雙品牌官網+電商', ['品牌官網', '電商', '一頁式']),
])}'''

web_extra = f'''
<section>
  <div class="wrap">
    <div class="eyebrow">Online × Offline</div>
    <h2 class="h2">線上與線下的視覺延伸與落地</h2>
    <p class="lead">網站、社群、印刷、包裝,讓視覺一致延伸到每個接觸點;印刷與包裝由 <a href="visual.html" style="text-decoration:underline">豐澤的視覺設計</a> 接手,同一套視覺 100% 延伸。</p>
    {note_grid([
        ('線上', '一站式服務', '省時省力:官網與社群視覺同一個窗口。', ['官網', '社群視覺']),
        ('線上 → 線下', '視覺延伸', '應用更一致:印刷物、包裝、菜單同一套。', ['印刷物', '包裝', '菜單']),
        ('協作', '減少溝通成本', '專注核心業務,不用在多個廠商之間傳話。', ['單一窗口']),
        ('落地', '設計有效落地', '提升整體質感,線上線下每個接觸點一致。', ['線上', '線下']),
    ])}
  </div>
</section>

<section style="background:#fff">
  <div class="wrap">
    <div class="eyebrow">AI Website Builder</div>
    <h2 class="h2">AI 10 秒架站?做得快 ≠ 做得對</h2>
    <p class="lead">AI 能快速產出,但不代表方向正確、流程完整。</p>
    <div class="vd-grid3">
      <div class="vd-card reveal"><h3>定位是否正確</h3><p>產出容易,判斷困難。</p></div>
      <div class="vd-card reveal"><h3>流程是否完整</h3><p>能夠上線,不等於能成交。</p></div>
      <div class="vd-card reveal"><h3>維護是否容易</h3><p>單次修改容易,長期維護仍需規劃。</p></div>
    </div>
    <div class="web-vs">
      <div class="vd-card bad reveal"><h3>自己用 AI 建站的盲點</h3><div class="who">DIY</div><ul><li>套版快速,品牌卻容易千篇一律</li><li>只有畫面,缺少 SEO 與轉換策略</li><li>功能串接、資安與法規容易踩雷</li><li>上線之後,測試維護都要自己來</li><li>上傳公司機密,資料去向難掌握</li></ul><div class="fit">看似省下建站費,卻可能錯失客戶與商機</div></div>
      <div class="vs reveal">VS</div>
      <div class="vd-card reveal"><h3>什麼情況該找專業做</h3><div class="who">PRO</div><ul><li>需要品牌形象與高信任感</li><li>需要被搜尋到、提高詢問與成交</li><li>需要特殊功能、表單或系統串接</li><li>沒時間自己反覆測試與長期維護</li></ul><div class="fit"><b>建議交給專業</b> 品牌型、成長型、商業導向網站</div></div>
    </div>
    <div class="vd-hl" style="grid-template-columns:1fr;margin-top:22px"><div class="reveal"><small>AI 與專業的分工</small><b>「AI 是效率工具,專業的價值在於判斷、整合與長期維護。」</b></div></div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="eyebrow">Take Action</div>
    <h2 class="h2">立即行動</h2>
    <p class="lead">別再觀望,現在就為品牌建立自己的數位總部。</p>
    {steps_html([
        ('評估現況', '有無官網?效能如何?是否過度依賴社群?', ['現況盤點']),
        ('免費諮詢', '分析現況、找出問題,提供適合的解決方案。', ['免費診斷']),
        ('開始行動', '不要再等,風險每天都在累積。', ['上線']),
    ])}
    <p class="lead" style="margin-top:26px">現在開始,讓官網成為你的品牌資產。 <a class="btn btn-gold" href="#contact" style="margin-left:10px">預約免費診斷 →</a></p>
  </div>
</section>
'''

page('web', '網站建置', '雅芬', 'WEBSITE',
     '社群風暴來襲,官網才是你的品牌主場。社群負責曝光,官網負責承接信任與詢問——一頁式銷售網、企業形象官網到完整電商,網站是五段服務的基礎建設,有了它,廣告與短影音導進來的人才有地方落腳。',
     '森序 Orii 設計所 創辦人,設計產業年資約 9 年。新網站建置 / 舊站升級維護 / SEO 優化;從成交開始規劃、用數據持續優化,懂設計,更懂你的生意。',
     [('約 9 年', '設計產業年資'), ('1.5–8 萬', '網站方案價格帶'), ('6 種', '產業官網範本')],
     [
         ('需求對焦與方案選型', '一頁式(純單頁上下滾動、錨點導覽)、企業形象(4–5 頁,可加後台)或電商(購物車/金流)——依目標與預算選對型,不做多餘的頁。', ['一頁式', '企業形象', '電商']),
         ('文案與架構(面談一)', '第一次面談定文案:首頁/產品特色/客戶見證/常見問題/立即購買 8 段落規劃,文字定稿再進設計。', ['8 段落', '文案定稿']),
         ('視覺設計與版型(面談二)', '套用品牌色與版型(與視覺設計同步),AI 輔助素材降低工時,「量化大於完美」快速上線。', ['RWD', 'AI 輔助設計']),
         ('基礎 SEO 與追蹤埋設', '基礎 SEO 設定、首年網域;搭配廣告時預埋 GA / GTM,讓後段投放能追到每一筆轉換。', ['SEO', 'GA / GTM']),
         ('上線與維護', '含首年 1–2 次微調換圖;後台權限、購物車、多語系等模組可另外加購。', ['維護', '模組加購']),
     ],
     web_cases, owner_img='assets/yafen.webp', after_hero=web_after_hero, extra_html=web_extra)

# ================= CRM (可芳) =================
page('crm', 'LINE 會員系統', '可芳', 'CRM',
     '把來過的客人留下來。會員管理、表單問卷、微網頁到點數/優惠券自動行銷——廣告導進來的每個人都留在你的私域池。',
     'LINE 會員系統分級(入門/進階/總店 POS 整合)、AI 客服、政府「韌性計畫」補助申請協助(50% 匹配撥款,最高 10 萬)。',
     [('17,000/年', '入門版起'), ('50%', '政府補助最高比例'), ('3 檔', '行銷策略建議')],
     [
         ('現況盤點與分級選型', '入門(資料收集)/進階(會員等級)/總店 POS 整合版——依門市數與經營方式選型,綁一年合約所以第一步就選對。', ['入門', '進階', 'POS 整合']),
         ('會員池建置與自動貼標', '會員管理、表單問卷、微網頁;網站表單直接進 LINE 自動貼標,後續才能分眾。', ['自動貼標', '微網頁', '表單']),
         ('行銷工具上線', '優惠券、點數、生日禮券自動行銷、裂變分享工具;搭配 3 檔行銷策略建議排檔期。', ['優惠券', '點數', '裂變']),
         ('補助申請(可選)', '協助具企劃之企業申請韌性計畫:專案 20 萬政府最高補助 10 萬,需通過 3 個月流量與系統使用審計。', ['韌性計畫', '50% 匹配']),
         ('數據分析與分眾優化', '會員行為分析標籤、消費數據分析、自動化分眾問卷,回饋給廣告端做再行銷。', ['分眾', '再行銷']),
     ],
     '<p class="lead">已建置的 LINE 會員系統案例。</p>' + ind_grid([
         ('連鎖門市', '(案例待補)', ['會員分級', '集點']),
         ('美業', '(案例待補)', ['預約', '優惠券']),
         ('教育', '教育機構(追蹤中)', ['學員點數']),
         ('補助案', '(案例待補)', ['韌性計畫']),
     ]),
     ('待可芳補件', '系統後台/LINE 畫面截圖、客戶名稱、方案級別、可公開數據(會員數/回購率/優惠券核銷率)。'))

# ================= VIDEO (David) — 內容來源:projects\BNI行銷產業鏈\David\牛排行銷-David.pdf(2026-09-09) =================
VD = 'assets/david'

video_after_hero = f'''
<section>
  <div class="wrap">
    <div class="eyebrow">Services</div>
    <h2 class="h2">我們的服務</h2>
    <p class="lead">短影音製作、課程包班、帳號矩陣——從一支影片到一整套影音行銷。</p>
    {vd_cards([
        ('短影音製作', 'IG / TikTok / Shorts', ['IG、TikTok 短影音製作(初階 / 進階)', '個人、公司 IP 打造', '短影音品牌商品廣告', '企業形象影片', '藏鏡人真人拍攝+AI 口播複製人']),
        ('課程與包班', '把方法留在你公司', ['企業短影音行銷包班', '明星課程', '商品形象拍攝課程', '動態影像課程', '3V 商業變現學院 公益課程']),
        ('品牌網路行銷', '帳號從 0 到矩陣', ['短影音帳號建置', '圖文 AI 矩陣行銷', 'KOL 合作', '廣告投放 → <a href="ads.html">丹丹|廣告投放</a>', '會員系統 → <a href="crm.html">可芳|LINE 會員</a>']),
    ])}
  </div>
</section>

<section style="background:#fff">
  <div class="wrap">
    <div class="eyebrow">Who It's For</div>
    <h2 class="h2">如果,你想打造個人 IP+影音曝光</h2>
    <p class="lead">三種目標,三種拍法——先確定你要的是知名度、曝光,還是業績。</p>
    {vd_aud([
        ('業務銷售', '目標:提升知名度', ['房仲', '店長', '理財投資顧問', '直銷高階主管', '企業管理顧問', '連鎖店企業總部', '中古車商', '融資貸款', '醫美整型業']),
        ('個人執業', '目標:行銷曝光', ['美容師', '美髮師', '刺青師', '營養師', '塔羅師', '中醫師', '商標律師', '行銷講師', '室內設計師']),
        ('零售電商', '目標:增加業績', ['保健食品業', '通訊業店家', '3C 維修商家', '美妝電商', '食品電商', '韓國代購商', '母嬰用品電商', '寵物用品電商']),
    ])}
  </div>
</section>
'''

video_steps = [
    ('IP 設定', '卡內基價值卡測驗、曼陀羅 IP 定位分析、訪談式人物分析總結——先確定你是誰、要對誰說話。', ['2~5 天', 'IP 定位']),
    ('企劃', '拍攝主體規劃、腳本及文案擬定、確認專案成本與拍攝時間。', ['3~4 週', '腳本文案']),
    ('拍攝', '器材架設、行前溝通、拍攝進行、確認檔案及收音;單趟拍攝 8 支以上。', ['依方案', '單趟 8 支+']),
    ('編製', '影片剪輯、確認檔案及收音;真人拍攝或 AI 口播複製人皆可產出,高層不願露臉也能 24 小時曝光。', ['10 天', '剪輯', 'AI 分身']),
    ('文案', '標題封面、文字配樂、風向長尾關鍵字,確稿發佈。', ['2 天', '標題封面']),
    ('優化', '關鍵數字指標、數據分析、頻道優化;有觀看沒詢問就換下一支,素材同步交給廣告端投放。', ['2 天', '數據優化']),
]

video_hl = [
    ('手機維修達人', '12 支破百萬流量', ['每月變現 +80%', 'IG 總流量破 3,500 萬']),
    ('琉球達人', '成功轉型,民宿電話接不停', ['IG 總流量破 800 萬']),
    ('刺青工作室', '14 支破 50 萬流量', ['自有商品商模開發', 'IG 總流量破 4,000 萬']),
]
video_wall = [
    ('v04b', '年關將至,各位小心年獸'), ('v08', '逛好市多的秘密:標籤暗號大全'), ('v09', 'AirPods 還有這麼多功能'), ('v03', '肉整盤煮?退冰涮才嫩口'), ('v07b', '去日本退稅必看:2026 最新規定'),
    ('v02', '大統百貨正式拆除,高雄人的共同回憶'), ('v04a', '鯊魚夾的妙用,出門夾也不奇怪'), ('v05', '全台最早土地公,求財拜法公開'), ('v07a', '代購價格怎麼算?趁日幣低賺回來'), ('v06', '各種風格寫真,男人也能改造'),
]
video_inds = ['市議員形象', '保健食品品牌', '美甲教育講師', '個人品牌經營者', '連鎖不動產', '德系豪華車', '新材料科技', '燒肉餐酒館', '火鍋店', '酵素保健品', '集團企業']
video_ips = ['火鍋店', '客製西服', '老牌客製化蛋糕', '手機通訊行', '素食親子', '廣東粥', '美業課程', '生活風格 IP', '銀行', '汽車經銷', '豪華車品牌', '旗袍寫真館']

video_cases = f'''<p class="lead">代表顧客的流量與變現成績,一個帳號一個數字。</p>
<div class="vd-hl">{''.join(f'<div class="reveal"><small>{H.escape(n)}</small><b>{H.escape(h)}</b>{chips(c)}</div>' for n, h, c in video_hl)}</div>
<h3 style="font-size:24px;margin-top:56px">作品牆</h3>
<p class="lead">觀看數直接印在畫面上,不用我們多說。</p>
<div class="vd-wall">{''.join(f'<figure class="reveal"><span class="ph"><img src="{VD}/{k}.webp" alt="{H.escape(t)}" loading="lazy"></span><figcaption>{H.escape(t)}</figcaption></figure>' for k, t in video_wall)}</div>
<h3 style="font-size:24px;margin-top:56px">合作產業與代表 IP</h3>
<p class="lead">從市議員到豪華車品牌,從火鍋店到旗袍寫真館——同一套方法,不同的行業。</p>
<div class="chips vd-ips">{''.join(f'<span>{H.escape(x)}</span>' for x in video_inds + video_ips)}</div>
<h3 style="font-size:24px;margin-top:56px">團隊聯名案例</h3>
<p class="lead">短影音與廣告投放同步啟動的案子。</p>
{ind_grid([
    ('房仲個人 IP', '房仲業務個人品牌', ['120 萬觀看', '1,000 留言', '5–6% 轉化']),
    ('健康器材', '遠紅外線陶瓷溫熱器', ['短影音']),
    ('保健食品', '酵素總代理', ['短影音', '廣告素材']),
    ('運動時尚', '高爾夫服飾品牌', ['短影音', 'Facebook Ads']),
])}'''

def vd_plan(name, per, total, n, fit, pace, hot=False, lbl=None):
    return (f'<div class="plan{" hot" if hot else ""} reveal">' + (f'<span class="lbl">{lbl}</span>' if lbl else '')
            + f'<h3>{H.escape(name)}</h3><div class="who">{H.escape(pace)}</div>'
            + f'<div class="vd-price">{per}<small> 元/部</small></div><div class="who">{total} 元/套組</div>'
            + f'<ul><li>{n}</li><li>帳號教學</li><li>行銷策略建構</li></ul>'
            + f'<div class="fit"><b>適合</b> {H.escape(fit)}</div></div>')

video_extra = f'''
<section>
  <div class="wrap">
    <div class="eyebrow">Why Short Video</div>
    <h2 class="h2">為什麼那麼多人都在拍短影音?</h2>
    <p class="lead">還記得下班滑 FB、看 YouTuber 的年代嗎?現在觀眾要的是「快速」、「有趣」、「不用動腦」。</p>
    <div class="vd-formula">
      <div class="quote reveal"><p>成交 = 信任感 × 曝光度<br>業績 = 流量 × 轉換率 × 客單價 × 回購率</p><small>完全行銷:先讓人喜歡你,再談成交</small></div>
      <div class="vd-card reveal"><h3>流量的底層邏輯</h3><p>來客數不是運氣,是這幾個數字堆出來的。</p>{chips(['完播率', '留言數', '粉絲數', '私領域', '演算法', '內容價值', '觀看數', '專業 & 泛流量'])}</div>
    </div>
    <div class="vd-grid3" style="margin-top:22px">
      <div class="vd-card reveal"><h3>菜單式 vs 試吃式</h3><p>菜單式讓人選擇障礙;試吃式讓人選擇快速、符合觀眾口味。短影音就是試吃式——先讓人嚐一口。</p></div>
      <div class="vd-card reveal"><h3>公域 × 私域</h3><p>我們深知社群平台操作差異:公域拿流量,私域留人;短影音導進來的人,交給 <a href="crm.html">LINE 會員系統</a> 留住。</p></div>
      <div class="vd-card reveal"><h3>AI 複製人系統</h3><p>檔期滿、不想露臉,也能靠 AI 口播複製人維持週更;真人與 AI 混拍,產量與真實感兼顧。</p></div>
    </div>
  </div>
</section>

<section style="background:#fff">
  <div class="wrap">
    <div class="eyebrow">Plans</div>
    <h2 class="h2">短影音專案方案</h2>
    <p class="lead">走團隊 A / B / C 包套時,短影音支數依 <a href="index.html#plans" style="text-decoration:underline">總覽方案</a> 配置;以下是單獨委託短影音的參考方案。</p>
    <div class="plans">
      {vd_plan('職人好口碑方案', '5,500', '110,000', '20 支短影音企劃', '初創、初步商模建置', '每週 2 支|3 個月')}
      {vd_plan('職人超值方案(季)', '4,800', '144,000', '30 支短影音企劃', '決定改變!加快累積粉絲', '每週 2 支|4~5 個月')}
      {vd_plan('半年約超值方案', '4,400', '308,000', '70 支短影音企劃', '年度預算,價值最大化', '每週 2 支|9~12 個月', hot=True, lbl='最划算')}
    </div>
    <div class="vd-plans-note">三方案皆含:平台帳號教學 / 協助(時間、內文編輯、標題應用、封面設計)、職業與服務內容腳本。單趟拍攝 8 支以上;車程超過三民區一小時,交通費另計。</div>
    <div class="vd-grid3" style="margin-top:30px">
      <div class="vd-card reveal"><h3>顧問陪跑專案</h3><div class="who">保證產出 30 支獲客短影音</div><ul><li>量身定戰略、高效獲客路徑、快速見察變現</li><li>腳本策劃、拍攝指導、後期剪輯</li><li>數據分析、成效優化、全程陪跑</li></ul><div class="fit" style="margin-top:16px;font-size:15px"><b>費用</b> 依專案需求討論</div></div>
      <div class="vd-card reveal"><h3>3V 商業變現學院</h3><div class="who">短影音變現、超級業務力 公益課程</div><ul><li>IP 定位 → 流量 → 成交 → 變現</li><li>3 位講師傳授實戰心法</li><li>公益課程價 990 元;扣除場地與製作費後全數捐給公益團體</li></ul></div>
      <div class="vd-card reveal"><h3>企業包班 / 課程</h3><div class="who">把拍攝與剪輯能力留在公司</div><ul><li>企業短影音行銷包班</li><li>商品形象拍攝課程、動態影像課程</li><li>明星課程、個人 IP 打造</li></ul></div>
    </div>
  </div>
</section>
'''

page('video', '短影音', 'David', 'VIDEO',
     '影音行銷的專家,用影像打造你的 IP 價值。IG / TikTok 短影音製作、個人與企業 IP 打造、藏鏡人拍攝+AI 口播分身;每週固定產出,影片同時是廣告素材,有觀看沒詢問就換下一支。',
     '《影音行銷的專家,用影像打造你的 IP 價值》。IG / TikTok 短影音製作、企業短影音行銷包班、個人與公司 IP 打造;真人藏鏡人拍攝+AI 口播複製人,開幕前中後三階段陪跑。',
     [('4,000 萬+', '單一客戶 IG 累積流量'), ('12 支', '單一客戶破百萬流量影片'), ('30 支', '顧問陪跑保證產出')],
     video_steps, video_cases,
     owner_img='assets/david.webp', after_hero=video_after_hero, extra_html=video_extra)

# ================= VISUAL (豐澤) — 內容來源:projects\BNI行銷產業鏈\豐澤\豐澤.pdf + 豐澤001.jpg(2026-09-09) =================
FZ = 'assets/fengze'
visual_after_hero = f'''
<section>
  <div class="wrap">
    <div class="eyebrow">Services</div>
    <h2 class="h2">品牌廣告設計,一次做到底</h2>
    <p class="lead">決不拖稿、最省心,有行銷底的設計師——從識別到包裝、從銷售頁到社群,視覺先定調。</p>
    {vd_cards([
        ('品牌形象', 'BRAND IDENTITY', ['企業 CIS、LOGO 設計', '主視覺與品牌色彩系統', '名片、信封等識別應用', '品牌重塑再造,讓品牌持續亮眼']),
        ('產品銷售', 'SALES DESIGN', ['菜單、型錄、DM', '包裝設計(盒裝、罐裝、紙盒、軟包裝)', '銷售圖文', '導購銷售頁:保健食品 / 生活用品 / 課程 / 攝影']),
        ('專案活動', 'CAMPAIGN', ['檔期活動主視覺', '活動海報、立牌', '提案簡報設計', '社群圖文 5 / 9 款']),
        ('商業攝影', 'PHOTOGRAPHY', ['靜態商品攝影', '動態影像', '食品、餐飲、成菜照', '營造品牌氛圍,拍出吸睛好賣相']),
        ('網路社群經營', 'SOCIAL MEDIA', ['FB / IG 貼文設計與文案', '行銷廣告圖', '持續圈粉,讓好評不斷', '與 <a href="ads.html">廣告投放</a>、<a href="video.html">短影音</a> 共用同一套視覺']),
        ('導購銷售頁', 'LANDING PAGE', ['打造網路超級業務,365 天 online 熱賣', '一頁式銷售頁視覺', '與 <a href="web.html">網站建置</a> 分工:設計在這裡,上線在那裡', '廣告落地頁同步供 <a href="ads.html">投放</a>']),
    ])}
  </div>
</section>
'''

visual_gallery = [
    ('graphic', '品牌廣告設計', '包裝、名片、DM、型錄——品牌形象 / 產品銷售 / 專案活動三條線'),
    ('packaging', '品牌包裝設計', '食品、美容、生活用品的盒裝、罐裝、紙盒設計'),
    ('landing', '導購銷售頁', '保健食品、生活用品、課程銷售、攝影銷售四類 Landing Page'),
    ('photo', '商業攝影 動・靜態', '肉品、海鮮、食材、成菜照——拍出吸睛好賣相'),
    ('social', '網路社群經營', 'FB / IG 貼文設計、行銷廣告、APP 應用圖'),
]
visual_inds = ['鹽製品食品', '日系眼鏡', '純素營養品', '共享空間', '火鍋店', '保健食品', '早餐品牌', '澎湖旅宿', '不動產', '窗簾品牌', '高爾夫用品', '美業新創']

visual_cases = f'''<p class="lead">作品集直接看——每一頁都是實際交付過的設計。</p>
<div class="vd-gallery">{''.join(f'<figure class="reveal"><img src="{FZ}/{k}.webp" alt="{H.escape(t)}" loading="lazy"><figcaption><b>{H.escape(t)}</b><span>{H.escape(d)}</span></figcaption></figure>' for k, t, d in visual_gallery)}</div>
<h3 style="font-size:24px;margin-top:56px">合作產業</h3>
<p class="lead">從食品到不動產,同一套設計方法,不同的行業。</p>
<div class="chips vd-ips">{''.join(f'<span>{H.escape(x)}</span>' for x in visual_inds)}</div>
<h3 style="font-size:24px;margin-top:56px">團隊聯名案例</h3>
{ind_grid([
    ('運動用品', '高爾夫用品品牌', ['包裝設計', '國際市場']),
    ('美業', '新創美業品牌 識別重設定', ['Logo', '社群圖文']),
    ('餐飲', '餐飲品牌 檔期 DM', ['檔期 DM', '菜單']),
    ('連鎖品牌', '連鎖門市 全店視覺', ['全店視覺', '立牌']),
])}'''

visual_extra = f'''
<section>
  <div class="wrap">
    <div class="eyebrow">Why Visual First</div>
    <h2 class="h2">放大品牌聲量,展現品牌價值</h2>
    <p class="lead">視覺不是最後才補的裝飾,是整條行銷產線的第一步。</p>
    <div class="vd-grid3">
      <div class="vd-card reveal"><h3>有行銷底的設計師</h3><p>設計是為了賣,不是為了好看而已;每一張圖都先想它要在哪裡被看到、要讓人做什麼。</p></div>
      <div class="vd-card reveal"><h3>決不拖稿、最省心</h3><p>檔期就是檔期。品牌方只要確認方向,交期、印刷規格、輸出檔案全部包辦。</p></div>
      <div class="vd-card reveal"><h3>一套視覺,五段共用</h3><p>Logo、色票、版型定好後,<a href="web.html">網站</a>、<a href="video.html">影片封面</a>、<a href="ads.html">廣告圖</a>、<a href="crm.html">LINE 圖文</a>全部套同一套,不用每次重做。</p></div>
    </div>
  </div>
</section>
'''

page('visual', '視覺設計', '豐澤', 'VISUAL',
     '放大品牌聲量、展現品牌價值。品牌識別、廣告設計、包裝、導購銷售頁、商業攝影到社群經營——視覺先定調,網站、影片封面、廣告圖全部套同一套。',
     '豐澤品牌 MAX BRAND CREATIVITY & MARKETING。決不拖稿、最省心,有行銷底的設計師;企業 CIS / LOGO / 包裝 / 型錄 DM / 導購銷售頁 / 商業攝影 / 社群經營一站包辦。',
     [('35,000', 'Logo 參考價'), ('5 / 9 款', '社群圖文'), ('6 類', '設計服務')],
     [
         ('品牌訪談與定位', '面談確定設計品項與需求;新創或品牌重塑先定 Logo、配色與字型系統。', ['Logo', '色票', '字型']),
         ('視覺系統定調', '品牌色彩設定與版型規範,交給網站、短影音、廣告端統一套用。', ['品牌規範', '版型']),
         ('社群圖文與檔期物', '社群圖文 5 或 9 款、檔期海報/DM、立牌一拉桿;提供列印規格指令。', ['社群圖', 'DM', '印刷規格']),
         ('包裝與銷售頁(可選)', '包裝兩款初稿、非結構性設計,以現有盒型或軟包裝為主;導購銷售頁視覺同步產出;大圖輸出 150–200 DPI 對接印刷。', ['包裝', '銷售頁', 'DPI']),
         ('商業攝影與維護', '需要實拍時安排靜態/動態商業攝影;首年 1–2 次微調或換圖服務。', ['攝影', '維護']),
     ],
     visual_cases, owner_img='assets/fengze.webp', after_hero=visual_after_hero, extra_html=visual_extra)
