#!/usr/bin/env python3
"""Stay Easy Tanzania site: index, vacations, transport, cargo (v2: photos, original colours, short copy)."""
from pathlib import Path

import os, sys
OUT = Path(os.environ.get("OUT", Path(__file__).resolve().parent.parent))
STANDALONE = os.environ.get("STANDALONE") == "1"  # full HTML docs for GitHub Pages
PHONE, PHONE_RAW, EMAIL = "+255 779 125 938", "255779125938", "info@stayeasytz.com"
RATE = 2641  # TZS per USD, 30 Oct 2026; prices rounded to nearest 1,000

TSH_OVERRIDE = {30: "80,000"}  # Rumion set by owner

def tsh(usd):
    return TSH_OVERRIDE.get(usd) or f"{round(usd * RATE / 1000) * 1000:,}"

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800'
         '&family=Figtree:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap">')

CSS = r"""
/* Layout concept: a transit map in the brand's own blues. Each service is a line
   (cyan vacations, blue transport, navy cargo); every page runs its line down the
   left edge and each section is a stop. Light-only by choice, matching the original site. */
:root{
  --bg:#ffffff; --soft:#eef8fc; --ink:#2c2521; --muted:#5d6b75; --rule:#dbe9f0;
  --cyan:#13c8ec; --cyan2:#30d9e8; --blue:#2563eb; --navy:#0459ae; --teal:#0a9cb4;
  --line:var(--teal); --on-line:#ffffff;
  --display:"Bricolage Grotesque","Arial Narrow",system-ui,sans-serif;
  --body:"Figtree",system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono:"JetBrains Mono",ui-monospace,Menlo,monospace;
  --wrap:1200px; color-scheme:light;
}
body.v{--line:var(--cyan)} body.t{--line:var(--blue)} body.c{--line:var(--navy)}
*{box-sizing:border-box}
[hidden]{display:none!important}
body{margin:0;background:var(--bg);color:var(--ink);font:400 16px/1.55 var(--body);-webkit-font-smoothing:antialiased}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--bg)}
a{color:inherit}
img{max-width:100%;display:block}
h1,h2,h3{font-family:var(--display);line-height:1.02;margin:0;text-wrap:balance;letter-spacing:-.02em}
h1{font-size:clamp(2.6rem,6.4vw,5.4rem);font-weight:800}
h2{font-size:clamp(1.6rem,3vw,2.3rem);font-weight:800}
h3{font-size:1.12rem;font-weight:600;letter-spacing:-.005em}
p{margin:0}
.wrap{max-width:var(--wrap);margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
.label{font:500 .72rem/1 var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
:focus-visible{outline:3px solid var(--line);outline-offset:3px;border-radius:4px}

/* header */
.top{position:sticky;top:env(safe-area-inset-top,0px);z-index:9;background:rgba(255,255,255,.94);backdrop-filter:blur(10px);border-bottom:1px solid var(--rule)}
.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:14px;padding-block:10px}
.brand img{height:40px;width:auto}
nav{display:flex;gap:4px;flex-wrap:wrap;justify-content:flex-end;align-items:center}
nav a{display:inline-flex;align-items:center;gap:7px;text-decoration:none;font-weight:600;font-size:.94rem;padding:8px 12px;border-radius:999px}
nav a:hover{background:var(--soft)}
nav a[aria-current="page"]{background:var(--soft)}
.dot{width:10px;height:10px;border-radius:50%;flex:none}
.dot.v{background:var(--cyan)} .dot.t{background:var(--blue)} .dot.c{background:var(--navy)}
nav .cta{background:var(--blue);color:#fff;margin-left:4px} nav .cta:hover{background:var(--navy)}
@media (max-width:720px){.brand img{height:32px} nav a .txt{display:none} nav a{padding:9px} nav .cta{padding:8px 13px}}

/* buttons */
.btns{display:flex;flex-wrap:wrap;gap:10px}
.btn{display:inline-flex;align-items:center;gap:8px;padding:13px 20px;border-radius:999px;text-decoration:none;border:2px solid transparent;cursor:pointer;font:700 .98rem/1 var(--body);background:var(--blue);color:#fff}
.btn:hover{background:var(--navy)}
.btn.glass{background:rgba(255,255,255,.16);border-color:rgba(255,255,255,.7);color:#fff;backdrop-filter:blur(6px)}
.btn.glass:hover{background:rgba(255,255,255,.28)}
.btn.ghost{background:transparent;border-color:var(--ink);color:var(--ink)} .btn.ghost:hover{background:var(--soft)}
.btn.wa{background:#1fa855} .btn.wa:hover{background:#178a45}

/* photo hero */
.hero{position:relative;color:#fff;isolation:isolate;overflow:hidden;background:var(--navy)}
.hero>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-2}
.hero::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,rgba(4,30,60,.78) 0%,rgba(4,30,60,.45) 45%,rgba(4,30,60,.05) 80%)}
.hero .wrap{min-height:clamp(380px,58vh,560px);display:grid;align-content:end;gap:16px;padding-block:48px 44px}
.hero .lede{font-size:1.15rem;max-width:34ch;opacity:.95}
.hero h1 em{font-style:normal;color:var(--cyan2)}
.linebadge{display:inline-flex;align-items:center;gap:8px;font:500 .74rem/1 var(--mono);letter-spacing:.12em;text-transform:uppercase;background:var(--line);color:var(--on-line);padding:8px 13px 8px 10px;border-radius:999px;justify-self:start}
.linebadge i{width:8px;height:8px;border-radius:50%;background:#fff}
body.v .linebadge{color:#06303b} body.v .linebadge i{background:#06303b}

/* home: three line panels */
.home-hero{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));min-height:clamp(520px,80vh,760px)}
.panel{--line:var(--teal);position:relative;isolation:isolate;overflow:hidden;color:#fff;text-decoration:none;display:grid;align-content:end;padding:28px 26px 30px;gap:10px}
.panel.v{--line:var(--cyan)} .panel.t{--line:var(--blue)} .panel.c{--line:var(--navy)}
.slides{position:absolute;inset:0;z-index:-2;overflow:hidden}
.slides img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transform:translateX(100%);transition:transform 2s cubic-bezier(.65,0,.35,1)}
.slides img.on{transform:translateX(0)} .slides img.off{transform:translateX(-100%)}
.slides img.snap{transition:none}
.slides img:first-child{transform:translateX(0)}
.slides.ready img:first-child:not(.on):not(.off){transform:translateX(100%)} .slides.ready img.off{transform:translateX(-100%)}
.panel::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(0deg,rgba(4,25,50,.86) 0%,rgba(4,25,50,.2) 50%,rgba(4,25,50,0) 66%,rgba(4,25,50,.55) 100%)}
@media (max-width:820px){.panel::after{background:linear-gradient(0deg,rgba(4,25,50,.86) 0%,rgba(4,25,50,0) 75%)}}
.panel::before{content:"";position:absolute;left:0;right:0;bottom:0;height:8px;background:var(--line)}
.panel h2{font-size:clamp(1.8rem,3.2vw,2.8rem)}
.panel .go{font-weight:700;display:inline-flex;gap:8px;align-items:center}
.panel .go i{font-style:normal;transition:transform .2s}
@media (prefers-reduced-motion:no-preference){.panel:hover .go i{transform:translateX(4px)}}
.home-title{position:absolute;inset:0 0 auto;pointer-events:none;z-index:2}
.home-title .wrap{padding-block:34px 0}
.home-title h1{color:#fff;font-size:clamp(2.6rem,6.2vw,5.2rem);text-shadow:0 2px 24px rgba(0,0,0,.35)}
.home-title p{color:#fff;font-weight:600;margin-top:10px;text-shadow:0 1px 10px rgba(0,0,0,.5)}
.home-wrap{position:relative}
@media (max-width:820px){.home-hero{grid-template-columns:1fr;min-height:0} .panel{min-height:230px} .home-title{position:static} .home-title .wrap{padding-block:28px 18px} .home-title h1{color:var(--ink);text-shadow:none} .home-title p{color:var(--muted);text-shadow:none}}

.strip{background:var(--soft);border-block:1px solid var(--rule)}
.strip .wrap{display:flex;flex-wrap:wrap;gap:10px 28px;padding-block:16px;align-items:center;justify-content:space-between}
.strip ul{display:flex;flex-wrap:wrap;gap:8px 26px;list-style:none;margin:0;padding:0;font-weight:600}
.strip li{display:flex;align-items:center;gap:8px}
.strip li::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--cyan)}

/* route */
.stop{position:relative;padding-block:clamp(26px,4vw,42px);padding-left:46px}
.stop::before{content:"";position:absolute;left:12px;top:0;bottom:0;width:6px;background:var(--line);border-radius:3px}
.route .stop:first-child::before{top:clamp(30px,4.4vw,48px)}
.route .stop:last-child::before{bottom:auto;height:clamp(30px,4.4vw,48px)}
.stop>header{position:relative;display:flex;flex-wrap:wrap;align-items:baseline;justify-content:space-between;gap:6px 18px;margin-bottom:18px}
.stop>header::before{content:"";position:absolute;left:-46px;top:2px;width:30px;height:30px;border-radius:50%;background:#fff;border:6px solid var(--line)}
.stop>header p{color:var(--muted)}

/* grids */
.grid{display:grid;gap:14px}
.g2{grid-template-columns:repeat(2,minmax(0,1fr))} .g3{grid-template-columns:repeat(3,minmax(0,1fr))} .g4{grid-template-columns:repeat(4,minmax(0,1fr))}
@media (max-width:980px){.g4,.g3{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:600px){.g2,.g3,.g4{grid-template-columns:1fr}}

/* photo card */
.pc{position:relative;border-radius:16px;overflow:hidden;background:var(--soft);display:grid;grid-template-rows:auto 1fr;border:1px solid var(--rule);min-width:0}
.pc .ph{aspect-ratio:3/2;overflow:hidden;position:relative}
.pc .ph img{width:100%;height:100%;object-fit:cover}
.pc .tag{position:absolute;left:12px;top:12px;font:500 .7rem/1 var(--mono);letter-spacing:.1em;text-transform:uppercase;background:#fff;color:var(--ink);padding:6px 9px;border-radius:999px}
.pc .in{padding:14px 16px 16px;display:grid;gap:8px;align-content:start;background:#fff}
.pc .meta{font:500 .8rem var(--mono);color:var(--muted)}
.pc .row{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap;margin-top:4px}
.price{font:800 1.5rem/1 var(--display)} .price small{font:500 .8rem var(--body);color:var(--muted)}
.pc .row a{font-weight:700;text-decoration:none;border-bottom:3px solid var(--line)}
.chips{display:flex;flex-wrap:wrap;gap:6px;list-style:none;margin:0;padding:0}
.chips li{font-size:.82rem;font-weight:600;padding:4px 10px;border-radius:999px;background:var(--soft);color:var(--ink)}

/* overlay tile (tours, services) */
.tile{position:relative;isolation:isolate;border-radius:16px;overflow:hidden;min-height:220px;display:grid;align-content:end;padding:16px;color:#fff;text-decoration:none}
.tile img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-2}
.tile::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(0deg,rgba(4,25,50,.82),rgba(4,25,50,0) 62%)}
.tile h3{font-size:1.2rem} .tile span{font-size:.9rem;opacity:.9}

/* cargo spec */
.split{display:grid;grid-template-columns:1fr 1fr;gap:14px;align-items:stretch}
@media (max-width:820px){.split{grid-template-columns:1fr}}
.split>img{width:100%;height:100%;min-height:220px;object-fit:cover;border-radius:16px}
.boxes{display:grid;gap:12px}
.box{border:1px solid var(--rule);border-radius:16px;padding:18px;display:grid;grid-template-columns:auto 1fr;gap:6px 18px;align-items:center;background:#fff}
.box b{font:800 2.2rem/1 var(--display);color:var(--navy);grid-row:span 2}
.box .meta{font:500 .8rem var(--mono);color:var(--muted)}
.ticks{list-style:none;margin:0;padding:0;display:grid;gap:8px}
.ticks li{display:flex;gap:10px;align-items:center;font-weight:600}
.ticks li::before{content:"";width:12px;height:4px;border-radius:2px;background:var(--line);flex:none}

/* contact */
.contact{background:var(--soft);border-top:1px solid var(--rule)}
.contact .wrap{display:grid;grid-template-columns:.8fr 1.2fr;gap:clamp(22px,4vw,52px);padding-block:clamp(30px,5vw,52px)}
@media (max-width:860px){.contact .wrap{grid-template-columns:1fr}}
.details{display:grid;gap:14px;align-content:start}
.details dl{display:grid;grid-template-columns:auto 1fr;gap:8px 16px;margin:4px 0 0}
.details dt{font:500 .72rem/1.9 var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.details dd{margin:0;font-weight:600}
form{display:grid;gap:12px;grid-template-columns:1fr 1fr;background:#fff;border:1px solid var(--rule);border-radius:18px;padding:20px}
form .full{grid-column:1/-1}
@media (max-width:520px){form{grid-template-columns:1fr}}
label{display:grid;gap:6px;font-weight:600;font-size:.88rem}
input,select,textarea{font:inherit;font-weight:400;color:var(--ink);background:#fff;border:1px solid #c7d9e3;border-radius:10px;padding:11px 12px;width:100%}
textarea{min-height:90px;resize:vertical}
.out{grid-column:1/-1;border:2px solid var(--line);border-radius:14px;padding:16px;display:grid;gap:12px;background:var(--soft)}
.out pre{margin:0;white-space:pre-wrap;font:500 .86rem/1.5 var(--mono);color:var(--ink)}

/* footer */
footer{background:#fff;border-top:1px solid var(--rule)}
footer .wrap{display:flex;flex-wrap:wrap;gap:16px 32px;justify-content:space-between;align-items:center;padding-block:22px}
footer img{height:34px;width:auto}
footer ul{display:flex;flex-wrap:wrap;gap:6px 20px;list-style:none;margin:0;padding:0;font-weight:600;font-size:.92rem}
footer a{text-decoration:none} footer a:hover{text-decoration:underline}
.legal{font-size:.78rem;color:var(--muted);border-top:1px solid var(--rule)}
.legal .wrap{display:block;padding-block:12px 20px}
"""

PAGES = [("index.html", "Home", ""), ("vacations.html", "Vacations", "v"),
         ("transport.html", "Transport", "t"), ("cargo.html", "Cargo", "c")]


def header(current):
    links = "".join(
        f'<a href="{f}"{" aria-current=page" if f == current else ""}>{f"<i class=\"dot {k}\"></i>" if k else ""}<span class="txt">{n}</span></a>'
        for f, n, k in PAGES if f != "index.html")
    return (f'<header class="top"><div class="wrap"><a class="brand" href="index.html"><img src="img/logo.png" alt="StayEasyTZ, meets all your needs" width="520" height="119"></a>'
            f'<nav aria-label="Main">{links}<a class="cta" href="#contact">Book now</a></nav></div></header>')


def contact(default, heading, fields):
    opts = ["Accommodation", "Tours & safaris", "Hiking & trekking", "Group activities",
            "Airport pick-up & drop-off", "Car hire", "Group transport", "Cargo transport"]
    options = "".join(f'<option{" selected" if o == default else ""}>{o}</option>' for o in opts)
    return f'''<section class="contact" id="contact"><div class="wrap">
<div class="details"><span class="label">Contact</span><h2>{heading}</h2>
<dl><dt>Phone</dt><dd>{PHONE}</dd><dt>WhatsApp</dt><dd>{PHONE}</dd><dt>Email</dt><dd>{EMAIL}</dd><dt>Office</dt><dd>Kinondoni, Dar es Salaam</dd><dt>Hours</dt><dd>Mon–Sat, 8 AM – 6 PM</dd></dl>
<div class="btns"><a class="btn wa" href="https://wa.me/{PHONE_RAW}" target="_blank" rel="noopener">Chat on WhatsApp</a></div></div>
<form id="enquiry" novalidate>
<label>Name<input id="f-name" name="Name" required autocomplete="name"></label>
<label>Phone<input id="f-phone" name="Phone" type="tel" autocomplete="tel"></label>
<label class="full">Service<select id="f-service" name="Service">{options}</select></label>
{fields}
<label class="full">Message<textarea id="f-msg" name="Message"></textarea></label>
<div class="full btns"><button class="btn" type="submit">Send request</button></div>
<div class="out" id="out" hidden><span class="label">Your request</span><pre id="out-text"></pre>
<div class="btns"><a class="btn wa" id="wa" target="_blank" rel="noopener">Send on WhatsApp</a><a class="btn ghost" id="em">Send by email</a></div></div>
</form></div></section>'''


CREDITS = ('Photos: Unsplash. Toyota Alphard (Paje, Zanzibar) by Raf24 and Toyota Rumion by Super cool Ian, '
           'both <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener">CC BY-SA 4.0</a> via Wikimedia Commons.')

FOOTER = f'''<footer><div class="wrap"><a href="index.html"><img src="img/logo.png" alt="StayEasyTZ" width="520" height="119"></a>
<ul><li><a href="vacations.html">Vacations</a></li><li><a href="transport.html">Transport</a></li><li><a href="cargo.html">Cargo</a></li><li><a href="https://de-s1.serverpanel.com:2096/" target="_blank" rel="noopener">Staff email</a></li></ul></div>
<div class="legal"><div class="wrap">© 2026 Stay Easy Tanzania. {CREDITS}</div></div></footer>'''

JS = r"""<script>
(function(){
  var rm=window.matchMedia&&matchMedia("(prefers-reduced-motion: reduce)").matches;
  var sets=[].slice.call(document.querySelectorAll(".slides")); if(!sets.length||rm) return;
  sets.forEach(function(el,k){var imgs=[].slice.call(el.children), i=0; el.classList.add("ready"); imgs[0].classList.add("on");
    setTimeout(function(){ setInterval(function(){
      var cur=imgs[i], nxt=imgs[(i+1)%imgs.length];
      nxt.classList.add("snap"); nxt.classList.remove("off","on"); void nxt.offsetWidth; nxt.classList.remove("snap");
      cur.classList.remove("on"); cur.classList.add("off"); nxt.classList.add("on"); i=(i+1)%imgs.length;
    }, 7000); }, k*1200);
  });
})();
</script><script>
(function(){
  var f=document.getElementById('enquiry'); if(!f) return;
  var out=document.getElementById('out'), txt=document.getElementById('out-text');
  document.querySelectorAll('[data-service]').forEach(function(a){
    a.addEventListener('click',function(){document.getElementById('f-service').value=a.dataset.service;
      var x=document.getElementById('f-extra'); if(x&&a.dataset.detail){x.value=a.dataset.detail}});
  });
  f.addEventListener('submit',function(e){
    e.preventDefault();
    var name=document.getElementById('f-name');
    if(!name.value.trim()){name.setCustomValidity('Add your name so we know who to reply to');name.reportValidity();name.focus();return}
    name.setCustomValidity('');
    var lines=['Hello Stay Easy,',''];
    f.querySelectorAll('input,select,textarea').forEach(function(el){ if(el.value.trim()) lines.push(el.name+': '+el.value.trim()); });
    var msg=lines.join('\n'); txt.textContent=msg; out.hidden=false;
    document.getElementById('wa').href='https://wa.me/__PHONE__?text='+encodeURIComponent(msg);
    document.getElementById('em').href='mailto:__EMAIL__?subject='+encodeURIComponent('Request: '+document.getElementById('f-service').value)+'&body='+encodeURIComponent(msg);
    out.scrollIntoView({block:'nearest'});
  });
})();
</script>""".replace("__PHONE__", PHONE_RAW).replace("__EMAIL__", EMAIL)


FOCUS = {"dhow":"30% 50%","safari-cruiser":"28% 60%","cargo-truck":"58% 75%","kilimanjaro":"50% 30%","chauffeur":"65% 40%",
 "cargo-road":"52% 62%","containers":"50% 50%","team":"52% 72%","airport":"45% 45%","car-hire":"42% 40%","alphard":"32% 55%",
 "rumion":"36% 62%","rav4":"50% 55%","safari-lodge":"52% 55%","dar":"50% 50%","beach-hammock":"38% 60%","safari-lion":"52% 58%",
 "zanzibar-beach":"50% 50%","maasai":"50% 45%","balloon":"34% 45%","migration":"50% 55%","group-van":"45% 58%","kili-hike":"50% 55%",
 "ngorongoro":"50% 50%"}

import re
def focus(html):
    return re.sub(r'<img src="img/([a-z0-9-]+)\.jpg"', lambda m: f'<img src="img/{m.group(1)}.jpg" style="object-position:{FOCUS.get(m.group(1),"50% 50%")}"', html)

def page(fname, title, desc, cls, main, contact_html):
    main = focus(main)
    head = (f'<title>{title}</title><meta name="claude:viewport-fit-sides" content="cover">'
            f'<meta name="description" content="{desc}">{FONTS}<style>{CSS}</style>')
    body = f'{header(fname)}<main>{main}{contact_html}</main>{FOOTER}{JS}'
    if fname == "index.html" and not STANDALONE:
        html = f'{head}\n{body}'
    else:
        html = (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
                f'<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
                f'<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}</style>'
                f'{head}</head><body class="{cls}">{body}</body></html>')
    (OUT / fname).write_text(html)


def hero(img, alt, badge, h1, lede, btns):
    return (f'<section class="hero"><img src="img/{img}.jpg" alt="{alt}"><div class="wrap">'
            f'<span class="linebadge"><i></i>{badge}</span><h1>{h1}</h1><p class="lede">{lede}</p>'
            f'<div class="btns">{btns}</div></div></section>')


def tile(img, alt, title, sub, service=None, detail=None):
    attrs = f' href="#contact" data-service="{service}"' + (f' data-detail="{detail}"' if detail else '') if service else ''
    tag = 'a' if service else 'div'
    sub_html = f'<span>{sub}</span>' if sub else ''
    return f'<{tag} class="tile"{attrs}><img src="img/{img}.jpg" alt="{alt}" loading="lazy"><h3>{title}</h3>{sub_html}</{tag}>'


# ---------------------------------------------------------------- HOME
home_main = f'''
<div class="home-wrap">
<div class="home-title"><div class="wrap"><h1>Stay. Ride. Ship.</h1><p>Across East &amp; Central Africa.</p></div></div>
<section class="home-hero" aria-label="Our services">
<a class="panel v" href="vacations.html"><span class="slides"><img src="img/dhow.jpg" alt="Dhow on a Zanzibar beach"><img src="img/kilimanjaro.jpg" alt="Mount Kilimanjaro" loading="lazy"><img src="img/zanzibar-beach.jpg" alt="Zanzibar beach" loading="lazy"></span><span class="label" style="color:#fff">Vacations</span><h2>Stays &amp; tours</h2><span class="go">Explore <i>→</i></span></a>
<a class="panel t" href="transport.html"><span class="slides"><img src="img/safari-cruiser.jpg" alt="Safari Land Cruiser on a dirt road in Tanzania"><img src="img/chauffeur.jpg" alt="Driver at the wheel" loading="lazy"><img src="img/migration.jpg" alt="Safari vehicles among wildebeest" loading="lazy"></span><span class="label" style="color:#fff">Transport</span><h2>Pick-ups &amp; car hire</h2><span class="go">Book a ride <i>→</i></span></a>
<a class="panel c" href="cargo.html"><span class="slides"><img src="img/cargo-truck.jpg" alt="Truck hauling an orange shipping container"><img src="img/containers.jpg" alt="Stacked shipping containers" loading="lazy"><img src="img/cargo-road.jpg" alt="Truck on an open highway" loading="lazy"></span><span class="label" style="color:#fff">Cargo</span><h2>Container haulage</h2><span class="go">Get a quote <i>→</i></span></a>
</section></div>
<section class="strip" aria-label="Why Stay Easy"><div class="wrap"><ul><li>15+ years experience</li><li>Licensed &amp; insured fleet</li><li>No hidden fees</li><li>Tanzania · Zanzibar · Kenya · Uganda · South Africa</li></ul></div></section>
'''

# ---------------------------------------------------------------- VACATIONS
def stay(img, alt, region, name, guests, feats, price):
    chips = "".join(f"<li>{x}</li>" for x in feats)
    return (f'<article class="pc"><div class="ph"><img src="img/{img}.jpg" alt="{alt}" loading="lazy"><span class="tag">{region}</span></div>'
            f'<div class="in"><h3>{name}</h3><span class="meta">{guests}</span><ul class="chips">{chips}</ul>'
            f'<div class="row"><span class="price">${price}<small> /night from</small></span>'
            f'<a href="#contact" data-service="Accommodation" data-detail="{name}, {region}">Enquire</a></div></div></article>')

vac_main = hero("kilimanjaro", "Mount Kilimanjaro above the plains with zebras", "Vacations",
                "Beaches, safaris &amp; <em>Kilimanjaro.</em>", "Stays and tours across East Africa.",
                '<a class="btn" href="#contact" data-service="Accommodation">Plan my trip</a><a class="btn glass" href="#stays">See stays</a>') + f'''
<div class="route"><div class="wrap">
<section class="stop" id="stays"><header><h2>Stays</h2><p>All-inclusive packages available</p></header>
<div class="grid g3">
{stay("beach-hammock","Hammock between palm trees on a white-sand beach","Zanzibar","Beach Experience","2 adults · 1 child under 7",["Ocean view","Private beach","Restaurant"],120)}
{stay("safari-lodge","Tented safari lodge with elephants in front","Serengeti","Safari Lodge","2 adults · 2 children under 7",["Wildlife view","Guided tours","All meals"],150)}
{stay("dar","Aerial view of central Dar es Salaam and the harbour","Dar es Salaam","City Experience","4 adults · 2 children under 7",["City centre","Modern amenities","Breakfast"],50)}
</div></section>
<section class="stop" id="tours"><header><h2>Tours</h2><p>Planned around you</p></header>
<div class="grid g4">
{tile("safari-lion","Safari vehicle with a lion walking past","Safari expeditions","","Tours & safaris","Safari expedition")}
{tile("zanzibar-beach","Zanzibar beach with boats and thatched umbrellas","Beach getaways","","Tours & safaris","Beach getaway")}
{tile("maasai","Maasai women in traditional dress","Cultural tours","","Tours & safaris","Cultural tour")}
{tile("balloon","Hot-air balloon over zebras on the plains","Adventure packages","","Tours & safaris","Adventure package")}
</div></section>
<section class="stop" id="hiking"><header><h2>Hiking</h2><p>Certified guides · group or private</p></header>
<div class="grid g2">
<article class="pc"><div class="ph"><img src="img/kili-hike.jpg" alt="Hikers climbing a trail on Kilimanjaro" loading="lazy"><span class="tag">5–9 days</span></div><div class="in"><h3>Mount Kilimanjaro Trek</h3><span class="meta">Moderate to challenging · several routes</span><div class="row"><span class="meta">Sunrise summit</span><a href="#contact" data-service="Hiking &amp; trekking" data-detail="Mount Kilimanjaro Trek">Book trek</a></div></div></article>
<article class="pc"><div class="ph"><img src="img/ngorongoro.jpg" alt="View into the Ngorongoro Crater" loading="lazy"><span class="tag">Half to full day</span></div><div class="in"><h3>Ngorongoro Crater Walks</h3><span class="meta">Easy to moderate · wildlife up close</span><div class="row"><span class="meta">Guided nature walk</span><a href="#contact" data-service="Hiking &amp; trekking" data-detail="Ngorongoro Crater Walks">Book walk</a></div></div></article>
</div></section>
<section class="stop" id="groups"><header><h2>Groups</h2><p>Corporate events · team building · custom itineraries</p></header>
<div class="split"><img src="img/team.jpg" alt="Tour group posing at a waterfall in the forest" loading="lazy">
<div class="box" style="grid-template-columns:1fr;align-content:center"><ul class="ticks"><li>Corporate events</li><li>Team building</li><li>Group exploration</li><li>Custom itineraries</li></ul><div class="btns" style="margin-top:8px"><a class="btn" href="#contact" data-service="Group activities">Plan a group trip</a></div></div></div>
</section>
</div></div>'''

# ---------------------------------------------------------------- TRANSPORT
def car(img, alt, name, seats, feats, usd):
    chips = "".join(f"<li>{x}</li>" for x in feats)
    return (f'<article class="pc"><div class="ph"><img src="img/{img}.jpg" alt="{alt}" loading="lazy"><span class="tag">{seats} seats</span></div>'
            f'<div class="in"><h3>{name}</h3><ul class="chips">{chips}</ul>'
            f'<div class="row"><span class="price">${usd}<small> /day · Tsh {tsh(usd)}</small></span>'
            f'<a href="#contact" data-service="Car hire" data-detail="{name}">Request</a></div></div></article>')

tr_main = hero("chauffeur", "Driver at the wheel of a car", "Transport",
               "From arrivals <em>to anywhere.</em>", "Insured vehicles, 24/7 support on every booking.",
               '<a class="btn" href="#contact" data-service="Airport pick-up &amp; drop-off">Book a pick-up</a><a class="btn glass" href="#fleet">See the fleet</a>') + f'''
<div class="route"><div class="wrap">
<section class="stop" id="services"><header><h2>Services</h2><p>Self-drive or with a driver</p></header>
<div class="grid g4">
{tile("airport","Pick Up Here sign at an airport","Airport pick &amp; drop","Book →","Airport pick-up & drop-off")}
{tile("car-hire","Man standing by a hired car","Car hire","Book →","Car hire")}
{tile("migration","Safari vehicles among wildebeest in the Serengeti","Safari vehicles","Book →","Car hire","Safari vehicle")}
{tile("group-van","White passenger van on a tree-lined road","Group transport","Book →","Group transport")}
</div></section>
<section class="stop" id="fleet"><header><h2>Fleet</h2><p>Daily rates · longer hires on request</p></header>
<div class="grid g3">
{car("alphard","White Toyota Alphard in Paje, Zanzibar","Toyota Alphard",7,["Luxury","Executive","Business travel"],50)}
{car("rumion","Toyota Rumion","Toyota Rumion",7,["Family","City tours","Fuel efficient"],30)}
{car("rav4","Silver Toyota RAV4","Toyota RAV4",5,["Off-road","Safari tours","All-terrain"],70)}
</div></section>
</div></div>'''

# ---------------------------------------------------------------- CARGO
cg_main = hero("cargo-road", "Truck and trailer on an open highway", "Cargo",
               "Containers moved <em>across the region.</em>", "Experienced transporters based in East &amp; Central Africa.",
               '<a class="btn" href="#contact" data-service="Cargo transport">Request a quote</a><a class="btn glass" href="#containers">Container sizes</a>') + '''
<div class="route"><div class="wrap">
<section class="stop" id="containers"><header><h2>Containers</h2><p>Quote on request</p></header>
<div class="split"><img src="img/containers.jpg" alt="Stacked shipping containers" loading="lazy">
<div class="boxes">
<div class="box"><b>20 ft</b><h3>Standard container</h3><span class="meta">6.1 m long</span></div>
<div class="box"><b>40 ft</b><h3>Large container</h3><span class="meta">12.2 m long</span></div>
<div class="box" style="grid-template-columns:1fr"><ul class="ticks"><li>Container handling</li><li>Regional cargo movement</li><li>Logistics support</li><li>Insured vehicles</li></ul></div>
</div></div></section>
</div></div>'''

CARGO_FIELDS = '''<label>Container<select id="f-extra" name="Container"><option>20 ft</option><option>40 ft</option><option>Not sure</option></select></label>
<label>Ready date<input id="f-date" name="Ready date" type="date"></label>
<label>From<input id="f-from" name="From"></label><label>To<input id="f-to" name="To"></label>'''
TRANSPORT_FIELDS = '''<label>Vehicle<input id="f-extra" name="Vehicle"></label>
<label>Date<input id="f-date" name="Date" type="date"></label>
<label>Pick-up<input id="f-from" name="Pick-up"></label><label>Drop-off<input id="f-to" name="Drop-off"></label>'''
VAC_FIELDS = '''<label>Stay or trip<input id="f-extra" name="Trip"></label>
<label>Dates<input id="f-date" name="Dates"></label>'''

page("index.html", "Stay Easy Tanzania", "Accommodation, transport and cargo across East and Central Africa.", "",
     home_main, contact("Accommodation", "Book with us", ""))
page("vacations.html", "Vacations · Stay Easy Tanzania", "Stays, tours and hikes in Tanzania, Zanzibar and East Africa.", "v",
     vac_main, contact("Accommodation", "Plan your trip", VAC_FIELDS))
page("transport.html", "Transport · Stay Easy Tanzania", "Airport pick-ups, car hire, safari vehicles and group transport.", "t",
     tr_main, contact("Airport pick-up & drop-off", "Book a vehicle", TRANSPORT_FIELDS))
page("cargo.html", "Cargo · Stay Easy Tanzania", "20 ft and 40 ft container transport across East and Central Africa.", "c",
     cg_main, contact("Cargo transport", "Request a quote", CARGO_FIELDS))
print("built")
