import json, os, re, sys
ROOT = sys.argv[1]
PROJECTS = json.load(open(os.path.join(ROOT, 'data', 'projects.json')))
idx = open(os.path.join(ROOT, 'index.html')).read()
icons = re.search(r'(<svg width="0" height="0".*?</svg>)', idx, re.S).group(1)

COMMON = {
 'en': dict(back="← All services", inc_h="What's included", work_h="Recent work", tap="Tap a photo to enlarge.",
   area_h="Where we work", area_p="Based in Malden, we serve towns across Massachusetts, including:",
   area_more="Don't see your town? Ask us.", other_h="Other services",
   cta_h="Get a free, detailed estimate", cta_p="Every estimate is in writing, with each step explained. What we agree on is what we deliver.",
   cta_est="Request an estimate", cta_text="Send us a text", call_short="Call", text_short="Text", before="Before", after="After", close="Close",
   foot="Insured painting contractor, Malden, Massachusetts"),
 'pt': dict(back="← Todos os serviços", inc_h="O que está incluído", work_h="Trabalhos recentes", tap="Toque numa foto para ampliar.",
   area_h="Onde atendemos", area_p="Com base em Malden, atendemos cidades de todo o Massachusetts, como:",
   area_more="Não viu sua cidade? Pergunte.", other_h="Outros serviços",
   cta_h="Peça um orçamento grátis e detalhado", cta_p="Todo orçamento é por escrito, com cada etapa explicada. O que combinamos é o que entregamos.",
   cta_est="Pedir orçamento", cta_text="Mandar SMS", call_short="Ligar", text_short="SMS", before="Antes", after="Depois", close="Fechar",
   nav_services="Serviços", nav_work="Trabalhos", nav_about="Sobre nós", nav_est="Orçamento",
   foot="Empresa de pintura com seguro, Malden, Massachusetts"),
 'es': dict(back="← Todos los servicios", inc_h="Qué incluye", work_h="Trabajos recientes", tap="Toque una foto para ampliarla.",
   area_h="Dónde trabajamos", area_p="Con base en Malden, atendemos ciudades de todo Massachusetts, como:",
   area_more="¿No ve su ciudad? Pregúntenos.", other_h="Otros servicios",
   cta_h="Pida un presupuesto gratis y detallado", cta_p="Cada presupuesto es por escrito, con cada paso explicado. Lo que acordamos es lo que entregamos.",
   cta_est="Pedir presupuesto", cta_text="Enviar mensaje de texto", call_short="Llamar", text_short="Texto", before="Antes", after="Después", close="Cerrar",
   nav_services="Servicios", nav_work="Trabajos", nav_about="Nosotros", nav_est="Presupuesto",
   foot="Empresa de pintura asegurada, Malden, Massachusetts"),
}
TOWNS = "Malden, Medford, Everett, Melrose, Revere, Saugus, Somerville, Cambridge, Boston, Arlington, Lexington, Woburn, Burlington, Billerica, Waltham, Newton, Brookline, Wellesley, Quincy, Winchester."

PAGES = [
 dict(slug='interior-painting', job='o1', title="Interior Painting in Massachusetts", 
  desc="Residential interior painting specialists in Massachusetts: walls, ceilings, trim, doors, drywall repair and wallpaper removal. Insured. Free, detailed written estimates.",
  photos=[('cambridge-antes','before','Living room before'),('cambridge-depois-1','after','Living room after'),('cambridge-depois-3','after','Bedroom after'),('brookline-depois-1','after','Room after'),('brookline-depois-2','after','Room after'),('brookline-depois-3','after','Room after')],
  en=dict(eye="Our specialty", h="Residential interior painting", p="Interior painting is what we do most and where we deliver our finest finish. Walls, ceilings, trim and doors, prepared properly before the first coat.",
   inc=["Walls, ceilings, baseboards, trim and doors","Drywall repair, patching and sanding before painting","Primer where the surface needs it","Wallpaper removal and wall prep","Floors and furniture covered, rooms left clean"], nav="Interior painting"),
  pt=dict(eye="Nossa especialidade", h="Pintura interna residencial", p="Pintura interna é o que mais fazemos e onde entregamos nosso acabamento mais fino. Paredes, tetos, rodapés e portas, bem preparados antes da primeira demão.",
   inc=["Paredes, tetos, rodapés, guarnições e portas","Reparo de drywall, massa e lixa antes da pintura","Primer onde a superfície precisa","Remoção de papel de parede e preparação da parede","Piso e móveis protegidos, ambientes entregues limpos"], nav="Pintura interna"),
  es=dict(eye="Nuestra especialidad", h="Pintura interior residencial", p="La pintura interior es lo que más hacemos y donde entregamos nuestro mejor acabado. Paredes, techos, molduras y puertas, bien preparados antes de la primera mano.",
   inc=["Paredes, techos, zócalos, molduras y puertas","Reparación de drywall, masilla y lijado antes de pintar","Primer donde la superficie lo necesita","Retiro de papel tapiz y preparación de la pared","Pisos y muebles protegidos, espacios entregados limpios"], nav="Pintura interior")),
 dict(slug='cabinet-painting', job='o3', title="Cabinet Painting and Refinishing in Massachusetts",
  desc="Kitchen and bathroom cabinet painting and staining, furniture and metal refinishing in Massachusetts. Insured. Free, detailed written estimates.",
  photos=[('wellesley-antes-1','before','Kitchen cabinets before'),('wellesley-depois-1','after','Kitchen cabinets after'),('wellesley-depois-2','after','Kitchen cabinets after'),('billerica-antes','before','Cabinets before'),('billerica-depois-1','after','Cabinets after'),('billerica-depois-2','after','Cabinets after')],
  en=dict(eye="Fine finishes", h="Cabinets, furniture and metal", p="Give your kitchen or bathroom a new look without replacing the cabinets. We clean, sand, prime and finish, or strip the old stain and apply a new one. We also refinish furniture and metal pieces.",
   inc=["Kitchen and bathroom cabinets, doors and drawers","Degreasing, sanding and bonding primer","A new paint color or a fresh stain","Furniture, railings and metal surfaces","Spray finishes when the piece calls for it"], nav="Cabinets and furniture"),
  pt=dict(eye="Acabamento fino", h="Armários, móveis e ferragens", p="Dê cara nova à cozinha ou ao banheiro sem trocar os armários. Limpamos, lixamos, aplicamos primer e finalizamos, ou removemos o stain antigo e aplicamos um novo. Também renovamos móveis e peças de metal.",
   inc=["Armários de cozinha e banheiro, portas e gavetas","Desengraxe, lixa e primer de aderência","Nova cor de tinta ou novo stain","Móveis, grades e superfícies de metal","Pintura a spray quando a peça pede"], nav="Armários e móveis"),
  es=dict(eye="Acabado fino", h="Gabinetes, muebles y metal", p="Renueve su cocina o baño sin cambiar los gabinetes. Limpiamos, lijamos, aplicamos primer y terminamos, o retiramos el tinte viejo y aplicamos uno nuevo. También renovamos muebles y piezas de metal.",
   inc=["Gabinetes de cocina y baño, puertas y cajones","Desengrase, lijado y primer de adherencia","Nuevo color de pintura o un tinte nuevo","Muebles, barandas y superficies de metal","Acabados en spray cuando la pieza lo pide"], nav="Gabinetes y muebles")),
 dict(slug='stairs-railings', job='o1', title="Stair, Handrail and Baluster Painting in Massachusetts",
  desc="Painting and staining of stairs, risers, handrails and balusters in Massachusetts homes. Insured. Free, detailed written estimates.",
  photos=[('cambridge-depois-2','after','Staircase after')],
  en=dict(eye="Detail work", h="Stairs, handrails and balusters", p="Stairs are the most detailed job in the house: every baluster, every riser, every edge. That's why we treat them as interior specialist work.",
   inc=["Risers, treads and stringers","Handrails and newel posts","Balusters, one by one","Paint or stain, matched to the rest of the house"], nav="Stairs and railings"),
  pt=dict(eye="Trabalho de detalhe", h="Escadas, corrimãos e balaústres", p="A escada é o trabalho mais minucioso da casa: cada balaústre, cada espelho, cada quina. Por isso tratamos a escada como trabalho de especialista em interiores.",
   inc=["Espelhos, degraus e laterais","Corrimãos e pilares","Balaústres, um a um","Tinta ou stain, combinando com o resto da casa"], nav="Escadas e corrimãos"),
  es=dict(eye="Trabajo de detalle", h="Escaleras, pasamanos y balaústres", p="La escalera es el trabajo más minucioso de la casa: cada balaústre, cada contrahuella, cada borde. Por eso la tratamos como trabajo de especialistas en interiores.",
   inc=["Contrahuellas, peldaños y zancas","Pasamanos y postes","Balaústres, uno por uno","Pintura o tinte, a juego con el resto de la casa"], nav="Escaleras y pasamanos")),
 dict(slug='basement-floor-painting', job='o7', title="Basement Floor Painting in Massachusetts",
  desc="Basement concrete floor cleaning, prep and painting in Massachusetts. Insured. Free, detailed written estimates.",
  photos=[],
  en=dict(eye="Basements", h="Basement floor painting", p="A painted concrete floor makes a basement cleaner, brighter and easier to keep. We clean and prepare the concrete, then apply a coating made for floors.",
   inc=["Cleaning and degreasing the concrete","Floor-grade primer and paint","Walls and ceiling too, if you want the whole basement done"], nav="Basement floors"),
  pt=dict(eye="Basements", h="Pintura de piso de basement", p="Piso de concreto pintado deixa o basement mais limpo, mais claro e mais fácil de manter. Limpamos e preparamos o concreto e aplicamos uma tinta própria para piso.",
   inc=["Limpeza e desengraxe do concreto","Primer e tinta próprios para piso","Paredes e teto também, se quiser o basement inteiro"], nav="Piso de basement"),
  es=dict(eye="Sótanos", h="Pintura de pisos de sótano", p="Un piso de concreto pintado deja el sótano más limpio, más claro y más fácil de mantener. Limpiamos y preparamos el concreto y aplicamos una pintura hecha para pisos.",
   inc=["Limpieza y desengrase del concreto","Primer y pintura para pisos","Paredes y techo también, si quiere todo el sótano"], nav="Pisos de sótano")),
 dict(slug='commercial-painting', job='o7', title="Commercial and Rental Painting in Massachusetts",
  desc="Commercial painting for stores, offices and rental apartments in Massachusetts, for owners, property managers and general contractors. Insured. Free, detailed written estimates.",
  photos=[],
  en=dict(eye="Commercial", h="Commercial and rental painting", p="Storefronts, offices and rental apartments, painted at the same standard we use in homes. We work directly with property owners and with general contractors.",
   inc=["Stores, offices and commercial spaces","Rental units between tenants","Interior and exterior","A detailed written estimate before we start","Owners, property managers and general contractors"], nav="Commercial and rentals"),
  pt=dict(eye="Comercial", h="Pintura comercial e de aluguel", p="Lojas, salas e apartamentos de aluguel, pintados com o mesmo padrão que usamos nas casas. Trabalhamos direto com proprietários e com general contractors.",
   inc=["Lojas, salas e espaços comerciais","Apartamentos de aluguel entre um inquilino e outro","Interior e exterior","Orçamento detalhado por escrito antes de começar","Proprietários, administradores e general contractors"], nav="Comercial e aluguel"),
  es=dict(eye="Comercial", h="Pintura comercial y de alquiler", p="Locales, oficinas y apartamentos de alquiler, pintados con el mismo estándar que usamos en las casas. Trabajamos directamente con propietarios y con contratistas generales.",
   inc=["Locales, oficinas y espacios comerciales","Apartamentos de alquiler entre inquilinos","Interior y exterior","Presupuesto detallado por escrito antes de empezar","Propietarios, administradores y contratistas generales"], nav="Comercial y alquiler")),
 dict(slug='exterior-painting', job='o2', title="Exterior Painting and Pressure Washing in Massachusetts",
  desc="Exterior house painting, deck staining and pressure washing in Massachusetts, residential and commercial. Insured. Free, detailed written estimates.",
  photos=[('somerville-antes-1','before','House before'),('somerville-depois-1','after','House after'),('somerville-antes-2','before','Deck before'),('somerville-depois-2','after','Deck after'),('brookline-exterior','after','House exterior after')],
  en=dict(eye="Outside", h="Exterior painting and pressure washing", p="Siding, trim, doors and decks, prepared to stand up to New England winters. Pressure washing on its own or before we paint.",
   inc=["Siding, trim and doors","Decks: paint or stain","Scraping, sanding and priming bare spots","Pressure washing for siding, decks and driveways","Residential and commercial"], nav="Exterior and pressure washing"),
  pt=dict(eye="Área externa", h="Pintura externa e pressure washing", p="Siding, acabamentos, portas e decks, preparados para aguentar o inverno da Nova Inglaterra. Lavagem com pressão sozinha ou antes da pintura.",
   inc=["Siding, acabamentos e portas","Decks: tinta ou stain","Raspagem, lixa e primer nas partes expostas","Lavagem com pressão de siding, decks e garagens","Residencial e comercial"], nav="Externa e pressure washing"),
  es=dict(eye="Exterior", h="Pintura exterior y lavado a presión", p="Siding, molduras, puertas y decks, preparados para el invierno de Nueva Inglaterra. Lavado a presión solo o antes de pintar.",
   inc=["Siding, molduras y puertas","Decks: pintura o tinte","Raspado, lijado y primer en zonas expuestas","Lavado a presión de siding, decks y entradas","Residencial y comercial"], nav="Exterior y lavado a presión")),
]

def esc(t): return t.replace('&','&amp;').replace('<','&lt;')

for pg in PAGES:
    en = pg['en']; C = COMMON['en']
    dicts = {}
    for L in ('pt','es'):
        d = dict(COMMON[L]); P = pg[L]
        d.update(eye=P['eye'], h=P['h'], p=P['p'])
        for i,t in enumerate(P['inc']): d['i%d'%i] = t
        for q in PAGES: d['nav_'+q['slug']] = q[L]['nav']
        dicts[L] = d
    inc = "\n".join(f'<li><svg><use href="#i-check"/></svg><span data-i18n="i{i}">{esc(t)}</span></li>' for i,t in enumerate(en['inc']))
    gallery = ''
    projs = [x for x in PROJECTS if pg['slug'] in x['services']
             and any(k=='before' for _,k,_ in x['photos']) and any(k=='after' for _,k,_ in x['photos'])]
    for x in projs:
        if x['photos'][0][1] != 'before': x['photos'].sort(key=lambda t: 0 if t[1]=='before' else 1)
    if projs:
        blocks = []
        for x in projs:
            for L in ('pt','es'): dicts[L]['pd_'+x['id']] = x['desc'][L]
            shots = "\n".join(f'<button type="button" class="shot"><img src="/img/{f}.jpg" alt="{x["city"]}: {a}" loading="lazy"><span class="tag{" before" if k=="before" else ""}" data-i18n="{k}">{C[k]}</span></button>' for f,k,a in x['photos'])
            blocks.append(f'<article class="project"><div class="project-head"><h3>{x["city"]}, MA</h3><p data-i18n="pd_{x["id"]}">{esc(x["desc"]["en"])}</p></div><div class="shots">{shots}</div></article>')
        gallery = f'''<section class="alt" aria-labelledby="w-h"><div class="wrap">
  <div class="section-head"><h2 id="w-h" data-i18n="work_h">{C['work_h']}</h2><p class="lead" data-i18n="tap">{C['tap']}</p></div>
  <div class="projects">{"".join(blocks)}</div></div></section>
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Photo"><button type="button" id="lb-close" data-i18n="close">Close</button><img alt=""></div>'''
    others = "\n".join(f'<a href="/{q["slug"]}/" data-i18n="nav_{q["slug"]}">{esc(q["en"]["nav"])}</a>' for q in PAGES if q is not pg)
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{pg['title']} | Made Painting Service Plus</title>
<meta name="description" content="{pg['desc']}">
<link rel="canonical" href="https://madepaintingservice.com/{pg['slug']}/">
<link rel="icon" href="/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/site.css">
</head>
<body>
{icons}
<header class="top"><div class="wrap">
  <a class="brand" href="/" aria-label="Made Painting Service Plus, home"><img src="/logo.png" alt="" width="46" height="46"><span class="brand-name">Made Painting<small>Service Plus LLC</small></span></a>
  <nav class="mainnav" aria-label="Main"><a href="/#services" data-i18n="nav_services">Services</a><a href="/#work" data-i18n="nav_work">Our work</a><a href="/#about" data-i18n="nav_about">About us</a><a href="/#estimate" data-i18n="nav_est">Free estimate</a></nav>
  <div class="top-actions">
    <div class="langs" role="group" aria-label="Language"><button class="lang" type="button" data-lang="en" aria-pressed="true">EN</button><button class="lang" type="button" data-lang="pt" aria-pressed="false">PT</button><button class="lang" type="button" data-lang="es" aria-pressed="false">ES</button></div>
    <a class="btn btn-primary btn-sm" href="tel:+17327916348"><svg><use href="#i-phone"/></svg><span data-i18n="call_short">Call</span></a>
  </div>
</div></header>
<main>
<section class="svc-hero"><div class="wrap">
  <a class="back" href="/#services" data-i18n="back">{C['back']}</a>
  <p class="eyebrow" data-i18n="eye">{esc(en['eye'])}</p>
  <h1 data-i18n="h">{esc(en['h'])}</h1>
  <p data-i18n="p">{esc(en['p'])}</p>
  <div class="hero-ctas"><a class="btn btn-primary" href="/?job={pg['job']}#estimate" data-i18n="cta_est">{C['cta_est']}</a><a class="btn btn-ghost" href="sms:+17327916348"><svg><use href="#i-sms"/></svg><span data-i18n="cta_text">{C['cta_text']}</span></a></div>
</div></section>
<section aria-labelledby="inc-h"><div class="wrap">
  <div class="section-head"><h2 id="inc-h" data-i18n="inc_h">{C['inc_h']}</h2></div>
  <ul class="incl">{inc}</ul>
</div></section>
{gallery}
<section aria-labelledby="area-h"><div class="wrap two">
  <div class="panel"><h3 id="area-h" data-i18n="area_h">{C['area_h']}</h3><p data-i18n="area_p">{C['area_p']}</p><p class="towns">{TOWNS}</p><p style="margin-top:14px" data-i18n="area_more">{C['area_more']}</p></div>
  <div class="panel"><h3 data-i18n="other_h">{C['other_h']}</h3><div class="more-svc">{others}</div></div>
</div></section>
<section class="cta-band"><div class="wrap">
  <h2 data-i18n="cta_h">{C['cta_h']}</h2><p class="lead" data-i18n="cta_p">{C['cta_p']}</p>
  <div class="hero-ctas"><a class="btn btn-primary" href="/?job={pg['job']}#estimate" data-i18n="cta_est">{C['cta_est']}</a><a class="btn btn-ghost" href="tel:+17327916348"><svg><use href="#i-phone"/></svg>(732) 791-6348</a></div>
</div></section>
</main>
<footer><div class="wrap"><span><strong>Made Painting Service Plus LLC</strong> <span data-i18n="foot">{C['foot']}</span></span><span>(732) 791-6348</span></div></footer>
<div class="callbar">
  <a class="btn btn-primary" href="tel:+17327916348"><svg><use href="#i-phone"/></svg><span data-i18n="call_short">Call</span></a>
  <a class="btn btn-outline" href="sms:+17327916348"><svg><use href="#i-sms"/></svg><span data-i18n="text_short">Text</span></a>
  <a class="btn btn-outline" href="https://wa.me/17327916348"><svg><use href="#i-chat"/></svg>WhatsApp</a>
</div>
<script>
(function () {{
  var dicts = {json.dumps(dicts, ensure_ascii=False)};
  var en = {{}};
  document.querySelectorAll("[data-i18n]").forEach(function (el) {{ en[el.getAttribute("data-i18n")] = el.textContent; }});
  dicts.en = en;
  var htmlLang = {{ en: "en", pt: "pt-BR", es: "es" }};
  var btns = document.querySelectorAll(".langs .lang");
  function apply(lang) {{
    var d = dicts[lang] || en;
    document.querySelectorAll("[data-i18n]").forEach(function (el) {{ var k = el.getAttribute("data-i18n"); if (d[k]) el.textContent = d[k]; }});
    document.documentElement.lang = htmlLang[lang] || "en";
    btns.forEach(function (b) {{ b.setAttribute("aria-pressed", b.getAttribute("data-lang") === lang ? "true" : "false"); }});
    try {{ localStorage.setItem("lang", lang); }} catch (e) {{}}
  }}
  var saved = null;
  try {{ saved = localStorage.getItem("lang"); }} catch (e) {{}}
  if (!dicts[saved]) {{ var nav = (navigator.language || "").toLowerCase().slice(0, 2); saved = dicts[nav] ? nav : "en"; }}
  if (saved !== "en") apply(saved);
  btns.forEach(function (b) {{ b.addEventListener("click", function () {{ apply(b.getAttribute("data-lang")); }}); }});
  var lb = document.getElementById("lightbox");
  if (lb) {{
    var img = lb.querySelector("img"), closeBtn = document.getElementById("lb-close"), last = null;
    function close() {{ lb.classList.remove("open"); img.removeAttribute("src"); if (last) last.focus(); }}
    document.querySelectorAll(".shot").forEach(function (b) {{ b.addEventListener("click", function () {{ last = b; img.src = b.querySelector("img").src; img.alt = b.querySelector("img").alt; lb.classList.add("open"); closeBtn.focus(); }}); }});
    closeBtn.addEventListener("click", close);
    lb.addEventListener("click", function (e) {{ if (e.target === lb) close(); }});
    document.addEventListener("keydown", function (e) {{ if (e.key === "Escape" && lb.classList.contains("open")) close(); }});
  }}
}})();
</script>
</body>
</html>
'''
    os.makedirs(os.path.join(ROOT, pg['slug']), exist_ok=True)
    open(os.path.join(ROOT, pg['slug'], 'index.html'), 'w').write(html)
print('ok')
