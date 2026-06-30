Taller de Investigacion

Proyecto educativo dividido en 4 partes que cubre Python, Flask, bases de datos, Git y GitHub.

Parte 1 - Python

Fundamentos del lenguaje: variables, estructuras de control, loops, funciones, estructuras de datos, manejo de archivos, excepciones y programacion orientada a objetos.

Parte 2 - Flask

Microframework web: rutas, decoradores, templates Jinja2, formularios, parametros de URL, archivos estaticos, herencia de templates, redirects, manejo de errores, sesiones y APIs REST.

Parte 3 - Temas avanzados

SQLite con Python, integracion Flask + SQLite, entornos virtuales, Git, GitHub y estructura profesional de proyectos Flask.

Parte 4 - Proyecto final (proyecto_flask)

Aplicacion web de formulario de contacto con Flask y SQLite. Permite enviar mensajes, verlos en una lista y eliminarlos.

Requisitos: Python 3.8+, pip

Instalacion:

1. Crear entorno virtual: python -m venv venv
2. Activarlo: source venv/bin/activate (Linux/Mac) o venv\Scripts\activate (Windows)
3. Instalar dependencias: pip install -r requirements.txt
4. Ejecutar: python app.py
5. Abrir http://127.0.0.1:5000

Rutas de la aplicacion:

- GET  /               -> lista de mensajes
- GET  /contacto       -> formulario de contacto
- POST /contacto       -> guarda el mensaje
- GET  /eliminar/<id>  -> elimina un mensaje

Base de datos: SQLite. La tabla mensajes tiene id, nombre, email y mensaje.
