# Plantillas HTML con Jinja2
'Flask está configurado para buscar todos tus archivos HTML en una carpeta específica llamada estrictamente templates (en minúsculas y plural). Esta carpeta debe estar ubicada en la raíz de tu proyecto, al mismo nivel que tu archivo app.py'

'la estructura de archivos debe verse exactamente así:' 
'''
mi_proyecto_flask/
├── .venv/                  # Entorno virtual
├── app.py                  # Código principal de Flask
└── templates/              # ¡Carpeta obligatoria para los HTML!
    ├── inicio.html
    └── usuarios.html
'''

#Cómo usar render_template()
'En lugar de escribir código HTML feo y largo dentro de las funciones de Python, usamos la función render_template(). Esta función toma un archivo de la carpeta templates, lo procesa y se lo envía al navegador.'

'Además, permite pasar variables desde Python hacia el HTML.'

from flask import Flask, render_template  # Importamos la función

app = Flask(__name__)

@app.route('/')
def inicio():
    usuario = "Jesús"
    # Pasamos la variable 'nombre_usuario' al HTML con el nombre 'usuario'
    return render_template('inicio.html', usuario=usuario)

if __name__ == '__main__':
    app.run(debug=True)

#Sintaxis de Jinja2 (El motor de plantillas)
'Jinja2 es el motor que usa Flask para permitirnos escribir código lógico (como variables, condiciones y bucles) directamente dentro de un archivo HTML estático. Utiliza unos delimitadores muy específicos:'

'Variables: {{ nombre_variable }}'
'Condicionales: {% if condición %}...{% elif otra_condición %}...{% else %}...{% endif %}'
'Bucles: {% for item in lista %}...{% endfor %}'
