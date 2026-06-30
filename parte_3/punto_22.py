#Integracion Flask + SQLite — CRUD basico

#El Ciclo de Vida (Abrir y Cerrar)
'Para no saturar la memoria, la base de datos se abre cuando llega la solicitud del usuario y se cierra automáticamente al terminar, usando el objeto g (almacenamiento temporal de Flask) y el decorador teardown' 

from flask import Flask, g, request
import sqlite3

app = Flask(__name__)

def get_db():
    # Si no hay conexión en esta solicitud, la crea
    if 'db' not in g:
        g.db = sqlite3.connect('datos.db')
        g.db.row_factory = sqlite3.Row # Permite buscar por nombre de columna
    return g.db

@app.teardown_appcontext
def close_db(exception):
    # Al terminar la solicitud, se cierra la BD automáticamente
    db = g.pop('db', None)
    if db is not None:
        db.close()

#Operaciones CRUD


#Crear (CREATE / INSERT)
'Recibe los datos de un formulario y los guarda. Recuerda usar commit() para aplicar los cambios.'
@app.route('/crear', methods=['POST'])
def crear():
    nombre = request.form['nombre']
    db = get_db()
    db.execute("INSERT INTO usuarios (nombre) VALUES (?)", (nombre,))
    db.commit() # Guarda el cambio
    return "Usuario guardado"


#Leer (READ / SELECT)
'Busca los registros en la base de datos para mostrarlos.'
@app.route('/usuarios')
def leer():
    db = get_db()
    usuarios = db.execute("SELECT * FROM usuarios").fetchall()
    # En el HTML los usas así: usuario['nombre']
    return f"Total de usuarios: {len(usuarios)}"

#Actualizar (UPDATE)
'Modifica un registro existente usando su identificador único (id).'
@app.route('/editar/<int:id>', methods=['POST'])
def actualizar(id):
    nuevo_nombre = request.form['nombre']
    db = get_db()
    db.execute("UPDATE usuarios SET nombre = ? WHERE id = ?", (nuevo_nombre, id))
    db.commit()
    return "Usuario actualizado"

#Eliminar (DELETE)
'Borra un registro de la base de datos de forma permanente.'
@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    db = get_db()
    db.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    db.commit()
    return "Usuario eliminado"