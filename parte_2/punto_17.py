#Redireccionamiento y url_for

#¿Cómo se usan estas funciones?
'La función url_for() se utiliza principalmente para realizar enrutamiento dinámico. En lugar de escribir una dirección web fija, le pasas el nombre de la función de Python (la que está debajo del @app.route) y Flask genera la URL correspondiente de forma automática.'

#Uso en archivos Python (Redirecciones)
'Se suele combinar con redirect() para enviar al usuario a otra página después de una acción (como iniciar sesión).'

#ejemplo 
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return "Página de Inicio"

@app.route('/perfil/<username>')
def mostrar_perfil(username):
    return f"Perfil de: {username}"

@app.route('/login_exitoso')
def login():
    # url_for busca la función 'mostrar_perfil' y le pasa el parámetro requerido
    # Esto genera internamente la cadena: '/perfil/juan'
    return redirect(url_for('mostrar_perfil', username='juan'))

if __name__ == '__main__':
    app.run(debug=True)


#Uso en Plantillas HTML (Jinja2)
'Se usa para crear enlaces (<a>), cargar imágenes o enlazar archivos CSS de forma dinámica.'
#ejemplo
'''
<a href="{{ url_for('inicio') }}">Ir al Inicio</a>

<a href="{{ url_for('mostrar_perfil', username='maria') }}">Ver Perfil de Maria</a>'''

#¿Por qué url_for es mejor que escribir URLs manualmente?
'url_for es mejor porque evita enlaces rotos y facilita el mantenimiento: al conectar tus páginas con el nombre de la función de Python en lugar de una ruta de texto fija, puedes cambiar cualquier URL en tu servidor y todo el sitio web se actualizará automáticamente sin tener que modificar tus HTML uno por uno. Además, corrige errores de escritura al instante durante el desarrollo y adapta las rutas de forma automática si cambias tu proyecto de servidor.'

