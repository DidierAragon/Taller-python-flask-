#Manejo de Archivos — open, read, write
"""la función open() se utiliza para abrir archivos. Para garantizar que los archivos se cierren automáticamente (liberando memoria y recursos del sistema), la mejor práctica es utilizar el administrador de contexto with."""

#Modos de apertura

""" (r) (Lectura): Es el modo predeterminado. Abre el archivo para leer su contenido. Si el archivo no existe, arroja un error."""
""" (w) (Escritura): Abre el archivo para escribir. Si el archivo existe, lo sobrescribe (borrando su contenido). Si no existe, lo crea."""
""" (a) (Adición): Abre el archivo para escribir al final del archivo sin sobrescribir el contenido existente. Si no existe, lo crea."""

#Uso de with
"""La declaración with maneja el flujo de entrada/salida de forma segura. Al salir del bloque with, Python cierra el archivo automáticamente, incluso si ocurren errores durante la ejecución."""

with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, mundo!")

#Leer línea por línea
"""Para leer archivos grandes sin saturar la memoria RAM, la forma más eficiente es iterar directamente sobre el objeto del archivo."""

with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip()) # strip() elimina el salto de línea oculto al final
#Leer todo de una vez
"""Si el archivo no es demasiado grande, puedes leer todo su contenido de una sola vez usando read()."""
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
