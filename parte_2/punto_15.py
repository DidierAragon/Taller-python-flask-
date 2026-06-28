#Archivos estaticos — CSS, JS e imagenes
'En Flask, el manejo de archivos estáticos (como hojas de estilo CSS, imágenes o archivos JavaScript) sigue una convención de estructura muy clara. Flask busca de forma automática estos recursos dentro de una carpeta llamada exactamente' 
'static'

'Para mantener el proyecto ordenado y escalable, nunca debes colocar los archivos sueltos dentro de static. La mejor práctica es crear subcarpetas según el tipo de recurso.'

'La estructura recomendada de tu proyecto debería verse así:'

'''mi_proyecto_flask/
│
├── app.py                  # Archivo principal de Python
├── templates/              # Carpeta para tus archivos HTML
│   └── index.html
└── static/                 # Carpeta raíz de archivos estáticos
    ├── css/                # Subcarpeta para hojas de estilo
    │   └── estilos.css
    ├── js/                 # Subcarpeta para scripts de JavaScript
    │   └── script.js
    └── img/                # Subcarpeta para imágenes y logotipos
        └── logotipo.png'''

#Referenciar archivos CSS con url_for()
'Para enlazar un archivo CSS en tus plantillas HTML (dentro de la carpeta templates), debes utilizar el motor de plantillas Jinja2 junto con la función url_for() de Flask.'
#por qué usar url_for() en lugar de una ruta común como /static/css/estilos.css
'Porque url_for genera rutas absolutas dinámicamente. Si el día de mañana decides mover tu aplicación a otra subruta del servidor o cambias el nombre de la carpeta estática en la configuración, Flask corregirá todos los enlaces automáticamente sin que tengas que editar tus HTML uno por uno.'

'La sintaxis dentro del HTML requiere llaves dobles {{ ... }}:'

'templates/index.html'

'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi Página en Flask</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/estilos.css') }}">
</head>
<body>
    <h1>Bienvenido a mi aplicación</h1>
</body>
</html>'''

#explicacion
'''El primer argumento 'static' le indica a Flask que busque en la carpeta raíz de archivos estáticos.

El parámetro filename='css/estilos.css' le dice la ruta exacta del archivo partiendo desde el interior de la carpeta static.'''

#Cargar imágenes en los Templates
'El proceso para mostrar imágenes en tus páginas web es exactamente el mismo que con los archivos CSS. Utilizarás la etiqueta HTML <img> y asignarás el resultado de url_for() al atributo src.'

#ejemplo
'''<img src="{{ url_for('static', filename='img/logotipo.png') }}" alt="Logotipo de mi sitio web" width="200">'''