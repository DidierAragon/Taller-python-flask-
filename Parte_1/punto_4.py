#Funciones — def, parámetros, return
""" las funciones son bloques de código reutilizables. Se definen con la palabra clave def, seguida del nombre de la función y paréntesis. Los valores se envían a través de parámetros, pueden tener valores por defecto y el resultado se devuelve usando return."""

# Definición básica y Retorno
"""Una función se define usando la palabra clave def, seguida del nombre de la función y los parámetros entre paréntesis. El bloque de código que constituye la función debe estar indentado (4 espacios o 1 tabulación). El resultado se devuelve usando la palabra clave return."""

def saludar():#Función sin parámetros que retorna un mensaje de saludo.
    return "¡Hola!"
# Llamada a la función
mensaje = saludar()
print(mensaje)

#Parámetros con valores por defecto
"""Puedes asignar un valor predeterminado a un parámetro usando el signo igual (=). Si no se proporciona ese argumento al llamar a la función, se utilizará el valor por defecto."""

def saludar_con_nombre(nombre="Invitado"):
    return f"¡Hola, {nombre}!"

# Llamada sin proporcionar el parámetro (usa el valor por defecto)
print(saludar_con_nombre())

# Llamada con el parámetro (sobrescribe el valor por defecto)
print(saludar_con_nombre("Mayron"))

# Argumentos por nombre
"""Puedes especificar los argumentos por nombre para mayor claridad y para pasar valores en cualquier orden."""

print(saludar_con_nombre(nombre="Katerine"))
