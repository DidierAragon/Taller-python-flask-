#Entornos virtuales — venv
'Un entorno virtual es una herramienta que crea un espacio aislado para tus proyectos de Python. es como una "caja fuerte" para cada proyecto, permitiendo que cada uno tenga sus propias librerías y versiones sin interferir con los demás ni con la configuración general de tu computadora.'

#Crear el entorno virtual
'python -m venv mi_entorno'

#Activar el entorno virtual
# Windows
'mi_entorno\Scripts\activate'
# macOS/Linux
'source mi_entorno/bin/activate'

'Cómo saber si funcionó Verás el nombre de tu entorno entre paréntesis al inicio de la línea de comandos'

#Instalar paquetes
'Una vez activado, cualquier librería que instales usando pip se quedará guardada únicamente dentro de ese entorno virtual.'

'pip install nombre_paquete'

#Generar el archivo requirements.txt
'Para que otra persona (o para uno mismo pero  en otra computadora) se puede replicar exactamente las mismas librerías del proyecto, exportando la lista de paquetes instalados usando pip freeze > requirements.txt.'

#Para instalar desde un requirements.txt:
'Si descargo un proyecto que ya tiene este archivo, lo unico que debo hacer es activarlo a tu entorno virtual y corres:'
'pip install -r requirements.txt'

#Desactivar el entorno virtual
'Una vez que hayas terminado de trabajar, puedes salir del entorno virtual con el comando deactivate.'
