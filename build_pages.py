# -*- coding: utf-8 -*-
"""Generate the 5 service sub-pages from data. Run: python build_pages.py"""
import html as H

NAV = '''<header>
  <div class="wrap nav">
    <a class="logo" href="index.html"><img src="assets/logo.webp" alt="牛排行銷 BULL MARKETING"></a>
    <ul id="menu">
      <li><a href="index.html#services">五大服務</a></li>
      <li><a href="web.html">網站</a></li>
      <li><a href="crm.html">LINE 會員</a></li>
      <li><a href="visual.html">視覺</a></li>
      <li><a href="video.html">短影音</a></li>
      <li><a href="ads.html">廣告</a></li>
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

def other_links(key):
    return '<div class="other-svc">' + ''.join(
        f'<a href="{k}.html">{n}<span>→</span></a>' for k, n, _, _ in ALL if k != key) + '</div>'

def page(key, name, owner, tag, hero_sub, owner_desc, stats, steps, cases_html, todo=None):
    stats_html = ''.join(f'<div><b>{H.escape(v)}</b><span>{H.escape(l)}</span></div>' for v, l in stats)
    doc = f'''<!DOCTYPE html>
<html lang="zh-Hant-TW">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name}|牛排行銷 BULL MARKETING</title>
<meta name="description" content="牛排行銷 {name} 服務流程與實際案例。">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&family=Noto+Serif+TC:wght@600;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
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
        <div class="av">{owner[0]}</div>
        <div><b>{owner}</b><small>{tag} LEAD</small><p>{owner_desc}</p></div>
      </div>
    </div>
  </div>
</section>

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
    ('FB', '綜合型', '2025.08|宗教用品電商', '$77,340', '營收 30%'),
    ('FB', '填表', '2025.07~09|B2B 行銷 CRM', '$31,215', '比請人還便宜|填表成本 240 元/位;總點擊 826 次、填表 130 人,提交率 15.7%'),
    ('FB', '填表', '2025.04~09|交友聯誼 B', '$300,388', '每 200 位名單比請業務便宜|填表成本 160 元/位'),
    ('FB', '填表', '2025.04~09|交友聯誼 A', '$250,198', '每 100 位名單比請業務便宜|填表成本 273 元/位'),
    ('FB Google', '綜合型', '2025.04~09|餐飲實業', '$164,884', '網站人流成長 40 倍(1,500 → 60,000 人/半年)|網站新客成長 25 倍(800 → 20,000 人/半年)'),
    ('FB', '綜合型', '2025.03~05|冷凍食品電商', '$377,000', '3 月底 ROAS <3 拉升至 >4.5|4 月 ROAS 6.5|5 月 ROAS 7.1'),
    ('FB', '流量', '2025.01~09|網紅部落客導購', '$156,487', 'ROAS 均值 20~60|經銷商毛利門檻需 >12|網紅 IP 加持'),
    ('蝦皮', '流量', '2024.10~2025.02|蝦皮家電賣場', '$581,200', '廣告 ROAS 9.4~12.7、營收 ROAS 11.8~20.1(逐月)'),
    ('FB', '綜合型', '2022~2023|保健食品', '$14,400,000', '一半占比顯示標籤為成效出色,轉換 ROAS 約 2.5~3.5'),
    ('Google', '綜合型', '2022~2023|保健食品', '$3,600,000', '純 Ads 轉換 ROAS 2.5,實際轉換 ROAS 約 3~3.5'),
]
ads_inds = [
    ('看護長照', '順心 / 恆愛 / 優善 / 晴美 / 仁安 / 力威 / 久伴 / 長安', ['Google Ads', 'SEO', '網站設計']),
    ('室內設計', '萬寶隆空間設計', ['Facebook Ads', 'Google Ads']),
    ('餐飲食品', '全國麗園 尋鮮坊', ['Facebook Ads', 'Google Ads']),
    ('餐飲飯店', '全國麗園', ['電商通路運營', 'Google Ads']),
    ('餐飲聯盟平台', 'JTK 揪攤集', ['Facebook Ads']),
    ('裂變行銷系統', 'Mecango LINE CRM 系統', ['Facebook Ads']),
    ('運動時尚', 'Avant-Golf 雅凡高爾夫', ['短影音', 'Facebook Ads']),
    ('個人 IP 行銷', '郁婷房仲', ['Facebook Ads']),
    ('健身產業', '麋鹿健身', ['Facebook Ads']),
    ('交友服務', '圈出新戀情 / 心跳配對 MatchUp', ['Facebook Ads']),
    ('電商零售', '財神小舖', ['Facebook Ads', 'Google Ads']),
    ('電商零售', 'KUDONG 酷凍', ['Facebook Ads', 'Google Ads']),
    ('電商零售', '三劍客歐陸嚴選', ['Facebook Ads']),
    ('金融貸款', '玥鋒理財', ['Google Ads']),
    ('太陽能儲能', '築能太陽能', ['Google Ads', 'SEO']),
    ('音樂工作室', '悉尼音樂工作室', ['Facebook Ads']),
    ('網紅經紀', '55GO', ['Facebook Ads']),
    ('人力仲介', '中豪人力仲介', ['SEO', '網站設計']),
    ('室內設計', '品家設計', ['網站設計', 'SEO']),
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
     ads_steps, ads_cases)

# ================= WEB (雅芬) =================
page('web', '網站建置', '雅芬', 'WEBSITE',
     '一頁式銷售網、企業形象官網到完整電商——網站是漏斗最前端的基礎建設,品牌定調後必須先有網站,後續投廣告才有意義。',
     '網頁開發與電商建設。一頁式(A)/品牌網含 CMS(B)/完整電商含金流(C);協助既有平台導入視覺並優化系統限制。',
     [('3', '種網站方案'), ('1.5–8 萬', '價格帶'), ('3 次', '修改次數上限')],
     [
         ('需求對焦與方案選型', '一頁式(純單頁上下滾動、錨點導覽)、企業形象(4–5 頁,可加後台)或電商(購物車/金流)——先依目標與預算選對型,不做多餘的頁。', ['一頁式', '企業形象', '電商']),
         ('文案與架構(面談一)', '第一次面談定文案:首頁/產品特色/客戶見證/常見問題/立即購買 8 段落規劃,文字先過再進設計。', ['8 段落', '文案定稿']),
         ('視覺設計與版型(面談二)', '套用品牌色與版型(與視覺設計同步),AI 輔助素材降低工時,「量化大於完美」快速上線。', ['RWD', 'AI 輔助設計']),
         ('基礎 SEO 與追蹤埋設', '基礎 SEO 設定、首年網域;搭配廣告時預埋 GA / GTM,讓後段投放能追到每一筆轉換。', ['SEO', 'GA / GTM']),
         ('上線與維護', '含首年 1–2 次微調換圖;後台權限、購物車、多語系等模組可另外加購。', ['維護', '模組加購']),
     ],
     '<p class="lead">已交付的網站與電商作品。</p>' + ind_grid([
         ('行李箱品牌', 'Lucky Lucky / M Case', ['品牌官網', '電商']),
         ('餐飲', '(案例待補)', ['一頁式']),
         ('形象網站', '(案例待補)', ['企業形象', '後台']),
         ('平台轉型', '(案例待補)', ['既有平台優化']),
     ]),
     ('待雅芬補件', '作品截圖(桌機+手機)、客戶名稱、方案類型、可公開的成效(上線後流量/詢問數)。每案一組:圖 1 張 + 一句話 + 3 個標籤。'))

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
         ('教育', '三代同行(追蹤中)', ['學員點數']),
         ('補助案', '(案例待補)', ['韌性計畫']),
     ]),
     ('待可芳補件', '系統後台/LINE 畫面截圖、客戶名稱、方案級別、可公開數據(會員數/回購率/優惠券核銷率)。'))

# ================= VISUAL (豐澤) =================
page('visual', '視覺設計', '豐澤', 'VISUAL',
     '視覺先定調,後面全部一致。品牌識別、社群圖文、檔期 DM 到商品包裝——網站、影片封面、廣告圖全部套同一套。',
     '品牌設計與包裝。Logo(含中英文字型設定+色彩規劃)、社群圖文 5/9 款、檔期 DM/文宣/立牌、非結構性包裝設計。',
     [('35,000', 'Logo 參考價'), ('5 / 9 款', '社群圖文'), ('2 款', '包裝初稿')],
     [
         ('品牌訪談與定位', '面談確定設計品項與需求;新創或品牌重塑先定 Logo、配色與字型系統。', ['Logo', '色票', '字型']),
         ('視覺系統定調', '品牌色彩設定與版型規範,交給網站、短影音、廣告端統一套用。', ['品牌規範', '版型']),
         ('社群圖文與檔期物', '社群圖文 5 或 9 款、檔期海報/DM、立牌一拉桿;提供列印規格指令。', ['社群圖', 'DM', '印刷規格']),
         ('包裝設計(可選)', '兩款初稿、非結構性設計,以現有盒型或軟包裝為主;大圖輸出 150–200 DPI 對接印刷。', ['包裝', 'DPI']),
         ('維護與換圖', '首年 1–2 次微調或換圖服務。', ['維護']),
     ],
     '<p class="lead">品牌識別與包裝作品。</p>' + ind_grid([
         ('運動用品', '歐米斯 Omis 高爾夫', ['包裝設計', '國際市場']),
         ('美業', '新創美業品牌 識別重設定', ['Logo', '社群圖文']),
         ('餐飲', '(案例待補)', ['檔期 DM']),
         ('連鎖品牌', '(案例待補)', ['全店視覺']),
     ]),
     ('待豐澤補件', '作品圖(Logo/包裝/社群圖各 1–2 張)、客戶名稱、設計品項標籤。'))

# ================= VIDEO (David) =================
page('video', '短影音', 'David', 'VIDEO',
     '每週 1 支的固定節奏,搭配 AI 口播分身與真人拍攝;影片同時是廣告素材,不孤軍奮戰——有觀看沒詢問就換下一支。',
     'AI 短影音與線上課程。藏鏡人短影音+AI 口播複製人、AI 虛擬分身訓練、線上課程錄製與上架;開幕前中後三階段陪跑。',
     [('4 支/月', '固定產出'), ('60 支', '演算法臨界點'), ('3 單元', '線上課程方案')],
     [
         ('定位與受眾節奏', '先定觀眾是誰、在意什麼;40 歲以上受眾節奏放慢、字幕吸收率優先,避免防禦心理。', ['受眾', '節奏']),
         ('鉤子與腳本', 'AI 輔助文案發想:好奇心開場、資訊不對稱誘發留言;每幕精簡不推銷。', ['鉤子', 'AI 文案']),
         ('拍攝與 AI 分身', '藏鏡人真人拍攝+AI 口播複製人;高層不願露臉或檔期滿,用數位分身 24 小時曝光。', ['真人拍攝', 'AI 分身']),
         ('週更與素材陪跑', '每週 1 支、每月 4 支;開幕前/中/後三階段素材,同步交給廣告端投放。', ['週更', '三階段']),
         ('留言自動化與名單', 'ManyChat / 內部系統自動回覆大量留言,導流表單收預算與意向,轉化率 5–6%。', ['自動回覆', '名單表單']),
     ],
     '<p class="lead">短影音與線上課程作品。</p>' + ind_grid([
         ('房仲個人 IP', '郁婷房仲', ['120 萬觀看', '1,000 留言', '5–6% 轉化']),
         ('健康器材', '遠紅外線陶瓷溫熱器', ['短影音']),
         ('保健食品', '酵素總代理', ['短影音', '廣告素材']),
         ('線上課程', '(案例待補)', ['3 單元錄製']),
     ]),
     ('待 David 補件', '影片連結或封面截圖、客戶名稱、觀看/留言/詢問數(可公開者)。'))
