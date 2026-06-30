# Aplicacion Flask - Formulario de Contacto

Taller de Investigacion

Aplicacion web de formulario de contacto hecha con Flask y SQLite.

## Requisitos

- Python 3.8 o superior
- pip

## Instalacion

1. crear entorno virtual
   python -m venv venv

2. activar
   source venv/bin/activate  (Linux/Mac)
   venv\Scripts\activate     (Windows)

3. instalar flask
   pip install -r requirements.txt

4. ejecutar
   python app.py

5. abrir http://127.0.0.1:5000

## Rutas

- GET  /                -> lista de mensajes
- GET  /contacto        -> formulario
- POST /contacto        -> guarda mensaje
- GET  /eliminar/<id>   -> borra mensaje

## Base de datos

SQLite, se crea sola al iniciar. Tabla mensajes con: id, nombre, email, mensaje.
