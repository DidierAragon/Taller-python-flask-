#Manejo de Excepciones — try, except, finally
"""Los bloques try y except se utilizan para gestionar errores durante la ejecución de un programa y evitar cierres inesperados. El código a evaluar se coloca en try y, si ocurre un fallo, el control pasa a except, donde se define cómo resolver o registrar el problema.""" 

# Capturar Tipos Específicos de Excepción
"""Es una buena práctica capturar errores específicos en lugar de usar un except genérico, ya que te permite manejar cada tipo de fallo de forma adecuada y evitar ocultar errores inesperados."""
try:
    numero1 = int(input("Introduce un número: "))
    numero2 = int(input("Introduce otro número: "))
    resultado = numero1 / numero2
    print(f"El resultado es {resultado}")

except ValueError as e:
    print(f"Error: Debes introducir números enteros válidos. Detalles: {e}")

except ZeroDivisionError as e:
    print(f"Error: No se puede dividir un número entre cero. Detalles: {e}")

#El bloque finally
"""El bloque finally es opcional pero muy útil. Se ejecuta siempre al final del proceso, sin importar si el código dentro del bloque try se ejecutó correctamente o si se lanzó una excepción."""

"""Se utiliza frecuentemente para liberar recursos del sistema, como cerrar conexiones a bases de datos, detener flujos de red o cerrar archivos de manera segura"""

archivo = None # Inicializamos la variable

try:
    archivo = open("datos.txt", "r") # Abrimos el archivo para leer
    contenido = archivo.read() # Leemos todo el contenido del archivo
    print(contenido) # Imprimimos el contenido del archivo
except FileNotFoundError: # Error cuando el archivo no existe
    print("Error: El archivo no existe.") 
finally:
    if archivo is not None: # Verificamos que el archivo se abrió correctamente
        archivo.close() # Cerramos el archivo
        print("El archivo ha sido cerrado de forma segura.")
