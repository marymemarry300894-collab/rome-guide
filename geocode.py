import urllib.request, json, urllib.parse, time, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "coords.json")
NOM = "https://nominatim.openstreetmap.org/search?"

queries = {
    "doria_pamphilj": "Doria Pamphilj Gallery, Roma",
    "appetito": "Appetito Pizza Gourmet, Roma",
    "colonna": "Palazzo Colonna, Roma",
    "quadrighe": "Terrazza delle Quadrighe, Roma",
    "aventino": "Terrazza Belvedere Aventino, Roma",
    "altemps": "Palazzo Altemps, Roma",
    "teatro_marcello": "Teatro di Marcello, Roma",
    "torre_argentina": "Largo di Torre Argentina, Roma",
    "pamphilj": "Palazzo Pamphilj, Piazza Navona, Roma",
    "mattei": "Palazzo Mattei, Roma",
    "via_margutta": "Via Margutta, Roma",
    "barberini": "Palazzo Barberini, Roma",
    "santa_maria_popolo": "Santa Maria del Popolo, Roma",
    "san_luigi": "San Luigi dei Francesi, Roma",
    "santi_giovanni_paolo": "Santi Giovanni e Paolo, Roma",
    "santa_maria_maggiore": "Basilica Santa Maria Maggiore, Roma",
    "fontana_api": "Fontana delle Api, Roma",
    "barcaccia": "Fontana della Barcaccia, Roma",
    "fontana_moro": "Fontana del Moro, Roma",
}

def geocode(q):
    url = NOM + urllib.parse.urlencode({"q": q, "format": "json", "limit": 1})
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    })
    with urllib.request.urlopen(req, timeout=15) as r:
        d = json.load(r)
    if d:
        return {"lat": float(d[0]["lat"]), "lng": float(d[0]["lon"]), "display": d[0].get("display_name")}
    return None

res = {}
for key, q in queries.items():
    try:
        g = geocode(q)
        res[key] = g
        print(f"{key}: {g}")
    except Exception as e:
        res[key] = None
        print(f"{key}: ERR {e}")
    time.sleep(1.1)

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=2)
print("SAVED", OUT)
