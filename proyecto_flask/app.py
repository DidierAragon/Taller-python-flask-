# Jesus Alvarez - Taller de Investigacion
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DATABASE = 'contacto.db'

# crea la tabla si no existe
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mensajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            mensaje TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# muestra todos los mensajes
@app.route('/')
def index():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre, email, mensaje FROM mensajes ORDER BY id DESC')
    mensajes = cursor.fetchall()
    conn.close()
    return render_template('index.html', mensajes=mensajes)

# muestra el formulario y guarda el mensaje
@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO mensajes (nombre, email, mensaje) VALUES (?, ?, ?)',
                       (nombre, email, mensaje))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('contacto.html')

# elimina un mensaje por su id
@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM mensajes WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
