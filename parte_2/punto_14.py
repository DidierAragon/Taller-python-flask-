# Variables de URL y parametros de consulta
'En Flask, existen dos formas principales de capturar datos directamente desde la URL: las Variables de Ruta (o parámetros de ruta) y los Parámetros de Consulta (Query Parameters).'

#. Variables de Ruta y Conversores (int, float, string)
'En Flask, puedes definir rutas dinámicas utilizando < entre llaves {} en la URL. Los conversores (int, float, string) especifican el tipo de dato que esperas recibir.'

'''app=None

@app.route('/usuario/<int:id_usuario>')
def mostrar_usuario(id_usuario):
    return f"Usuario con ID: {id_usuario}"'''

'''
string: (Por defecto) Acepta cualquier texto que no contenga una barra diagonal (/).
int: Acepta únicamente números enteros positivos.
float: Acepta números decimales positivos.'''

from flask import Flask

app = Flask(__name__)

# 1. Conversor por defecto (string)
@app.route('/usuario/<nombre>')
def mostrar_usuario(nombre):
    # 'nombre' es de tipo str
    return f"Perfil del usuario: {nombre}"

# 2. Conversor int (Fuerza a que sea entero)
@app.route('/producto/<int:producto_id>')
def mostrar_producto(producto_id):
    # 'producto_id' es un número entero de Python
    return f"Buscando el producto con ID numérico: {producto_id}"

# 3. Conversor float (Fuerza a que sea decimal)
@app.route('/cambio/<float:precio>')
def calcular_cambio(precio):
    # 'precio' es de tipo float
    iva = precio * 0.19
    return f"El IVA para el precio {precio} es: {iva:.2f}"

if __name__ == '__main__':
    app.run(debug=True)


#Parámetros de Consulta con request.args
'Los parámetros de consulta no cambian la estructura de la ruta; se añaden al final de la URL después de un signo de interrogación (?) en formato de llave y valor (llave=valor). Si hay varios parámetros, se separan con un amperio (&).'

'Para capturar estos valores se utiliza request.args. A diferencia de las variables de ruta, todos los datos obtenidos a través de request.args son strings (texto), por lo que debes convertirlos manualmente si necesitas operar con ellos.'

from flask import Flask, request

app = Flask(__name__)

# URL de ejemplo: http://127.0.0.1:5000/buscar?termino=flask&pag=2
@app.route('/buscar')
def buscar():
    # .get() evita que la app falle si el parámetro no viene en la URL
    # Sintaxis: .get('nombre_parametro', valor_por_defecto)
    termino_busqueda = request.args.get('termino', '')
    
    # Como llega como string, lo convertimos a entero manualmente
    pagina = request.args.get('pag', default=1, type=int)
    
    return f"Buscando: '{termino_busqueda}' en la página número: {pagina}"