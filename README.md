# HH sec+

**Tu red: diseñada para funcionar, asegurada para durar.**

Sitio estático de presentación de servicios de **HH sec+**, consultoría de redes informáticas, ciberseguridad, infraestructura TI y optimización para PyMEs en Chile.

## Estructura

- `index.html`: página principal, metadatos de SEO, Open Graph y JSON-LD.
- `assets/styles.css`: diseño responsivo sin dependencia de frameworks.
- `assets/favicon.svg` y `assets/social-card.svg`: recursos de identidad visual iniciales.
- `linkedin/descripcion-exacta.txt`: descripción para Company Page, copiada literalmente del brief.
- `linkedin/primer-post.md`: publicación de lanzamiento (2026).
- `robots.txt`: indexación permitida.
- `tests/check_site.py`: comprobaciones automáticas básicas.

## Pruebas locales

```sh
python3 -m http.server 8000
# abrir http://localhost:8000
python3 tests/check_site.py
```

## Publicación (GitHub Pages)

1. Repositorio creado: [`hu-herrera/HH-sec-`](https://github.com/hu-herrera/HH-sec-).
2. Contenido publicado en la rama `main`.
3. En [`Settings > Pages`](https://github.com/hu-herrera/HH-sec-/settings/pages), configurar `Deploy from a branch`, rama `main`, carpeta `/ (root)`.
4. Una vez publicada la URL final, añadir URL absoluta en `og:image`, `canonical`, `sitemap.xml` y `url` del JSON-LD antes de dar de alta en Google Search Console.
5. En LinkedIn Company Page, reemplazar el sitio web temporal (`cv-hh.pages.dev`) por la web HH sec+ cuando esté disponible.

## Reglas editoriales

- No publicar información interna de clientes, contraseñas, logs, diagramas privados o proyectos académicos aún no públicos.
- No declarar certificaciones CCNA/CCNP oficiales sin contar con credenciales verificables. Los cursos aprobados son formación, no necesariamente certificaciones.
- No implicar asociaciones comerciales con RH Rental o BlackShark Studios sin autorización. La experiencia vinculada al rubro industrial puede describirse sin sugerir respaldo institucional.
- Ningún cambio SEO garantiza el primer puesto en Google; verificar indexación con herramientas adecuadas.

## Contacto

Correo: [hu.herrera@outlook.com](mailto:hu.herrera@outlook.com)

Perfil personal: [LinkedIn](https://www.linkedin.com/in/hugo-herrera-redes)