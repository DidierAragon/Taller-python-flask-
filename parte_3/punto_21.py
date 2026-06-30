#SQLite con Python — sqlite3

#importar el módulo y crear la conexión
'Para empezar, importas sqlite3. Al usar sqlite3.connect(), se creará un archivo de base de datos en tu directorio actual si este no existe. Si ya existe, simplemente se conectará a él.'

'También es fundamental crear un cursor. El cursor es el objeto que te permite ejecutar comandos SQL y recorrer los resultados.'

import sqlite3

# Crear la conexión (si el archivo no existe, se creará automáticamente)
conexion = sqlite3.connect("mi_base_de_datos.db")

# Crear el objeto cursor para ejecutar comandos
cursor = conexion.cursor()

#Crear una tabla (CREATE TABLE)

'Usamos el método execute() del cursor para enviar la sentencia SQL. aqui vamos a crear una tabla llamada usuarios.'

# Crear una tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER
)
""")
'Nota: Los cambios de estructura se aplican inmediatamente,' 
'pero es buena práctica tener la conexión bajo control.'

#Insertar datos (INSERT)
'Cuando modificas datos (con INSERT, UPDATE o DELETE), debes usar conexion.commit() después de ejecutar el comando. Si no lo haces, los cambios se perderán al cerrar la sesión (se revertirán).'

# Datos a insertar
nuevo_usuario = ("Carlos", 28)

# Ejecutar la inserción usando marcadores de posición (?) por seguridad
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", nuevo_usuario)

# Guardar los cambios en la base de datos de forma permanente
conexion.commit()
print("Usuario insertado con éxito.")

#Consultar datos (SELECT)
'Para leer datos, ejecutas el SELECT y luego utilizas métodos del cursor como fetchall() (para traer todos los registros) o fetchone() (para traer solo uno).'
# Ejecutar la consulta
cursor.execute("SELECT id, nombre, edad FROM usuarios")

# Recuperar todos los resultados de la consulta
usuarios = cursor.fetchall()

# Recorrer y mostrar los resultados
print("\n--- Lista de Usuarios ---")
for usuario in usuarios:
    # Cada usuario es una tupla: (id, nombre, edad)
    print(f"ID: {usuario[0]} | Nombre: {usuario[1]} | Edad: {usuario[2]}")

#Cerrar la conexión
'Es vital cerrar tanto el cursor como la conexión para liberar los recursos del sistema y evitar que el archivo de la base de datos quede bloqueado.'
# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
print("\nConexión cerrada correctamente.")