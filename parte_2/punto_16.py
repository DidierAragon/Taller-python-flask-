#Herencia de plantillas — base.html y block
'En Flask, el motor de plantillas Jinja2 utiliza el concepto de herencia de plantillas para evitar la repetición de código. Esto te permite crear una estructura base (que contiene el header, el footer y los enlaces a CSS/JS) y "heredarla" en las demás páginas, cambiando únicamente el contenido central.'

#La Plantilla Base (El cascarón general)
'Primero, creamos un archivo que servirá de molde para todo el sitio web. Aquí definiremos el header y el footer, y dejaremos un espacio reservado (un bloque) para que las otras páginas inyecten su propio contenido.'

'Por convención, a este archivo se le suele llamar base.html.'
#ejemplo en html
'templates/base.html'

'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Mi Sitio Web{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/estilos.css') }}">
</head>
<body>

    <header>
        <nav>
            <a href="/">Inicio</a> | 
            <a href="/contacto">Contacto</a>
        </nav>
    </header>
    <hr>

    <main>
        {% block content %}
        {% endblock %}
    </main>

    <hr>
    <footer>
        <p>&copy; 2026 - Todos los derechos reservados.</p>
    </footer>

</body>
</html>'''

#Explicación de las Etiquetas
'{% block nombre %} y {% endblock %}: Son etiquetas que sirven para delimitar una "región heredable". Le dicen a Jinja2: "Este espacio está reservado para que cualquier página que herede de aquí pueda modificar su interior". Puedes crear tantos bloques como quieras (title, css, js, etc.).'

'{% block content %}: No es una etiqueta especial del sistema; content es simplemente el nombre que los programadores eligen por buena práctica para identificar el bloque del contenido principal de la página. Podrías llamarlo {% block cuerpo %}, pero la comunidad usa content de forma estándar.'

'{% extends "archivo.html" %}: Es la etiqueta que se coloca en la primera línea de las páginas secundarias (páginas hijas). Le indica a Flask que esa página debe copiar toda la estructura del archivo padre indicado.'

#Creando las Páginas Hijas (Reutilizando el código)
'Ahora que tenemos el molde base.html, crear páginas nuevas como el "Inicio" o el "Contacto" es sumamente fácil y limpio, ya que no tienes que volver a escribir las etiquetas <html>, <head>, <header> ni <footer>'

#ejemplo
'templates/inicio.html'

'''{% extends "base.html" %}

{% block title %}Inicio{% endblock %}

{% block content %}
    <h2>Bienvenido a mi sitio web</h2>
    <p>Este es el contenido de la página de inicio.</p>
{% endblock %}
'''
#El archivo en Flask (app.py)
'Para renderizar estas páginas en tu servidor de Flask, las rutas llaman directamente a los archivos hijos. Flask se encargará tras bambalinas de fusionar el hijo con el padre antes de enviárselo al navegador del usuario.'

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    # Renderiza 'inicio.html', el cual jala automáticamente el header y footer de 'base.html'
    return render_template('inicio.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)

