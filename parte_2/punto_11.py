#Rutas y Decoradores — @app.route

#Cómo funciona el decorador @app.route
'En Python, un decorador (la línea que empieza con @) es una función que envuelve a otra función para modificar su comportamiento sin cambiar su código fuente.'
#ejemplo 
app=None
@app.route('/contacto') #esto es un decorador que asigna la ruta '/contacto' a la función 'contact'
def contact():
    return "Página de contacto"

if __name__ == '__main__':
    app.run(debug=True)

#Cómo definir múltiples rutas
'En Flask, puedes mapear tantas rutas como quieras en el mismo archivo simplemente añadiendo más funciones decoradas.'

'Incluso puedes asignar múltiples rutas a una sola función:'

@app.route('/')
@app.route('/inicio')
@app.route('/home')
def index():
    return "¡Bienvenido a la página principal!"

#Rutas dinámicas
'Flask permite capturar partes de la URL usando pico-paréntesis <>.'
'El valor capturado en la URL se pasa automáticamente como un argumento a la función:'

# Ruta dinámica simple (por defecto acepta texto/strings)
@app.route('/user/<username>')
def mirarperfil(usuario):
    return f"Perfil del usuario: {usuario}"

# Ruta dinámica con convertidor de tipo (int, float, path)
@app.route('/post/<int:post_id>')
def mirar_post(post_id):
    # 'post_id' está garantizado que será un número entero
    return f"Estás leyendo el artículo número: {post_id}"

#Gestión de métodos HTTP (GET y POST)
'todas las rutas en Flask responden únicamente a peticiones de tipo GET (solicitudes para leer o descargar información). Si quieres que una ruta reciba datos de un formulario o cree un registro, debes permitir el método POST.'

'Para lograrlo, se usa el argumento methods dentro del decorador:'
from flask import Flask, request  # Importamos 'request' para leer los datos del formulario

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # El usuario envió el formulario
        usuario = request.form.get('usuario')
        contraseña = request.form.get('contraseña')
        return f"Procesando inicio de sesión para {usuario}..."
    else:
        # El usuario solo entró a la página a ver el formulario (GET)
        return '''
            <form method="post">
                <input type="text" name="username" placeholder="Usuario"><br>
                <input type="password" name="password" placeholder="Contraseña"><br>
                <input type="submit" value="Iniciar Sesión">
            </form>
        '''

#Cómo funciona el flujo de arriba

'Paso 1 (GET): Entras a http://127.0.0.1:5000/login. Como es una petición de lectura, se ejecuta el bloque else y el navegador dibuja el formulario HTML.'

'Paso 2 (POST): Escribes tus datos y haces clic en "Iniciar Sesión". El formulario envía los datos de vuelta a la misma URL /login, pero ahora con el método POST. El código detecta que request.method == POST y procesa los datos de forma segura.'