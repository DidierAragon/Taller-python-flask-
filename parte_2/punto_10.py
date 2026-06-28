# Primera aplicacion Flask — app.py y servidor de desarrollo
"""Este archivo contiene la primera aplicación Flask que configura el objeto app,
define una ruta raíz y ejecuta el servidor de desarrollo con debug=True."""
from flask import Flask  #importaciones 

# 1. Crear el objeto 'app' (instancia de la clase Flask)
app = Flask(__name__)

# 2. Definir una ruta raíz ('/') que responda con un mensaje
@app.route('/')
def home():
    return "¡Hola! Servidor Flask corriendo con éxito."

# 3. Ejecutar el servidor de desarrollo con debug=True
if __name__ == '__main__':
    app.run(debug=True) #muestra el error en pantalla
