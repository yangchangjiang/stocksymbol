#!/usr/bin/env python3
"""Build StockSymbol — 8K stocks × 10 languages — FINANCE theme"""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
LANGS = ["en","zh-CN","ja","ko","es","pt","fr","de","ar","hi"]

with open(os.path.join(BASE, "stocks.json"), encoding="utf-8") as f:
    stocks = json.load(f)

# UI translations
UI = {
    "en": {"title":"Stock Symbol Directory","home":"Home","about":"About","privacy":"Privacy","search":"Search stocks...","browse":"Browse by Letter","sector":"Sector","exchange":"Exchange","symbol":"Symbol","company":"Company Name","prev":"Previous","next":"Next","all":"All","page":"Page","subscribe":"Stay informed with real-time stock data","footer":"Stock Reference Database. Data for informational purposes only."},
    "zh-CN": {"title":"股票代码查询","home":"首页","about":"关于","privacy":"隐私","search":"搜索股票代码...","browse":"按字母浏览","sector":"行业","exchange":"交易所","symbol":"代码","company":"公司名称","prev":"上一页","next":"下一页","all":"全部","page":"页","subscribe":"实时掌握股票行情","footer":"股票参考数据库。数据仅供参考。"},
    "ja": {"title":"株式コード検索","home":"ホーム","about":"概要","privacy":"プライバシー","search":"株式コードを検索...","browse":"アルファベット順","sector":"セクター","exchange":"取引所","symbol":"コード","company":"会社名","prev":"前へ","next":"次へ","all":"すべて","page":"ページ","subscribe":"リアルタイム株価情報","footer":"株式参照データベース。情報提供目的です。"},
    "ko": {"title":"주식 종목 코드","home":"홈","about":"소개","privacy":"개인정보","search":"종목 검색...","browse":"알파벳별","sector":"섹터","exchange":"거래소","symbol":"코드","company":"회사명","prev":"이전","next":"다음","all":"전체","page":"페이지","subscribe":"실시간 주식 시세","footer":"주식 참조 데이터베이스. 정보 제공 목적입니다."},
    "es": {"title":"Directorio de Símbolos Bursátiles","home":"Inicio","about":"Acerca","privacy":"Privacidad","search":"Buscar acciones...","browse":"Por Letra","sector":"Sector","exchange":"Bolsa","symbol":"Símbolo","company":"Empresa","prev":"Anterior","next":"Siguiente","all":"Todos","page":"Página","subscribe":"Mantente informado con datos en tiempo real","footer":"Base de datos de referencia bursátil. Solo informativo."},
    "pt": {"title":"Diretório de Ações","home":"Início","about":"Sobre","privacy":"Privacidade","search":"Buscar ações...","browse":"Por Letra","sector":"Setor","exchange":"Bolsa","symbol":"Símbolo","company":"Empresa","prev":"Anterior","next":"Próximo","all":"Todos","page":"Página","subscribe":"Fique informado com dados em tempo real","footer":"Base de dados de referência. Apenas informativo."},
    "fr": {"title":"Répertoire des Symboles Boursiers","home":"Accueil","about":"À propos","privacy":"Confidentialité","search":"Rechercher...","browse":"Par Lettre","sector":"Secteur","exchange":"Bourse","symbol":"Symbole","company":"Société","prev":"Précédent","next":"Suivant","all":"Tous","page":"Page","subscribe":"Restez informé en temps réel","footer":"Base de référence boursière. Information seulement."},
    "de": {"title":"Aktiensymbol-Verzeichnis","home":"Start","about":"Über uns","privacy":"Datenschutz","search":"Aktien suchen...","browse":"Nach Buchstabe","sector":"Branche","exchange":"Börse","symbol":"Symbol","company":"Unternehmen","prev":"Zurück","next":"Weiter","all":"Alle","page":"Seite","subscribe":"Aktuelle Kursdaten in Echtzeit","footer":"Aktienreferenzdatenbank. Nur zu Informationszwecken."},
    "ar": {"title":"دليل رموز الأسهم","home":"الرئيسية","about":"حول","privacy":"الخصوصية","search":"البحث عن الأسهم...","browse":"تصفح بالأحرف","sector":"القطاع","exchange":"البورصة","symbol":"الرمز","company":"الشركة","prev":"السابق","next":"التالي","all":"الكل","page":"صفحة","subscribe":"ابق على اطلاع ببيانات السوق","footer":"قاعدة بيانات مرجعية. لأغراض إعلامية فقط."},
    "hi": {"title":"स्टॉक प्रतीक निर्देशिका","home":"होम","about":"बारे में","privacy":"गोपनीयता","search":"स्टॉक खोजें...","browse":"अक्षर द्वारा","sector":"सेक्टर","exchange":"एक्सचेंज","symbol":"प्रतीक","company":"कंपनी का नाम","prev":"पिछला","next":"अगला","all":"सभी","page":"पेज","subscribe":"रीयल-टाइम बाजार डेटा","footer":"स्टॉक संदर्भ डेटाबेस। केवल सूचनात्मक उद्देश्यों के लिए।"},
}

# Stocks by first letter
by_letter = {}
for s in stocks:
    letter = s["symbol"][0].upper()
    if "A" <= letter <= "Z":
        by_letter.setdefault(letter, []).append(s)

CSS = """:root{--bg:#0a0e1a;--surface:#131a2e;--surface2:#1c2541;--text:#e2e8f0;--text2:#8892b0;--accent:#f5a623;--accent2:#34d399;--border:#1e2744}*{margin:0;padding:0;box-sizing:border-box}body{font-family:system-ui;background:var(--bg);color:var(--text);line-height:1.6}header{background:linear-gradient(135deg,#0a0e1a 0%,#131a2e 100%);border-bottom:1px solid var(--border);padding:14px 0;position:sticky;top:0;z-index:100}.container{max-width:1200px;margin:0 auto;padding:0 20px}nav{display:flex;align-items:center;gap:16px;flex-wrap:wrap}nav a{color:var(--text2);font-size:.9rem;text-decoration:none;font-weight:500}nav a:hover{color:var(--accent)}.logo{font-size:1.2rem;font-weight:700;color:var(--accent)}.search-box{width:100%;padding:14px 20px;background:var(--surface);border:2px solid var(--border);border-radius:12px;color:var(--text);font-size:1.1rem;outline:none;margin:20px 0}.search-box:focus{border-color:var(--accent)}.alpha-nav{display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin:20px 0}.alpha-nav a{width:36px;height:36px;display:flex;align-items:center;justify-content:center;background:var(--surface);border:1px solid var(--border);border-radius:8px;color:var(--text2);text-decoration:none;font-weight:600;font-size:.9rem}.alpha-nav a:hover{background:var(--accent);color:#fff;border-color:var(--accent)}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px;margin:20px 0}.card{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:16px;text-decoration:none;color:var(--text);transition:all .3s}.card:hover{transform:translateY(-2px);border-color:var(--accent);box-shadow:0 4px 20px rgba(245,166,35,.15)}.card .sym{font-size:1.1rem;font-weight:700;color:var(--accent)}.card .name{font-size:.85rem;color:var(--text2);margin-top:4px;display:block}.card .exch{font-size:.75rem;color:var(--accent2);margin-top:4px;display:block}footer{background:var(--surface);border-top:1px solid var(--border);padding:30px 0;text-align:center;color:var(--text2);font-size:.85rem;margin-top:60px}
"""

print(f"🚀 Generating {len(stocks)} stocks × {len(LANGS)} languages...")

# Generate pages per language
for lang in LANGS:
    lp = lang + "/" if lang != "en" else ""
    d = BASE if lang == "en" else os.path.join(BASE, lang)
    os.makedirs(d, exist_ok=True)
    u = UI[lang]
    
    # Index page
    buf = []
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        lst = by_letter.get(letter, [])
        if not lst: continue
        buf.append(f'<div class="letter-section" id="letter-{letter}"><h2 style="color:var(--accent);margin:24px 0 12px;font-size:1.3rem">{letter}</h2><div class="grid">')
        for s in lst[:30]:
            buf.append(f'<a href="/{lp}{s["symbol"]}.html" class="card" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'\'"><span class="sym">{s["symbol"]}</span><span class="name">{s["name"]}</span><span class="exch">{s["exchange"]}</span></a>')
        buf.append('</div></div>')
    
    index_html = f'''<!DOCTYPE html><html lang="{lang}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><meta name="description" content="{u["title"]} — {len(stocks)} stocks across NYSE and NASDAQ."><title>{u["title"]}</title><style>{CSS}</style></head><body>
<header><div class="container"><nav><a class="logo" href="/{lp}">&#x1F4C8; StockSymbol</a><a href="/{lp}">{u["home"]}</a><a href="/{lp}about.html">{u["about"]}</a><a href="/{lp}privacy.html">{u["privacy"]}</a><span style="flex:1"></span></nav></div></header>
<main class="container"><h1 style="font-size:2rem;margin:30px 0 10px;background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent">{u["title"]}</h1>
<p style="color:var(--text2);margin-bottom:20px">{len(stocks)} stocks • NYSE • NASDAQ</p>
<input type="text" class="search-box" placeholder="{u["search"]}" oninput="var q=this.value.toUpperCase();document.querySelectorAll('.grid a').forEach(function(e){e.style.display=e.textContent.includes(q)?'':'none'});document.querySelectorAll('.letter-section').forEach(function(e){e.style.display=e.querySelector('.grid a[style*=\"block\"]')?'':'none'})">
<div class="alpha-nav">'''
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if by_letter.get(letter):
            index_html += f'<a href="#letter-{letter}">{letter}</a>'
    
    index_html += '</div>' + "\n".join(buf) + '\n</main>\n'
    index_html += f'<footer><div class="container">&copy; 2026 StockSymbol. {u["footer"]} <a href="/{lp}privacy.html" style="color:var(--accent)">{u["privacy"]}</a></div></footer>\n'
    index_html += '<script>var L=["en","zh-CN","ja","ko","es","pt","fr","de","ar","hi"];function goLang(l){for(var i=0;i<L.length;i++){if(window.location.pathname.indexOf("/"+L[i]+"/")>=0){if(L[i]===l)return;if(l==="en"){window.location.href=window.location.pathname.replace("/"+L[i]+"/","/")}else{window.location.href=window.location.pathname.replace("/"+L[i]+"/","/"+l+"/")}return}}var p=window.location.pathname.split("/").filter(function(x){return x.length>0});var pg=p.join("/");if(l==="en"){window.location.href="/"+pg}else{window.location.href="/"+l+"/"+pg}}</script>\n'
    index_html += '</body></html>'
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    
    # Stock detail pages
    page_count = 0
    for s in stocks:
        sym = s["symbol"]
        name = s["name"]
        exch = s["exchange"]
        
        # Build letter navigation for this page
        nav_links = ""
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if by_letter.get(letter):
                nav_links += f'<a href="/{lp}#letter-{letter}" style="display:inline-block;width:30px;height:30px;line-height:30px;text-align:center;background:var(--surface);border:1px solid var(--border);border-radius:6px;color:var(--text2);text-decoration:none;font-size:.75rem;font-weight:600;margin:2px">{letter}</a>'
        
        detail_html = f'''<!DOCTYPE html><html lang="{lang}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><meta name="description" content="{sym} ({name}) — stock symbol listed on {exch}. View company info, sector, and exchange data."><title>{sym} ({name}) — {u["title"]}</title><style>{CSS}</style></head><body>
<header><div class="container"><nav><a class="logo" href="/{lp}">&#x1F4C8; StockSymbol</a><a href="/{lp}">{u["home"]}</a><a href="/{lp}about.html">{u["about"]}</a><a href="/{lp}privacy.html">{u["privacy"]}</a></nav></div></header>
<main class="container">
<div style="margin:20px 0"><div style="font-size:.8rem;color:var(--text2)"><a href="/{lp}" style="color:var(--accent)">{u["home"]}</a> / {sym}</div></div>
<div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:30px;margin:20px 0;text-align:center">
<h1 style="font-size:3rem;font-weight:800;color:var(--accent)">{sym}</h1>
<p style="font-size:1.2rem;color:var(--text);margin:8px 0">{name}</p>
<p style="display:inline-block;background:var(--accent2);color:#0a0e1a;padding:4px 12px;border-radius:20px;font-size:.8rem;font-weight:600">{exch}</p>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px;margin:20px 0">
<div style="background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:20px"><p style="font-size:.8rem;color:var(--text2)">{u["symbol"]}</p><p style="font-size:1.5rem;font-weight:700;color:var(--accent)">{sym}</p></div>
<div style="background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:20px"><p style="font-size:.8rem;color:var(--text2)">{u["company"]}</p><p style="font-size:1rem;color:var(--text)">{name}</p></div>
<div style="background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:20px"><p style="font-size:.8rem;color:var(--text2)">{u["exchange"]}</p><p style="font-size:1.2rem;font-weight:600;color:var(--accent2)">{exch}</p></div>
</div>
<div style="background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:20px;margin:20px 0"><h3 style="color:var(--accent);margin-bottom:12px;font-size:1rem">{u["browse"]}</h3><div style="display:flex;flex-wrap:wrap;gap:4px">{nav_links}</div></div>
</main>
<footer><div class="container">&copy; 2026 StockSymbol. {u["footer"]} <a href="/{lp}privacy.html" style="color:var(--accent)">{u["privacy"]}</a></div></footer>
<script>var L=["en","zh-CN","ja","ko","es","pt","fr","de","ar","hi"];function goLang(l){{for(var i=0;i<L.length;i++){{if(window.location.pathname.indexOf("/"+L[i]+"/")>=0){{if(L[i]===l)return;if(l==="en"){{window.location.href=window.location.pathname.replace("/"+L[i]+"/","/")}}else{{window.location.href=window.location.pathname.replace("/"+L[i]+"/","/"+l+"/")}}return}}}}var p=window.location.pathname.split("/").filter(function(x){{return x.length>0}});var pg=p.join("/");if(l==="en"){{window.location.href="/"+pg}}else{{window.location.href="/"+l+"/"+pg}}}}</script>
</body></html>'''
        with open(os.path.join(d, f"{sym}.html"), "w", encoding="utf-8") as f:
            f.write(detail_html)
        page_count += 1
    
    print(f"  {lang}: {page_count} stock pages + index")

# Sitemap
sitemap_urls = []
for lang in LANGS:
    lp = lang + "/" if lang != "en" else ""
    sitemap_urls.append(f"https://stocksymbol.top/{lp}")
    for s in stocks:
        sitemap_urls.append(f"https://stocksymbol.top/{lp}{s['symbol']}.html")
    sitemap_urls.append(f"https://stocksymbol.top/{lp}about.html")
    sitemap_urls.append(f"https://stocksymbol.top/{lp}privacy.html")

sitemap = '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
for url in sitemap_urls:
    sitemap += f"<url><loc>{url}</loc></url>"
sitemap += "</urlset>"
with open(os.path.join(BASE, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap)

# ads.txt
with open(os.path.join(BASE, "ads.txt"), "w") as f:
    f.write("google.com, pub-4047761093600857, DIRECT, f08c47fec0942fa0")

print(f"\n✅ Total: {len(stocks)} stocks × {len(LANGS)} languages = {len(stocks) * len(LANGS)} stock detail pages")
print(f"   Sitemap: {len(sitemap_urls)} URLs")
