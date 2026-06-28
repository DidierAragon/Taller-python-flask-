#Programacion Orientada a Objetos — Clases y Objetos
"""Para definir una clase en Python, se utiliza la palabra reservada class, seguida del nombre de la clase. El método __init__ es el constructor que se ejecuta automáticamente al crear un objeto. Los atributos de instancia almacenan datos únicos por objeto, y los métodos son las funciones que definen su comportamiento."""

#Definir la clase y el constructor __init__
"""El método __init__ inicializa el estado inicial del objeto. Su primer parámetro siempre es self, que representa la instancia misma que se está creando."""

class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre  # Atributo de instancia
        self.raza = raza      # Atributo de instancia

#Definir métodos
"""Los métodos son funciones creadas dentro de la clase. También deben incluir self como primer parámetro para poder acceder a los datos de esa instancia en particular."""

def ladrar(self):
        return f"{self.nombre} dice: ¡Guau!"
def presentarse(self):
        return f"Hola, soy {self.nombre} y soy un {self.raza}."

#Crear una instancia (Objeto) y usar la clase
"""Para utilizar la clase, se llama a su nombre pasándole los argumentos requeridos por __init__ (sin contar self)."""

mi_perro = Perro("Max", "Golden Retriever")
print(mi_perro.ladrar())
print(mi_perro.presentarse())



