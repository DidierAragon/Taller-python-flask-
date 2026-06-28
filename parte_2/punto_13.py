#Formularios HTML y metodo POST

#El Formulario HTML (method="POST")
'Para enviar datos de forma segura al servidor (como un inicio de sesión o un registro), utilizamos el método POST. Es crucial que cada elemento de entrada (<input>) tenga un atributo name, ya que Flask utilizará ese nombre para identificar el dato.'

'templates/formulario.html:'

'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Formulario de Registro</title>
</head>
<body>
    <h2>Formulario de Registro</h2>
    <form action="/procesar" method="POST">
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" name="usuario" required>
        <br><br>
        <label for="correo">Correo:</label>
        <input type="email" id="correo" name="email" required>
        <br><br>
        <button type="submit">Enviar</button>
    </form>
</body>
</html>'''

#Recibir los datos en Flask (request.form)
'para capturar los datos enviados mediante POST, debes importar el objeto request. Los datos del formulario se almacenan en un diccionario llamado request.form.'

'app.py'

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def mostrar_formulario():
    # Renderiza la página que contiene el formulario HTML
    return render_template('formulario.html')

# Es obligatorio especificar que esta ruta acepta el método POST
@app.route('/procesar', methods=['POST'])
def procesar_formulario():
    # Se obtienen los datos usando el atributo 'name' del HTML
    nombre_usuario = request.form.get('usuario')
    correo_usuario = request.form.get('email')
    
    return f"¡Gracias {nombre_usuario}! Hemos recibido tu correo: {correo_usuario}."

if __name__ == '__main__':
    app.run(debug=True)

#Diferencia entre GET y POST
'''
GET sirve para pedir información; POST sirve para enviar información.
GET muestra los datos en la URL (ej: web.com?nombre=juan); POST los esconde dentro del cuerpo del mensaje.
GET es inseguro (cualquiera ve los datos en el historial); POST es más seguro (ideal para contraseñas).
GET tiene un límite de texto muy corto; POST no tiene límite (sirve para subir fotos o textos largos).
GET se puede guardar en Favoritos/Marcadores; POST no se puede guardar.

En resumen: Usa GET para buscar o navegar, y POST para iniciar sesión o registrar datos.'''

