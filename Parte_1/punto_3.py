#Ciclos — for y while
"""Los ciclos for y while son herramientas fundamentales de control de flujo. Usa for cuando conozcas de antemano el número exacto de elementos a iterar (como recorrer una lista). Usa while para repetir acciones basadas en una condición lógica que cambiará durante la ejecución."""


#Ciclo for (Iteración sobre colecciones)
"""Util para para recorrer estructuras de datos ( listas, rangos, arreglos). Ejecuta un bloque de código por cada elemento en la colección."""

"""Ejemplo de ciclo for (recorriendo una lista):"""
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(f"Número: {numero}")



#Ciclo while (Repetición con condición)
"""Se ejecuta continuamente mientras una condición específica se evalúe como verdadera (true)."""

"""Ejemplo de ciclo while (repetición basada en condición):"""
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1

#Control de flujo: break y continue
"""Estas palabras clave te permiten modificar el comportamiento natural de cualquier ciclo:"""

"""break: Termina el ciclo por completo de forma inmediata. El programa salta a la siguiente línea de código después del ciclo."""
"""continue: Salta el resto de las instrucciones de la iteración actual y fuerza al ciclo a evaluar la siguiente iteración."""

# Ejemplo de FOR con CONTINUE
numeros = [1, 2, 3, 4, 5]
for n in numeros:
    if n == 3:
        continue  # Salta el número 3 y sigue con el 4
    print(n)  # Imprime: 1, 2, 4, 5

# Ejemplo de WHILE con BREAK
contador = 0
while contador < 3:
    contador += 1
    if contador > 3:
        break  # Detiene el ciclo cuando el contador llega a 3
    print(contador)  # Imprime: 1, 2, 3