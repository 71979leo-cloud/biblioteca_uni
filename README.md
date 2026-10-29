# Biblioteca Universitaria del Valle

Aplicación web multipágina desarrollada con Flask, plantillas Jinja2 y Bootstrap
para el ejercicio de biblioteca universitaria. Los datos de dirección y contacto
son ficticios.

## Requisitos

- Python 3.10 o posterior
- pip

## Instalación y ejecución

Desde la carpeta del proyecto, ejecuta:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python server.py
```

Abre <http://127.0.0.1:5000/> en el navegador. Bootstrap se carga desde su CDN,
por lo que se requiere conexión a internet para aplicar sus estilos.

## Páginas

- **Inicio (`/`)**: presenta la biblioteca, su propósito y el horario general.
- **Catálogo (`/catalogo`)**: muestra libros, revistas, tesis y recursos digitales.
- **Servicios (`/servicios`)**: describe los servicios disponibles.
- **Contacto (`/contacto`)**: incluye dirección, correo y horario ficticios.

## Elementos implementados

- `server.py` crea la aplicación Flask y define las cuatro rutas. Cada ruta usa
  `render_template()` y envía las variables `titulo` y `mensaje`, además de los
  datos específicos que necesita su página.
- `templates/layout.html` contiene la estructura HTML, la referencia a Bootstrap,
  el título del documento, la navegación horizontal y el bloque `content`.
- `templates/index.html`, `templates/catalogo.html`, `templates/servicios.html`
  y `templates/contacto.html` heredan de `layout.html` con `extends` y definen
  su contenido en el bloque `content`.
- Los enlaces del menú se generan con `url_for()` y el contenido de cada página
  se organiza dentro de `container-fluid`.
- `requirements.txt` declara Flask como dependencia del proyecto.

## Repositorio de GitHub

URL: **Pendiente de publicar.** Después de crear el repositorio en GitHub,
reemplaza esta línea con su URL.
