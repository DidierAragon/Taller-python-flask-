#Manejo de errores — 404 y 500
'El decorador @app.errorhandler se usa en Flask para reemplazar las pantallas de error genéricas del servidor por páginas web personalizadas con la estética de tu sitio. A diferencia de una ruta común, la función que maneja el error debe recibir obligatoriamente un argumento (que contiene los detalles del fallo) y retornar tanto la plantilla HTML diseñada por ti como el código numérico del error HTTP (como 404 o 500) para no afectar el funcionamiento del navegador ni el SEO.'

#Cómo crear y registrar errores 404 y 500

'Los dos errores más comunes que debes personalizar son:'

'404 Not Found: El recurso o la URL solicitada no existe.'

'500 Internal Server Error: El código de Python falló (un error de lógica, base de datos caída, etc.).'

#ejemplo
from flask import Flask, render_template

app = Flask(__name__)

#RUTAS DE EJEMPLO
@app.route('/')
def inicio():
    return "Página de Inicio funcionando correctamente."

@app.route('/provocar-error')
def provocar_error():
    # Esta ruta causará un error 500 intencional al dividir por cero
    resultado = 1 / 0
    return f"El resultado es {resultado}"


#REGISTRO DE MANEJADORES DE ERROR

# 1. Manejador para el Error 404
@app.errorhandler(404)
def pagina_no_encontrada(e):
    # 'e' guarda la descripción del error
    # Es vital pasar el número 404 al final para que el navegador sepa el estado real
    return render_template('errores/404.html'), 404

# 2. Manejador para el Error 500
@app.errorhandler(500)
def error_interno_servidor(e):
    # Nota: En modo debug=True, Flask mostrará su propia pantalla interactiva de error
    # Este manejador se activará principalmente cuando la app esté en producción (debug=False)
    return render_template('errores/500.html'), 500


if __name__ == '__main__':
    # Pon debug=False para probar el error 500 personalizado
    app.run(debug=False)

'Para mantener el orden de tu proyecto, se recomienda guardar estas pantallas dentro de una subcarpeta llamada errores dentro de templates. Lo ideal es que estas páginas hereden de tu plantilla base.html para que sigan mostrando el mismo menú, cabecera y pie de página de todo tu sitio web.'

#ejemplo templates/errores/404.html
'''{% extends "base.html" %}

{% block title %}Página No Encontrada - 404{% endblock %}

{% block content %}
<div style="text-align: center; padding: 50px;">
    <h1>Elemento no encontrado (Error 404)</h1>
    <p>Lo sentimos, la página que estás buscando no existe o ha sido movida.</p>
    <a href="{{ url_for('inicio') }}">Volver al Inicio</a>
</div>
{% endblock %}'''

