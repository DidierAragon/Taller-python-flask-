#Estructura profesional de un proyecto Flask

'''mi_proyecto/
│
├── static/          # Archivos CSS, JavaScript e imágenes
├── templates/       # Archivos HTML (vistas)
├── .gitignore       # Archivos que Git debe ignorar
├── app.py           # Código principal de Flask
├── README.md        # Descripción y guía del proyecto
└── requirements.txt # Librerías instaladas'''

#¿Qué va en cada lugar? 

' static/: Guarda carpetas internas como css/, js/ o img/. Flask busca los archivos aquí automáticamente.'

'templates/: Guarda tus archivos .html (como index.html). Flask los renderiza usando render_template().'

'app.py: El corazón de tu aplicación. Aquí configuras las rutas, la lógica y la base de datos.'

'requirements.txt: La lista de dependencias generada con pip freeze > requirements.txt.'

'.gitignore: Evita que subas basura a GitHub. Debe incluir el entorno virtual (/mi_entorno/) y la base de datos (*.db).'

'README.md: Un archivo de texto (Markdown) que explica de qué trata tu proyecto y cómo ejecutarlo'