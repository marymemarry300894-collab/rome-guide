import base64, os

HERE = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(HERE, "images")
OUT_HTML = os.path.join(HERE, "index.html")

# image key -> filename
imgs = {
    "colosseum": "colosseum.jpg",
    "forum": "forum.jpg",
    "palatine": "palatine.jpg",
    "pantheon": "pantheon.jpg",
    "trevi": "trevi.jpg",
    "navona": "navona.jpg",
    "vatican": "vatican_museums.jpg",
    "stpeter": "stpeter.jpg",
    "trastevere": "trastevere.jpg",
    "borghese": "borghese.jpg",
}

def b64(key):
    p = os.path.join(IMG_DIR, imgs[key])
    with open(p, "rb") as f:
        return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()

b = {k: b64(k) for k in imgs}

# ---- hotel / start point ----
HOTEL = {
    "name": "Hotel Villa Pinciana",
    "addr": "Via Abruzzi 11, Виа Венето, 00187 Рим",
    "rating": "9.2 / 10 (на основе 442 отзывов)",
    "lat": 41.9090525, "lng": 12.4921677,
}

# ---- itinerary data ----
days = [
    {
        "title": "День 1 — Древний Рим + исторический центр",
        "color": "#e74c3c",
        "places": [
            {"img": b["colosseum"], "name": "Колизей", "time": "09:00 – 12:30",
             "desc": "Колизей, Римский Форум, Палатинский холм — комбинированный билет (~16 €, онлайн skip-the-line). Начните с Колизея, затем Форум и Палатин для панорамы.",
             "lat": 41.8902, "lng": 12.4922},
            {"img": b["forum"], "name": "Римский Форум", "time": "10:30 – 12:00",
             "desc": "Сердце древнего Рима: храмы, базилики, арка Септимия Севера. Идёт по пути от Колизея к Палатину.",
             "lat": 41.8919, "lng": 12.4853},
            {"img": b["palatine"], "name": "Палатинский холм", "time": "12:00 – 12:30",
             "desc": "Легендарное место основания Рима, вид сверху на Форум и Большой цирк.",
             "lat": 41.8886, "lng": 12.4870},
            {"img": b["pantheon"], "name": "Пантеон", "time": "13:30 – 15:00",
             "desc": "Вход платный (~5 €, с 2023 года). Обязательно бронируйте онлайн на pantheonroma.com — иначе не пустят. Внутри — знаменитый купол с окулюсом, шедевр инженерии.",
             "lat": 41.8986, "lng": 12.4769},
            {"img": b["trevi"], "name": "Фонтан Треви", "time": "12:30 – 13:30",
             "desc": "Физически подойти и кинуть монетку можно бесплатно в любое время — фонтан стоит в открытой площади. Но в карточке Google показан платный «Входной билет» от партнёров (Viator, Trip.com, Tourscanner) — экскурсии/туры от ~2 €. Это не обязательно, это тур, а не вход к воде. Чтобы избежать толпы и спокойно сфоткаться — приходите до 8:00 утра.",
             "lat": 41.9009, "lng": 12.4833},
            {"img": b["navona"], "name": "Площадь Навона", "time": "15:00 – 16:30",
             "desc": "Фонтаны Бернини, уличные художники, атмосферные кафе.",
             "lat": 41.8994, "lng": 12.4765},
        ],
        "dinner": {"name": "Da Enzo al 29", "link": "https://www.tripadvisor.com/Restaurant_Review-g187791-d1225073-Reviews-Da_Enzo_al_29-Rome_Lazio.html",
                   "desc": "Трастевере — паста amatriciana или cacio e pepe + бокал домашнего вина ≈ 22–28 €.",
                   "lat": 41.8880, "lng": 12.4695},
    },
    {
        "title": "День 2 — Ватикан + барокко",
        "color": "#27ae60",
        "places": [
            {"img": b["vatican"], "name": "Музеи Ватикана + Сикстинская капелла", "time": "09:00 – 12:30",
             "desc": "Вход платный (~20–30 €, онлайн skip-the-line). Билет включает Сикстинскую капеллу. Приходите к открытию (09:00), чтобы избежать очередей.",
             "lat": 41.9065, "lng": 12.4536},
            {"img": b["stpeter"], "name": "Базилика Святого Петра", "time": "12:30 – 13:30",
             "desc": "Бесплатный вход (может быть очередь). Подъём на купол ~8 € — вид на всю площадь и город.",
             "lat": 41.9022, "lng": 12.4534},
            {"img": b["trastevere"], "name": "Трастевере", "time": "15:00 – 16:30",
             "desc": "Живописный район: площадь Santa Maria in Trastevere, узкие улочки, уютные trattoria.",
             "lat": 41.8890, "lng": 12.4691},
        ],
        "dinner": {"name": "Osteria da Fortunata", "link": "https://www.tripadvisor.com/Restaurant_Review-g187791-d1203902-Reviews-Osteria_da_Fortunata-Rome_Lazio.html",
                   "desc": "Campo de' Fiori — домашняя паста (tonnarelli cacio e pepe) + бокал вина ≈ 22–28 €.",
                   "lat": 41.8955, "lng": 12.4724},
    },
    {
        "title": "День 3 — Вилла Боргезе, центр и шопинг",
        "color": "#2980b9",
        "places": [
            {"img": b["borghese"], "name": "Вилла Боргезе", "time": "09:00 – 11:30",
             "desc": "Парк бесплатный — идеален для утренней прогулки. Галерея Боргезе внутри — платно (~13–15 €), обязательно бронируйте заранее на galeriaborghese.it (пропускают строго по времени).",
             "lat": 41.9135, "lng": 12.4886},
            {"img": b["navona"], "name": "Пьяцца дель Пополо", "time": "12:00 – 13:30",
             "desc": "Терраса Пинчо — панорама на город. Рядом церковь Santa Maria del Popolo с работами Караваджо.",
             "lat": 41.9109, "lng": 12.4765},
            {"img": b["pantheon"], "name": "Пантеон (вечерний визит)", "time": "15:00 – 16:30",
             "desc": "Вход платный (~5 €, бронь на pantheonroma.com). Вечером меньше людей и красивый свет для фото. Если уже были внутри в День 1 — можно просто посидеть на площади рядом.",
             "lat": 41.8986, "lng": 12.4769},
        ],
        "dinner": {"name": "La Montecarlo", "link": "https://www.tripadvisor.com/Restaurant_Review-g187791-d2326017-Reviews-La_Montecarlo-Rome_Lazio.html",
                   "desc": "У Piazza Navona — тонкая римская пицца (marinara, margherita) + пиво/вино ≈ 12–18 €.",
                   "lat": 41.8992, "lng": 12.4748},
    },
]

# ---- build place cards html ----
cards = []
for d in days:
    items = []
    for p in d["places"]:
        items.append(f'''
        <div class="place">
            <img src="{p['img']}" alt="{p['name']}">
            <div class="info">
                <div class="time">{p['time']}</div>
                <div class="pname">{p['name']}</div>
                <div class="desc">{p['desc']}</div>
            </div>
        </div>''')
    items.append(f'''
        <div class="dinner" style="border-left:5px solid {d['color']}">
            <strong>Ужин (≤ 30 €):</strong>
            <a href="{d['dinner']['link']}" target="_blank">{d['dinner']['name']}</a><br>
            {d['dinner']['desc']}
        </div>''')
    cards.append(f'''
    <div class="day">
        <h2 style="border-bottom:3px solid {d['color']}">{d['title']}</h2>
        <div class="start">🏠 Старт: {HOTEL['name']} ({HOTEL['addr']})</div>
        {''.join(items)}
    </div>''')

# ---- build JS markers + routes ----
js_markers = []
js_routes = []
# hotel marker first
js_markers.append(
    f'L.marker([{HOTEL["lat"]}, {HOTEL["lng"]}], {{icon: homeIcon}}).addTo(map).bindPopup("<b>🏠 {HOTEL["name"]}</b><br>{HOTEL["addr"]}<br>Рейтинг: {HOTEL["rating"]}");')

for day_index, d in enumerate(days, start=1):
    route = [[HOTEL["lat"], HOTEL["lng"]]]  # start from hotel
    for p in d["places"]:
        route.append([p["lat"], p["lng"]])
        js_markers.append(
            f'L.marker([{p["lat"]}, {p["lng"]}]).addTo(map).bindPopup("<b>{p["name"]}</b><br>День {day_index} · {p["time"]}");')
    dn = d["dinner"]
    route.append([dn["lat"], dn["lng"]])
    js_markers.append(
        f'L.marker([{dn["lat"]}, {dn["lng"]}], {{icon: dinnerIcon}}).addTo(map).bindPopup("<b>Ужин: {dn["name"]}</b><br>День {day_index}");')
    js_routes.append(
        f'L.polyline({route}, {{color: "{d["color"]}", weight: 4, opacity: 0.8}}).addTo(map);')

markers_js = "\n        ".join(js_markers)
routes_js = "\n        ".join(js_routes)

html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Рим за 3 дня — бюджетный гид (июль 2026)</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<style>
  * {{ box-sizing: border-box; }}
  body {{ font-family: "Segoe UI", Arial, sans-serif; margin:0; background:#f5f6f8; color:#2c3e50; }}
  header {{ background: linear-gradient(135deg,#c0392b,#e67e22); color:#fff; padding:2.5rem 1rem; text-align:center; }}
  header h1 {{ margin:0 0 .4rem; font-size:2rem; }}
  header p {{ margin:0; opacity:.92; }}
  .hotelbox {{ background:#fff; border-radius:12px; padding:1rem 1.3rem; margin:-1.4rem auto 0; max-width:800px;
              box-shadow:0 4px 14px rgba(0,0,0,.12); position:relative; z-index:5; }}
  .hotelbox b {{ color:#c0392b; }}
  .wrap {{ max-width:1180px; margin:0 auto; padding:1.5rem; }}
  .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(330px,1fr)); gap:1.2rem; }}
  .day {{ background:#fff; border-radius:12px; padding:1.2rem 1.3rem; box-shadow:0 3px 10px rgba(0,0,0,.08); }}
  .day h2 {{ margin:0 0 .8rem; padding-bottom:.4rem; font-size:1.15rem; }}
  .start {{ font-size:.82rem; color:#7f8c8d; margin-bottom:.9rem; background:#fdf3e7; padding:.4rem .6rem; border-radius:6px; }}
  .place {{ display:flex; gap:.8rem; margin-bottom:1rem; }}
  .place img {{ width:130px; height:92px; object-fit:cover; border-radius:8px; flex-shrink:0; }}
  .info {{ flex:1; }}
  .time {{ font-weight:700; color:#7f8c8d; font-size:.82rem; }}
  .pname {{ font-weight:700; margin:.1rem 0; }}
  .desc {{ font-size:.88rem; line-height:1.4; }}
  .dinner {{ background:#eef7ff; border-radius:8px; padding:.8rem; margin-top:.6rem; font-size:.9rem; }}
  .dinner a {{ color:#1a73e8; font-weight:700; text-decoration:none; }}
  #map {{ height:540px; width:100%; border-radius:12px; margin:1.8rem 0; box-shadow:0 3px 10px rgba(0,0,0,.12); }}
  .legend {{ display:flex; gap:1.3rem; flex-wrap:wrap; justify-content:center; margin:.5rem 0 0; font-size:.85rem; }}
  .legend span {{ display:inline-flex; align-items:center; gap:.4rem; }}
  .dot {{ width:13px; height:13px; border-radius:50%; display:inline-block; }}
  .tips {{ background:#fff; border-radius:12px; padding:1.3rem 1.5rem; margin-top:1.5rem; box-shadow:0 3px 10px rgba(0,0,0,.08); }}
  .tips li {{ margin:.4rem 0; }}
  .tickets {{ background:#fff; border-radius:12px; padding:1.3rem 1.5rem; margin-top:1.5rem; box-shadow:0 3px 10px rgba(0,0,0,.08); overflow-x:auto; }}
  .tickets table {{ width:100%; border-collapse:collapse; font-size:.88rem; }}
  .tickets th, .tickets td {{ border-bottom:1px solid #eee; padding:.55rem .6rem; text-align:left; }}
  .tickets th {{ background:#fafafa; color:#c0392b; }}
  .tickets .free {{ color:#27ae60; font-weight:700; }}
  .tickets .paid {{ color:#e67e22; font-weight:700; }}
  footer {{ text-align:center; color:#888; font-size:.85rem; padding:2rem 1rem; }}
</style>
</head>
<body>
<header>
  <h1>Рим за 3 дня</h1>
  <p>Бюджетный маршрут с достопримечательностями, временем визита и ужинами до 30 € на человека.<br>
  Актуально на июль 2026 г. · Источники: Google, TripAdvisor, Booking.com и travel-блоги.</p>
</header>

<div class="hotelbox">
  🏠 <b>Отправная точка каждого дня:</b> {HOTEL['name']} —
  {HOTEL['addr']}<br>
  <span style="color:#27ae60;font-weight:700">Рейтинг {HOTEL['rating']}</span>
  (по оценке гостей, проживавших в отеле).
</div>

<div class="wrap">
  <div class="grid">
    {''.join(cards)}
  </div>

  <h2 style="text-align:center">Карта маршрута</h2>
  <div id="map"></div>
  <div class="legend">
    <span><i class="dot" style="background:#8e44ad"></i> 🏠 Отель (старт)</span>
    <span><i class="dot" style="background:#e74c3c"></i> День 1 — Древний Рим</span>
    <span><i class="dot" style="background:#27ae60"></i> День 2 — Ватикан</span>
    <span><i class="dot" style="background:#2980b9"></i> День 3 — Парк и центр</span>
    <span><i class="dot" style="background:#f1c40f"></i> Ужин</span>
  </div>

  <div class="tickets">
    <h3>Билеты и вход (актуально на 2024–2025 гг., цены ориентировочные)</h3>
    <table>
      <thead><tr><th>Объект</th><th>Вход</th><th>Цена</th><th>Бронь</th></tr></thead>
      <tbody>
        <tr><td>Колизей + Форум + Палатин</td><td class="paid">платно</td><td>~16–18 €</td><td>да (skip-the-line)</td></tr>
        <tr><td>Пантеон</td><td class="paid">платно (с 2023)</td><td>~5 €</td><td>да, pantheonroma.com</td></tr>
        <tr><td>Фонтан Треви</td><td class="free">бесплатно (подход)</td><td>—</td><td>в Google — платные туры от ~2 €</td></tr>
        <tr><td>Vicus Caprarius (подземелья у Треви)</td><td class="paid">платно</td><td>~5–7 €</td><td>нет</td></tr>
        <tr><td>Пьяцца Навона</td><td class="free">бесплатно</td><td>—</td><td>—</td></tr>
        <tr><td>Музеи Ватикана + Сикстинская капелла</td><td class="paid">платно</td><td>~20–30 €</td><td>да (skip-the-line)</td></tr>
        <tr><td>Базилика Св. Петра</td><td class="free">бесплатно</td><td>—</td><td>очередь</td></tr>
        <tr><td>Купол Св. Петра</td><td class="paid">платно</td><td>~8–10 €</td><td>нет</td></tr>
        <tr><td>Трастевере (район)</td><td class="free">бесплатно</td><td>—</td><td>—</td></tr>
        <tr><td>Вилла Боргезе (парк)</td><td class="free">бесплатно</td><td>—</td><td>—</td></tr>
        <tr><td>Галерея Боргезе</td><td class="paid">платно</td><td>~13–15 €</td><td>да, galeriaborghese.it</td></tr>
        <tr><td>Пьяцца дель Пополо</td><td class="free">бесплатно</td><td>—</td><td>—</td></tr>
      </tbody>
    </table>
    <p style="font-size:.8rem;color:#888;margin:.6rem 0 0">Точные цены и часы работы проверяйте на официальных сайтах перед поездкой — к 2026 г. возможны небольшие изменения. Roma Pass (48 ч) покрывает первые 2 платных объекта бесплатно.</p>
  </div>

  <div class="tips">
    <h3>Полезные советы</h3>
    <ul>
      <li><b>Roma Pass (48 ч)</b> — бесплатный вход в первые 2 музея/объекта + неограниченный проезд на транспорте.</li>
      <li>Вода из фонтанов-nasoni питьевая и бесплатная — берите бутылку с собой.</li>
      <li>Ужины ищите в стороне от туристических улиц (Трастевере, Тестаччо, Сан-Лоренцо) — дешевле и вкуснее.</li>
      <li>Билеты в Колизей и Ватикан бронируйте онлайн заранее — экономия времени в очереди.</li>
      <li>Маршруты на карте построены по времени визита и начинаются от отеля — проверьте логику перемещений.</li>
      <li>Цены указаны ориентировочно (по состоянию на 2024–2025 гг.) и могут незначительно меняться к 2026 г.</li>
    </ul>
  </div>
</div>

<footer>С любовью к путешествиям — ваш помощник Герми.</footer>

<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
  const map = L.map('map').setView([41.903, 12.476], 13);
  L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
    maxZoom: 19, attribution: '&copy; OpenStreetMap'
  }}).addTo(map);

  const homeIcon = L.divIcon({{
    className: '', html: '<div style="background:#8e44ad;width:18px;height:18px;border-radius:50%;border:2px solid #fff;display:flex;align-items:center;justify-content:center;font-size:11px;">🏠</div>',
    iconSize: [18,18], iconAnchor: [9,9]
  }});
  const dinnerIcon = L.divIcon({{
    className: '', html: '<div style="background:#f1c40f;width:14px;height:14px;border-radius:3px;border:2px solid #fff;"></div>',
    iconSize: [14,14]
  }});

  // маркеры
  {markers_js}

  // маршруты по дням (начало = отель, далее по времени визита)
  {routes_js}
</script>
</body>
</html>'''

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(html)

print("WROTE", OUT_HTML, os.path.getsize(OUT_HTML), "bytes")
