#Estructuras de Control — if, elif, else
"""En Python, if, elif y else son las estructuras fundamentales de control de flujo. Definen qué bloques de código ejecutar basándose en el cumplimiento de condiciones específicas. """

#Sintaxis Básica
"""La estructura comienza con un if, puede tener múltiples elif (abreviatura de else if) y termina con un else opcional. La línea del condicional siempre debe terminar con dos puntos (:)"""

# ejemplo
edad = 20

if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres niño")

#Indentación Obligatoria
"""En lugar de usar llaves {} como otros lenguajes, Python utiliza obligatoriamente la indentación (espacios en blanco al inicio de la línea) para definir qué instrucciones pertenecen a un bloque de código."""

"""Por convención, se utilizan 4 espacios por nivel."""
"""Todas las líneas del mismo bloque deben tener exactamente el mismo nivel de indentación"""
"""Un error de sangría (IndentationError) detendrá el programa."""

# Comparación de Valores
"""Para evaluar si dos valores cumplen una relación, Python utiliza los operadores de comparación. El resultado de estas comparaciones siempre es un valor booleano (True o False)"""

""" == : Igual a ( no podemos confundirlo con =, que sirve para asignar valores)."""
""" != : Distinto de."""
""" < : Menor que."""
""" <= : Menor o igual que."""
""" >: Mayor que."""
""" >= : Mayor o igual que."""


"""Además, puedes combinar múltiples comparaciones utilizando operadores lógicos:""" 

"""and (devuelve True si ambas condiciones se cumplen)."""
"""or (devuelve True si al menos una condición se cumple"""