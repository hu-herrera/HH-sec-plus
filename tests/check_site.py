from html.parser import HTMLParser
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
html = (ROOT / "index.html").read_text(encoding="utf-8")
css = (ROOT / "assets/styles.css").read_text(encoding="utf-8")
thanks = (ROOT / "gracias.html").read_text(encoding="utf-8")
privacy = (ROOT / "privacidad.html").read_text(encoding="utf-8")

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.refs = []
        self.meta = []
        self.h1 = 0
        self.local_files = []
        self.forms = []
        self.fields = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs: self.ids.add(attrs["id"])
        if tag == "h1": self.h1 += 1
        if tag == "meta": self.meta.append(attrs)
        if tag == "a" and attrs.get("href", "").startswith("#"):
            self.refs.append(attrs["href"][1:])
        if tag == "link" and attrs.get("href") and not attrs["href"].startswith("http"):
            self.local_files.append(attrs["href"].split("?", 1)[0])
        if tag == "img":
            assert not attrs.get("src", "").startswith(("http", "//")), "Imágenes servidas desde el propio sitio (CSP img-src 'self')"
            self.local_files.append(attrs["src"].split("?", 1)[0])
        if tag == "form": self.forms.append(attrs)
        if tag in ("input", "textarea"): self.fields.append(attrs)

p=Parser()
p.feed(html)
assert p.h1 == 1
assert all(x in p.ids for x in p.refs), "Anclas internas sin destino"
assert any(x.get("name") == "description" and 60 <= len(x.get("content", "")) <= 170 for x in p.meta)
assert any(x.get("property") == "og:title" for x in p.meta)
assert any(x.get("property") == "og:description" for x in p.meta)
assert '<link rel="canonical"' in html
assert 'application/ld+json' in html
assert all((ROOT / x).is_file() for x in p.local_files)
assert "prefers-reduced-motion" in css
assert "@media(max-width:640px)" in css
assert len(p.forms) == 1 and p.forms[0].get("method") == "POST"
assert p.forms[0].get("action","").startswith("https://formsubmit.co/")
assert {x.get("name") for x in p.fields} >= {"name", "email", "message", "_honey", "_next"}
assert all(any(x.get("name") == n and "required" in x for x in p.fields) for n in ("name","email","message"))
assert "Gracias" in thanks
assert "linkedin.com" not in html and "mailto:" not in html and "@outlook" not in html, "No exponer el correo"
assert "Financiera Pacífico" not in html
assert "credenciales" in p.ids
assert "fonts.googleapis.com" not in html + css, "Fuentes deben servirse desde el propio sitio"
assert (ROOT / "assets/fonts/dm-sans-latin-wght.woff2").is_file()
assert 'href="privacidad.html"' in html and "FormSubmit" in privacy
assert (ROOT / "404.html").is_file()
assert "Content-Security-Policy" in (ROOT / ".htaccess").read_text() and "Content-Security-Policy" in (ROOT / "_headers").read_text()
terms = (ROOT / "condiciones.html").read_text(encoding="utf-8")
assert 'href="condiciones.html"' in html and 'href="condiciones.html"' in privacy, "Enlazar las condiciones de servicio"
assert "autorización escrita" in terms and "condiciones.html" in (ROOT / "sitemap.xml").read_text()
ld = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
assert {json.loads(x)["@type"] for x in ld} == {"ProfessionalService", "FAQPage"}, "JSON-LD válido de empresa y preguntas"
faq_ld = next(json.loads(x) for x in ld if '"FAQPage"' in x)
assert len(faq_ld["mainEntity"]) == html.count('class="faq-item"'), "Preguntas del JSON-LD y del HTML deben coincidir"
print("OK: estructura, SEO, enlaces, formulario, privacidad, condiciones, fuentes locales y cabeceras.")
