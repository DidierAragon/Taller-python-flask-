# Sesiones en Flask — flask.session
'En Flask, el manejo de sesiones permite almacenar información específica de un usuario (como su nombre o si ha iniciado sesión) a través de diferentes peticiones HTTP. Dado que el protocolo HTTP no tiene memoria, las sesiones utilizan cookies cifradas para recordar al usuario.'

#Configurar la SECRET_KEY (Clave Secreta)
'Flask almacena los datos de la sesión dentro de una cookie en el navegador del usuario. Para evitar que el usuario manipule o modifique estos datos a su antojo, Flask los cifra. Para ello, es estrictamente obligatorio configurar una clave secreta (SECRET_KEY).'
'Si no configuras una SECRET_KEY e intentas usar sesiones, Flask lanzará un error de tipo RuntimeError.'

import os
from flask import Flask, session

app = Flask(__name__)

# Configuración de la clave secreta
app.config['SECRET_KEY'] = 'mayron123'

# Nota en producción: Se recomienda usar variables de entorno por seguridad:
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@app.route('/')
def inicio():
    # Almacenar datos en la sesión
    session['username'] = 'mayron'
    session['login'] = True
    return 'Sesión iniciada correctamente!'

if __name__ == '__main__':
    app.run(debug=True)

#Guardar y Leer datos con session
'Para gestionar la sesión, debes importar el objeto session de Flask. Este objeto funciona exactamente igual que un diccionario de Python, por lo que puedes agregar, leer y modificar elementos usando llaves []'

from flask import Flask, session, redirect, url_for, render_template, request #importaciones

app = Flask(__name__)#
app.config['SECRET_KEY'] = 'clave_secreta_de_prueba' #esta es la clave secret

@app.route('/login', methods=['POST']) #la ruta del login 
def login():
    
    usuario_formulario = request.form.get('username') #validamos los datos de un formulario
    
    # GUARDAR DATOS EN LA SESIÓN
    session['usuario'] = usuario_formulario 
    session['rol'] = 'administrador' 
    
    return redirect(url_for('perfil')) 

@app.route('/perfil')
def perfil():
    # LEER DATOS DE LA SESIÓN
    # Usamos .get() para evitar errores si la sesión está vacía
    if 'usuario' in session:
        nombre = session.get('usuario')
        rol = session.get('rol')
        return f"Bienvenido a tu perfil, {nombre}. Tu rol es: {rol}."
    
    return "No has iniciado sesión. Por favor ve a /login."

#Cómo Cerrar Sesión (session.pop o session.clear)
'Cerrar sesión consiste simplemente en eliminar los datos almacenados en la cookie del usuario. Tienes dos métodos principales para hacerlo en Python:'

'session.pop(llave, None): Elimina una variable específica de la sesión.'

'session.clear(): Borra absolutamente todos los datos guardados en la sesión, dejándola completamente vacía (es la opción más recomendada para un logout).'

@app.route('/logout')
def logout():
    # Elimina todos los datos de la sesión del usuario
    session.clear()
    
    # Alternativa si solo quieres borrar el usuario:
    # session.pop('usuario', None)
    
    return redirect(url_for('inicio'))


