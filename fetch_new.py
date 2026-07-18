import json, urllib.request, urllib.parse, os, time

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "images")
API = "https://commons.wikimedia.org/w/api.php"

terms = {
    "doria_pamphilj.jpg": "Doria Pamphilj gallery Rome",
    "colonna.jpg": "Palazzo Colonna Rome",
    "aventino.jpg": "Giardino degli Aranci Rome",
    "altemps.jpg": "Palazzo Altemps Rome",
    "teatro_marcello.jpg": "Theatre of Marcellus Rome",
    "santa_maria_maggiore.jpg": "Basilica Santa Maria Maggiore Rome",
    "barberini.jpg": "Palazzo Barberini Rome",
    "via_margutta.jpg": "Via Margutta Rome",
    "barcaccia.jpg": "Fontana della Barcaccia Rome",
    "fontana_moro.jpg": "Fontana del Moro Rome",
    "santa_maria_popolo.jpg": "Santa Maria del Popolo Rome",
    "san_luigi.jpg": "San Luigi dei Francesi Rome",
    "santi_giovanni_paolo.jpg": "Santi Giovanni e Paolo Rome",
    "torre_argentina.jpg": "Largo di Torre Argentina Rome",
}

def api_get(params):
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "RomeGuideBot/1.0 (mary@example.com)"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.load(r)

for i, (out, q) in enumerate(terms.items()):
    if i > 0:
        time.sleep(4)
    params = {"action":"query","generator":"search","gsrsearch":q,"gsrnamespace":"6",
              "gsrlimit":"5","prop":"imageinfo","iiprop":"url|mime","iiurlwidth":"800","format":"json"}
    try:
        data = api_get(params)
        pages = data.get("query",{}).get("pages",{})
        items = sorted(pages.values(), key=lambda v: v.get("index",0))
        thumb = None
        for it in items:
            ii = it.get("imageinfo",[{}])[0]
            if ii.get("mime","").startswith("image") and ii.get("thumburl"):
                thumb = ii["thumburl"]; break
        if not thumb:
            print(f"{out}: NO url"); continue
        time.sleep(2)
        req = urllib.request.Request(thumb, headers={"User-Agent":"RomeGuideBot/1.0"})
        with urllib.request.urlopen(req, timeout=60) as r:
            raw = r.read()
        with open(os.path.join(IMG, out),"wb") as f:
            f.write(raw)
        print(f"{out}: OK {len(raw)}")
    except Exception as e:
        print(f"{out}: ERR {e}")
print("DONE")
