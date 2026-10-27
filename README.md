# HH sec+

**Tu red: diseñada para funcionar, asegurada para durar.**

Sitio corporativo de **HH sec+**, empresa de consultoría TI, redes informáticas, ciberseguridad e infraestructura para PyMEs en Chile.

## Sitio web

La página presenta los servicios de la empresa, su enfoque de trabajo y un formulario de contacto para nuevos clientes.

## Archivos

- `index.html`: página principal y SEO.
- `assets/styles.css`: diseño adaptable.
- `assets/favicon.svg` y `assets/social-card.svg`: identidad visual.
- `gracias.html`: confirmación posterior al formulario.
- `robots.txt` y `sitemap.xml`: indexación.
- `tests/check_site.py`: comprobaciones básicas.

## Ejecutar localmente

```bash
python3 -m http.server 8000
python3 tests/check_site.py
```

Abrir `http://localhost:8000`.

## Publicar en GitHub Pages

En [Settings > Pages](https://github.com/hu-herrera/HH-sec-/settings/pages), seleccionar **Deploy from a branch**, rama **main**, carpeta **/(root)**.

URL prevista: https://hu-herrera.github.io/HH-sec-/

## Formulario de contacto

El formulario usa [FormSubmit](https://formsubmit.co/) como receptor para una web estática. Las consultas se envían al correo de administración configurado en el formulario, sin mostrarlo en la interfaz del sitio.

**Activación inicial:** una primera prueba de envío genera un correo de confirmación de FormSubmit. Es necesario confirmar ese mensaje para habilitar las notificaciones. Después, comprobar que llega correctamente una consulta de prueba. El contenido del formulario es procesado por ese proveedor externo.

Si se migra el sitio a otro hosting o dominio, actualizar la ruta de confirmación `_next` y las URLs de SEO.
