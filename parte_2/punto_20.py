# API REST con Flask — respuestas JSON

#¿Cómo usar jsonify() y definir endpoints JSON?

'jsonify()'
'es una función nativa de Flask que toma diccionarios, listas o variables de Python y los convierte en una respuesta formateada en JSON. Además, añade automáticamente el encabezado HTTP Content-Type: application/json, lo que le avisa al cliente que está recibiendo datos puros y no texto o HTML.'
#ejemplo

from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos simulada (lista de diccionarios)
productos = [
    {"id": 1, "nombre": "Teclado Mecánico", "precio": 85.50},
    {"id": 2, "nombre": "Ratón Ergonómico", "precio": 45.00}
]

# Endpoint tipo GET para obtener todos los productos
@app.route('/api/productos', methods=['GET'])
def obtener_productos():
    # jsonify convierte la lista de Python directamente a formato JSON
    return jsonify({"productos": productos, "status": "exitoso"}), 200


# Endpoint tipo POST para recibir y registrar un nuevo producto
@app.route('/api/productos', methods=['POST'])
def crear_producto():
    # request.get_json() captura el JSON enviado por el cliente
    datos_recibidos = request.get_json()
    
    nuevo_producto = {
        "id": len(productos) + 1,
        "nombre": datos_recibidos.get("nombre"),
        "precio": datos_recibidos.get("precio")
    }
    
    productos.append(nuevo_producto)
    
    # Devolvemos el producto creado con un código de estado 201 (Creado)
    return jsonify({"mensaje": "Producto creado", "producto": nuevo_producto}), 201

if __name__ == '__main__':
    app.run(debug=True)

#Cómo probar los endpoints
'Para probar los endpoints de tu servidor Flask existen dos opciones principales.' 
'El navegador web permite verificar rutas de forma rápida, pero tiene la limitación de que solo puede realizar peticiones tipo GET al ingresar la URL.' 
'Por otro lado, Postman es la herramienta estándar para pruebas completas de APIs, ya que permite simular cualquier método HTTP (GET, POST, PUT, DELETE). Para probar una petición GET en Postman, basta con abrir una pestaña, seleccionar dicho método, introducir la URL del servidor y hacer clic en Send para recibir la respuesta en formato JSON.'

'''Pasos para probar el endpoint POST (Crear producto):

    Crea una nueva pestaña en Postman.

    Cambia el método a POST.

    Introduce la URL: http://127.0.0.1:5000/api/productos.

    Ve a la pestaña Body (debajo de la URL), selecciona la opción raw y, en el menú desplegable de la derecha, cambia "Text" por JSON.

    En el cuadro de texto, escribe el JSON que quieres enviar:
    
    {
        "nombre": "Monitor 24 pulgadas",
        "precio": 199.99
    }
    
    Haz clic en Send para enviar la solicitud y ver la respuesta en formato JSON.
'''