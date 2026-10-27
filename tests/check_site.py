from html.parser import HTMLParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
html = (ROOT / "index.html").read_text(encoding="utf-8")
css = (ROOT / "assets/styles.css").read_text(encoding="utf-8")

class Check(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.internal_refs = []
        self.meta = []
        self.h1 = 0
        self.images = []
        self.files = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "h1": self.h1 += 1
        if tag == "meta": self.meta.append(attrs)
        if tag == "a" and attrs.get("href", "").startswith("#"):
            self.internal_refs.append(attrs["href"][1:])
        if tag == "link" and attrs.get("href") and not attrs["href"].startswith("http"):
            self.files.append(attrs["href"])
        if tag == "img":
            self.images.append(attrs)

p = Check()
p.feed(html)
assert p.h1 == 1, f"Se esperaba 1 H1, hay {p.h1}"
assert all(x in p.ids for x in p.internal_refs), "Anclas internas sin destino"
assert any(x.get("name") == "description" and 60 <= len(x.get("content", "")) <= 170 for x in p.meta), "Meta descripción ausente o demasiado larga"
assert any(x.get("property") == "og:title" for x in p.meta), "OG title ausente"
assert any(x.get("property") == "og:description" for x in p.meta), "OG description ausente"
assert 'application/ld+json' in html, "JSON-LD ausente"
assert all((ROOT / x).is_file() for x in p.files), "Recursos locales faltantes"
assert "@media(max-width:600px)" in css, "Faltan reglas móviles"
assert "prefers-reduced-motion" in css, "Falta opción de movimiento reducido"
assert "hu.herrera@outlook.com" in html, "Falta contacto"
assert "Financiera Pacífico" not in html and "Financiera Pacífico" not in (ROOT / "linkedin/primer-post.md").read_text(), "No divulgar la tesis"
text = (ROOT / "linkedin/descripcion-exacta.txt").read_text().strip()
assert text.startswith("HH sec+ fusiona") and text.endswith("hugo-herrera-redes."), "El brief debe conservarse"
post = (ROOT / "linkedin/primer-post.md").read_text(encoding="utf-8")
words = re.findall(r"\b[\wÁÉÍÓÚÜÑáéíóúüñ]+\b", re.sub(r"[#*]", "", post), flags=re.UNICODE)
assert 300 <= len(words) <= 500, f"Publicación fuera del rango solicitado: {len(words)} palabras"
print(f"OK: contenido, anclas, SEO, accesibilidad, recursos y privacidad. Post: {len(words)} palabras.")
