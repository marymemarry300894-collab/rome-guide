import base64, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "images")
OUT = os.path.join(HERE, "index.html")
with open(os.path.join(HERE, "coords.json"), encoding="utf-8") as f:
    COORDS = json.load(f)

def c(key):
    return COORDS[key]["lat"], COORDS[key]["lng"]

def b64(name):
    p = os.path.join(IMG, name)
    with open(p, "rb") as f:
        return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()

IM = {
    "doria": b64("doria_pamphilj.jpg"),
    "appetito": b64("appetito.jpg") if os.path.exists(os.path.join(IMG,"appetito.jpg")) else None,
    "colonna": b64("colonna.jpg"),
    "quadrighe": b64("quadrighe.jpg") if os.path.exists(os.path.join(IMG,"quadrighe.jpg")) else None,
    "aventino": b64("aventino.jpg"),
    "altemps": b64("altemps.jpg"),
    "marcello": b64("teatro_marcello.jpg"),
    "torre": b64("torre_argentina.jpg"),
    "pamphilj": b64("pamphilj.jpg") if os.path.exists(os.path.join(IMG,"pamphilj.jpg")) else None,
    "mattei": b64("mattei.jpg") if os.path.exists(os.path.join(IMG,"mattei.jpg")) else None,
    "margutta": b64("via_margutta.jpg"),
    "barberini": b64("barberini.jpg"),
    "popolo": b64("santa_maria_popolo.jpg"),
    "luigi": b64("san_luigi.jpg"),
    "giovanni": b64("santi_giovanni_paolo.jpg"),
    "maggiore": b64("santa_maria_maggiore.jpg"),
    "api": b64("fontana_api.jpg") if os.path.exists(os.path.join(IMG,"fontana_api.jpg")) else None,
    "barcaccia": b64("barcaccia.jpg"),
    "moro": b64("fontana_moro.jpg"),
    "colosseum": b64("colosseum.jpg"),
    "forum": b64("forum.jpg"),
    "palatine": b64("palatine.jpg"),
    "pantheon": b64("pantheon.jpg"),
    "trevi": b64("trevi.jpg"),
    "navona": b64("navona.jpg"),
    "vatican": b64("vatican_museums.jpg"),
    "stpeter": b64("stpeter.jpg"),
    "trastevere": b64("trastevere.jpg"),
    "borghese": b64("borghese.jpg"),
}

HOTEL = {"name":"Hotel Villa Pinciana","addr":"Via Abruzzi 11, Виа Венето, 00187 Рим",
         "rating":"9.2 / 10 (на основе 442 отзывов)","lat":41.9090525,"lng":12.4921677}

def img(key):
    return IM.get(key) or IM.get("pantheon")

BREAKFAST = {"img": None, "name":"🍳 ЗАВТРАК в отеле (Hotel Villa Pinciana)",
             "time":"08:00 – 09:00", "desc":"Возврат в отель к 8:00 на завтрак. Передохни, зарядись кофе и энергией перед второй половиной дня пешком.",
             "lat":HOTEL["lat"], "lng":HOTEL["lng"], "is_breakfast":True}

# ---- itinerary: each full day = morning (4-8) + breakfast + after ----
days = [
 {
  "date":"29 августа (чт) — вечер прилёта",
  "mode":"Прилёт после 16:00 · лёгкий вечерний разогрев пешком",
  "color":"#8e44ad",
  "morning":[],
  "after":[
    {"img":img("popolo"),"name":"Пьяцца дель Пополо + Санта-Мария-дель-Пополо","time":"16:30 – 17:30",
     "desc":"Старт у отеля. Пьяцца дель Пополо — главные ворота Рима, рядом базилика с работами Караваджо. Терраса Пинчо — вид на город вечером.","lat":41.9109,"lng":12.4765},
    {"img":img("margutta"),"name":"Via Margutta","time":"17:30 – 18:15",
     "desc":"Тихая творческая улица художников, в 2 минутах от Пьяцца дель Пополо. Уютно и без толпы.","lat":41.9086,"lng":12.4795},
    {"img":img("barcaccia"),"name":"Испанская лестница + Фонтан Barcaccia","time":"18:15 – 19:00",
     "desc":"Поднимитесь по Испанской лестнице, у её подножья — фонтан-лодка Barcaccia (Бернини).","lat":41.9058,"lng":12.4822},
    {"img":img("doria"),"name":"Галерея Дориа-Памфилj (вечерний осмотр снаружи)","time":"19:00 – 19:45",
     "desc":"Одна из лучших частных коллекций Рима. Вечером у фасада на Via del Corso приятно постоять. Если успеваете — билет на утро 30.08.","lat":41.8976,"lng":12.4805},
    {"img":img("appetito"),"name":"Ужин: Appetito Pizza Gourmet","time":"20:00 – 21:30",
     "desc":"Пиццерия 4,8★ (Via dei Gracchi, район Прати). Или вернитесь ближе к центру — выбор за вами.","lat":41.9097,"lng":12.4572},
  ],
 },
 {
  "date":"30 августа (пт) — полный день, античный Рим + дворцы",
  "mode":"Подъём в 4:00 · 8:00 завтрак в отеле · пешком до ~22:00",
  "color":"#e74c3c",
  "morning":[
    {"img":img("colosseum"),"name":"Колизей (рассвет)","time":"04:00 – 05:30",
     "desc":"Приходите к открытию неба — пусто, прохладно, идеальный свет. Билет комбо с Форумом+Палатином (~16–18 €, бронь онлайн).","lat":41.8902,"lng":12.4922},
    {"img":img("forum"),"name":"Римский Форум + Палатин","time":"05:30 – 07:00",
     "desc":"Сердце древнего Рима. Идите от Колизея к Палатину для панорамы, затем выходите к центру по пути домой.","lat":41.8919,"lng":12.4853},
    {"img":img("torre"),"name":"Театр Марцелла + Торре-Арджентина (по пути к отелю)","time":"07:00 – 07:45",
     "desc":"Древний амфитеатр и Ларго ди Торре-Арджентина — на пути обратно к отелю. К 8:00 будешь на завтраке.","lat":41.896,"lng":12.4768},
  ],
  "after":[
    {"img":img("altemps"),"name":"Палаццо Альтемпс","time":"09:00 – 10:00",
     "desc":"Филиал Национального музея Рима, великолепная античная скульптура. Билет ~12 € (входит в Roma Pass).","lat":41.9012,"lng":12.4731},
    {"img":img("pantheon"),"name":"Пантеон (прогулка, билет 31-го)","time":"10:00 – 10:30",
     "desc":"Подойдите к фасаду, посмотрите на площадь. Сам вход — по купленному билету 31.08 в 11:00.","lat":41.8986,"lng":12.4769},
    {"img":img("moro"),"name":"Пьяцца Навона + Фонтан Мавра + Палаццо Памфилj","time":"10:30 – 12:00",
     "desc":"Барочная площадь, фонтаны Бернини. Palazzo Pamphilj на площади — резиденция Бразилии.","lat":41.8981,"lng":12.4732},
    {"img":img("mattei"),"name":"Палаццо Маттеи + Еврейский гетто (обед)","time":"12:00 – 13:30",
     "desc":"Район гетто: Палаццо Маттеи, Портико д'Отавия. Обед в гетто (карпаччо, артишоки по-еврейски).","lat":41.8945,"lng":12.4781},
    {"img":img("api"),"name":"Фонтан Пчёл + Дворец Барберини","time":"13:30 – 14:30",
     "desc":"Маленький фонтан Пчёл (Бернини) у площади Барберини. Дворец Барберини — галерея (~12 €).","lat":41.9043,"lng":12.4888},
    {"img":img("colonna"),"name":"Дворец Колонна","time":"14:30 – 16:00",
     "desc":"Галерея 4,9★ — один из самых красивых частных дворцов. Открыт только по субботам с 9:00 (30.08 — суббота, попадает!). Билет ~12 €.","lat":41.8979,"lng":12.4841},
    {"img":img("trastevere"),"name":"Трастевере + ужин","time":"16:00 – 19:00",
     "desc":"Живописный район, площадь Santa Maria in Trastevere. Ужин в trattoria (≤30 €).","lat":41.889,"lng":12.4691},
    {"img":img("borghese"),"name":"Вилла Боргезе (парк, вечер)","time":"19:00 – 21:00",
     "desc":"Парк бесплатно, вечерняя прогулка к террасе Пинчо.","lat":41.9135,"lng":12.4886},
  ],
 },
 {
  "date":"31 августа (сб) — ДЕНЬ БИЛЕТОВ: Пантеон 11:00 + Ватикан 17:00",
  "mode":"Подъём в 4:00 · 8:00 завтрак в отеле · жёсткие привязки по билетам",
  "color":"#27ae60",
  "morning":[
    {"img":img("maggiore"),"name":"Санта-Мария-Маджоре","time":"04:00 – 05:15",
     "desc":"Одна из четырёх главных базилик Рима (4,8★, 56k отзывов). Ранним утром пустая и торжественная.","lat":41.8976,"lng":12.4985},
    {"img":img("luigi"),"name":"Сан-Луиджи-деи-Франчези","time":"05:15 – 06:00",
     "desc":"Французская церковь с тремя шедеврами Караваджо (зал св. Матфея). Бесплатно.","lat":41.8996,"lng":12.4745},
    {"img":img("giovanni"),"name":"Санти-Джованни-э-Паоло (Целий)","time":"06:00 – 07:00",
     "desc":"Базилика на холме Целий с садами и видом. Рядом — вход к дому св. Климента.","lat":41.8865,"lng":12.4921},
    {"img":img("aventino"),"name":"Терраса Авентино (Giardino degli Aranci)","time":"07:00 – 07:45",
     "desc":"Смотровая 4,8★ — вид на купол Св. Петра сквозь апельсиновый сад. Бесплатно, открыто с рассвета. Затем путь к отелю к 8:00.","lat":41.8827,"lng":12.4833},
  ],
  "after":[
    {"img":img("trevi"),"name":"Фонтан Треви (ранняя толпа меньше)","time":"09:00 – 10:00",
     "desc":"Подойти бесплатно. Кинь монетку на возвращение. В Google есть платные туры от ~2 € — опционально.","lat":41.9009,"lng":12.4833},
    {"img":img("pantheon"),"name":"ПАНТЕОН (КУПЛЕННЫЙ БИЛЕТ 11:00)","time":"10:30 – 12:00",
     "desc":"Вход платный (~5 €), бронь на pantheonroma.com на 31.08 11:00. Приходите за 15 мин. Купол с окулюсом — обязательно.","lat":41.8986,"lng":12.4769},
    {"img":img("doria"),"name":"Обед + Галерея Дориа-Памфилj","time":"12:00 – 14:30",
     "desc":"Обед рядом, затем галерея (если не были 29-го). Зал зеркал и «Отдых на пути в Египет» Караваджо.","lat":41.8976,"lng":12.4805},
    {"img":img("navona"),"name":"Пеший путь к Ватикану (Via dei Coronari)","time":"14:30 – 16:30",
     "desc":"Прогулка через исторический центр: Пьяцца Навона, Понте Сант-Анджело к Ватикану. ~2,5 км, пешком.","lat":41.8994,"lng":12.4765},
    {"img":img("vatican"),"name":"ВАТИКАН: Музеи + Сикстинская капелла (БИЛЕТ 17:00)","time":"17:00 – 20:00",
     "desc":"Вход платный (~20–30 €), бронь на 31.08 17:00. Включает Сикстинскую капеллу. После — площадь Св. Петра вечером.","lat":41.9065,"lng":12.4536},
    {"img":img("stpeter"),"name":"Базилика Св. Петра (вечер)","time":"20:00 – 21:00",
     "desc":"Бесплатный вход вечером, очередь меньше. Купол платный (~8–10 €, днём).","lat":41.9022,"lng":12.4534},
    {"img":img("trastevere"),"name":"Ужин в Трастевере","time":"21:00 – 22:30",
     "desc":"Финал дня — ужин в trattoria (≤30 €).","lat":41.889,"lng":12.4691},
  ],
 },
 {
  "date":"1 сентября (вт) — финальное утро, выезд до 11:00",
  "mode":"Подъём в 4:00 · 8:00 завтрак в отеле · всё закончить к 11:00",
  "color":"#2980b9",
  "morning":[
    {"img":img("quadrighe"),"name":"Terrazza delle Quadrighe (рассвет)","time":"04:00 – 05:00",
     "desc":"Смотровая 4,6★ на крыше Palazzo delle Esposizioni — панорама Рима на рассвете. Проверь часы открытия.","lat":41.9107,"lng":12.4835},
    {"img":img("trevi"),"name":"Фонтан Треви (пустой!)","time":"05:00 – 06:00",
     "desc":"В 5 утра фонтан почти пустой — лучшее время для фото и монетки.","lat":41.9009,"lng":12.4833},
    {"img":img("torre"),"name":"Прогулка центром: Торре-Арджентина, Пантеон снаружи","time":"06:00 – 07:30",
     "desc":"Спокойный утренний Рим. Заскочите на площадь перед Пантеоном ещё раз по пути домой.","lat":41.896,"lng":12.4768},
  ],
  "after":[
    {"img":img("appetito"),"name":"Прогулка/кофе: Appetito Pizza Gourmet","time":"09:00 – 10:00",
     "desc":"Последняя пицца/кофе перед отъездом (4,8★).","lat":41.9097,"lng":12.4572},
    {"img":img("popolo"),"name":"Возврат в отель, сборы к выезду 11:00","time":"10:00 – 11:00",
     "desc":"Путь к отелю (Via Abruzzi 11), сборы к выезду в 11:00.","lat":41.9091,"lng":12.4922},
  ],
 },
]

# cards
cards = []
for d in days:
    blocks = []
    for p in d.get("morning", []):
        blocks.append(f'''
        <div class="place">
            <img src="{p['img']}" alt="{p['name']}">
            <div class="info">
                <div class="time">{p['time']}</div>
                <div class="pname">{p['name']}</div>
                <div class="desc">{p['desc']}</div>
            </div>
        </div>''')
    if d.get("morning"):
        blocks.append(f'''
        <div class="breakfast">
            <div class="time">{BREAKFAST['time']}</div>
            <div class="pname">{BREAKFAST['name']}</div>
            <div class="desc">{BREAKFAST['desc']}</div>
        </div>''')
    for p in d.get("after", []):
        blocks.append(f'''
        <div class="place">
            <img src="{p['img']}" alt="{p['name']}">
            <div class="info">
                <div class="time">{p['time']}</div>
                <div class="pname">{p['name']}</div>
                <div class="desc">{p['desc']}</div>
            </div>
        </div>''')
    cards.append(f'''
    <div class="day">
        <h2 style="border-bottom:3px solid {d['color']}">{d['date']}</h2>
        <div class="mode">🚶 {d['mode']}</div>
        <div class="start">🏠 Отель: {HOTEL['name']} ({HOTEL['addr']})</div>
        {''.join(blocks)}
    </div>''')

# JS markers + routes
js_markers = [f'L.marker([{HOTEL["lat"]}, {HOTEL["lng"]}], {{icon: homeIcon}}).addTo(map).bindPopup("<b>🏠 {HOTEL["name"]}</b><br>{HOTEL["addr"]}<br>Рейтинг: {HOTEL["rating"]}");']
js_routes = []
for di, d in enumerate(days, 1):
    route = [[HOTEL["lat"], HOTEL["lng"]]]
    for p in d.get("morning", []):
        route.append([p["lat"], p["lng"]])
        js_markers.append(f'L.marker([{p["lat"]}, {p["lng"]}]).addTo(map).bindPopup("<b>{p["name"]}</b><br>{d["date"].split(" — ")[0]} · {p["time"]}");')
    if d.get("morning"):
        route.append([HOTEL["lat"], HOTEL["lng"]])  # return for breakfast
        js_markers.append(f'L.marker([{HOTEL["lat"]}, {HOTEL["lng"]}], {{icon: homeIcon}}).addTo(map).bindPopup("<b>🍳 Завтрак в отеле</b><br>{HOTEL["addr"]}<br>08:00");')
    for p in d.get("after", []):
        route.append([p["lat"], p["lng"]])
        js_markers.append(f'L.marker([{p["lat"]}, {p["lng"]}]).addTo(map).bindPopup("<b>{p["name"]}</b><br>{d["date"].split(" — ")[0]} · {p["time"]}");')
    js_routes.append(f'L.polyline({route}, {{color:"{d["color"]}", weight:4, opacity:0.8}}).addTo(map);')
markers_js = "\n        ".join(js_markers)
routes_js = "\n        ".join(js_routes)

html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Рим 29.08–01.09 2026 — персональный пеший гид</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<style>
  * {{ box-sizing: border-box; }}
  body {{ font-family: "Segoe UI", Arial, sans-serif; margin:0; background:#f5f6f8; color:#2c3e50; }}
  header {{ background: linear-gradient(135deg,#c0392b,#e67e22); color:#fff; padding:2.5rem 1rem; text-align:center; }}
  header h1 {{ margin:0 0 .4rem; font-size:2rem; }}
  header p {{ margin:0; opacity:.92; }}
  .hotelbox {{ background:#fff; border-radius:12px; padding:1rem 1.3rem; margin:-1.4rem auto 0; max-width:820px; box-shadow:0 4px 14px rgba(0,0,0,.12); position:relative; z-index:5; }}
  .hotelbox b {{ color:#c0392b; }}
  .wrap {{ max-width:1180px; margin:0 auto; padding:1.5rem; }}
  .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(340px,1fr)); gap:1.2rem; }}
  .day {{ background:#fff; border-radius:12px; padding:1.2rem 1.3rem; box-shadow:0 3px 10px rgba(0,0,0,.08); }}
  .day h2 {{ margin:0 0 .5rem; padding-bottom:.4rem; font-size:1.1rem; }}
  .mode {{ font-size:.82rem; color:#fff; background:#34495e; padding:.3rem .6rem; border-radius:6px; display:inline-block; margin-bottom:.6rem; }}
  .start {{ font-size:.8rem; color:#7f8c8d; margin-bottom:.7rem; background:#fdf3e7; padding:.4rem .6rem; border-radius:6px; }}
  .place {{ display:flex; gap:.8rem; margin-bottom:.9rem; }}
  .place img {{ width:120px; height:85px; object-fit:cover; border-radius:8px; flex-shrink:0; }}
  .info {{ flex:1; }}
  .time {{ font-weight:700; color:#7f8c8d; font-size:.8rem; }}
  .pname {{ font-weight:700; margin:.05rem 0; font-size:.92rem; }}
  .desc {{ font-size:.84rem; line-height:1.35; }}
  .breakfast {{ background:#e8f8e8; border-left:5px solid #27ae60; border-radius:8px; padding:.7rem .9rem; margin:.6rem 0; }}
  .breakfast .pname {{ color:#1e8449; }}
  #map {{ height:560px; width:100%; border-radius:12px; margin:1.8rem 0; box-shadow:0 3px 10px rgba(0,0,0,.12); }}
  .legend {{ display:flex; gap:1.1rem; flex-wrap:wrap; justify-content:center; margin:.5rem 0 0; font-size:.82rem; }}
  .legend span {{ display:inline-flex; align-items:center; gap:.4rem; }}
  .dot {{ width:12px; height:12px; border-radius:50%; display:inline-block; }}
  .tips {{ background:#fff; border-radius:12px; padding:1.3rem 1.5rem; margin-top:1.5rem; box-shadow:0 3px 10px rgba(0,0,0,.08); }}
  .tips li {{ margin:.4rem 0; }}
  footer {{ text-align:center; color:#888; font-size:.85rem; padding:2rem 1rem; }}
</style>
</head>
<body>
<header>
  <h1>Рим · 29.08 – 01.09 2026</h1>
  <p>Персональный пеший маршрут по твоему списку Google · подъём в 4:00, завтрак в отеле в 8:00, возврат ~21–22:00<br>
  Отель: Hotel Villa Pinciana (Via Abruzzi 11) · билеты: Пантеон 31.08 11:00, Ватикан 31.08 17:00</p>
</header>

<div class="hotelbox">
  🏠 <b>Отправная точка и завтрак:</b> {HOTEL['name']} — {HOTEL['addr']}<br>
  <span style="color:#27ae60;font-weight:700">Рейтинг {HOTEL['rating']}</span> · каждый день возврат к 8:00 на завтрак
</div>

<div class="wrap">
  <div class="grid">
    {''.join(cards)}
  </div>

  <h2 style="text-align:center">Карта маршрута (пеший, с возвратом на завтрак)</h2>
  <div id="map"></div>
  <div class="legend">
    <span><i class="dot" style="background:#8e44ad"></i> 29.08 вечер</span>
    <span><i class="dot" style="background:#e74c3c"></i> 30.08 полный день</span>
    <span><i class="dot" style="background:#27ae60"></i> 31.08 билеты</span>
    <span><i class="dot" style="background:#2980b9"></i> 01.09 утро</span>
    <span><i class="dot" style="background:#f1c40f"></i> 🏠 Отель / завтрак</span>
  </div>

  <div class="tips">
    <h3>Советы для режима 4:00 – 8:00 завтрак – 22:00</h3>
    <ul>
      <li><b>Завтрак в отеле в 8:00 каждый полный день</b> — утренняя сессия (4:00–8:00) строится так, чтобы ты успела вернуться пешком к отелю к 8:00.</li>
      <li>Удобная обувь — за день будет 20–30 км пешком. Бери воду (фонтаны-nasoni бесплатны).</li>
      <li>Ранние старты (4:00) — лучший свет и пустые площади (Треви в 5 утра — почти никого).</li>
      <li>Жёсткие точки: <b>Пантеон 31.08 11:00</b> и <b>Ватикан 31.08 17:00</b> — не пропусти, билеты куплены.</li>
      <li>Дворец Колонна открыт только по субботам (30.08 попадает) — план учёл.</li>
      <li>Смотровые Авентино и Quadrighe — проверь часы открытия (некоторые работают с 9–10).</li>
      <li>Маршруты на карте петляют через отель в 8:00 (завтрак).</li>
    </ul>
  </div>
</div>

<footer>Твой персональный гид, Мари · с любовью к путешествиям.</footer>

<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
  const map = L.map('map').setView([41.903, 12.476], 13);
  L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{{{y}}}}.png', {{ maxZoom:19, attribution:'&copy; OpenStreetMap' }}).addTo(map);
  const homeIcon = L.divIcon({{ className:'', html:'<div style="background:#f1c40f;width:18px;height:18px;border-radius:50%;border:2px solid #fff;display:flex;align-items:center;justify-content:center;font-size:11px;">🏠</div>', iconSize:[18,18], iconAnchor:[9,9] }});
  {markers_js}
  {routes_js}
</script>
</body>
</html>'''

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)
print("WROTE", OUT, os.path.getsize(OUT), "bytes")
