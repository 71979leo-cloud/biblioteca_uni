from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        titulo="Inicio",
        mensaje="Bienvenido a la Biblioteca Universitaria del Valle.",
    )


@app.route("/catalogo")
def catalogo():
    categorias = [
        {
            "nombre": "Libros",
            "descripcion": "Obras de consulta, estudio y lectura de distintas disciplinas.",
        },
        {
            "nombre": "Revistas",
            "descripcion": "Publicaciones periódicas académicas y de divulgación.",
        },
        {
            "nombre": "Tesis",
            "descripcion": "Trabajos de investigación elaborados por estudiantes universitarios.",
        },
        {
            "nombre": "Recursos digitales",
            "descripcion": "Libros electrónicos, revistas en línea y bases de datos académicas.",
        },
    ]
    return render_template(
        "catalogo.html",
        titulo="Catálogo",
        mensaje="Explora los materiales disponibles para apoyar tus estudios e investigaciones.",
        categorias=categorias,
    )


@app.route("/servicios")
def servicios():
    servicios_biblioteca = [
        {
            "nombre": "Préstamo de libros",
            "descripcion": "Consulta y préstamo de libros para llevar, de acuerdo con las políticas de la biblioteca.",
        },
        {
            "nombre": "Consulta en sala",
            "descripcion": "Espacios de lectura y estudio para consultar materiales dentro de la biblioteca.",
        },
        {
            "nombre": "Acceso a recursos digitales",
            "descripcion": "Consulta de recursos electrónicos disponibles para la comunidad universitaria.",
        },
        {
            "nombre": "Orientación bibliográfica",
            "descripcion": "Apoyo para localizar fuentes y organizar búsquedas de información académica.",
        },
    ]
    return render_template(
        "servicios.html",
        titulo="Servicios",
        mensaje="Conoce los servicios disponibles para acompañar tu aprendizaje.",
        servicios=servicios_biblioteca,
    )


@app.route("/contacto")
def contacto():
    datos_contacto = {
        "direccion": "Av. Universidad 1200, Col. Centro, Ciudad Universitaria",
        "correo": "biblioteca@universidad.edu.mx",
        "horario": "Lunes a viernes, de 8:00 a 20:00; sábados, de 9:00 a 14:00.",
    }
    return render_template(
        "contacto.html",
        titulo="Contacto",
        mensaje="Estamos disponibles para resolver tus dudas y orientarte.",
        contacto=datos_contacto,
    )


if __name__ == "__main__":
    app.run(debug=True)
