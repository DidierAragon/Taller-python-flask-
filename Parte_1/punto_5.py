#Listas, Tuplas y Diccionarios

"""Las listas son mutables (modificables), las tuplas son inmutables (fijas), y los diccionarios organizan los datos en pares de clave y valor."""

#listas
"""Colecciones mutables y ordenadas que permiten duplicados."""

"""Crear: Se utilizan corchetes []."""
mi_lista = ["manzana", "pera", "naranja"]

"""Acceder: Mediante índices (inician en 0). Soporta índices negativos."""
elemento1 = mi_lista[0] # "manzana"
elemento2 = mi_lista[-1] # "naranja"

"""Modificar: Son mutables, por lo que puedes reasignar valores, agregar (append) o insertar (insert)."""
mi_lista[1] = "uva" # Modifica el índice 1
mi_lista.append("sandía") # Agrega al final

"""Recorrer: Se usa un bucle for."""
for fruta in mi_lista:
    print(fruta)


#tuplas
"""Colecciones inmutables y ordenadas que permiten duplicados."""

"""Crear: Se utilizan paréntesis ()."""
mi_tupla = ("rojo", "verde", "azul")

"""Acceder: Al igual que las listas, mediante índices."""
elemento = mi_tupla[1] # "verde"

"""Modificar: No se pueden modificar una vez creadas (lanzan un TypeError si lo intentas). Para alterarlas, debes crear una nueva tupla o convertirla temporalmente a lista."""

"""Recorrer: Se utiliza un bucle for."""
for color in mi_tupla:
    print(color)


#diccionaro
"""Colecciones mutables formadas por pares de clave:valor, donde las claves son únicas."""

"""Crear: Se utilizan llaves {}."""
dicc = {"nombre": "Mayron", "edad": 28, "ciudad": "Palmira"}

"""Acceder: Se realiza a través de la clave específica"""
edad_persona = dicc["edad"] # 28

"""Modificar: Se puede cambiar el valor asociado a una clave existente o agregar una nueva clave-valor."""
dicc["edad"] = 29 # Modifica el valor existente
dicc["telefono"] = "1234567890" # Agrega una nueva clave

"""Recorrer: Se itera sobre las claves del diccionario."""
for clave in dicc:
    print(clave, dicc[clave])
