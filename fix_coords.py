import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(HERE, "coords.json")
with open(p, encoding="utf-8") as f:
    d = json.load(f)

# fix wrong / fill missing with known-good coords
fixes = {
    "doria_pamphilj": {"lat": 41.8976, "lng": 12.4805, "display": "Galleria Doria Pamphilj, Via del Corso, Roma"},
    "quadrighe": {"lat": 41.9107, "lng": 12.4835, "display": "Terrazza delle Quadrighe, Palazzo delle Esposizioni, Roma"},
    "aventino": {"lat": 41.8827, "lng": 12.4833, "display": "Terrazza Belvedere Aventino, Giardino degli Aranci, Roma"},
    "pamphilj": {"lat": 41.8989, "lng": 12.4731, "display": "Palazzo Pamphilj, Piazza Navona, Roma"},
    "santa_maria_popolo": {"lat": 41.9109, "lng": 12.4765, "display": "Santa Maria del Popolo, Piazza del Popolo, Roma"},
}
for k, v in fixes.items():
    d[k] = v

with open(p, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print("FIXED. keys:", len(d))
for k, v in d.items():
    print(f"  {k}: {v['lat']}, {v['lng']}")
