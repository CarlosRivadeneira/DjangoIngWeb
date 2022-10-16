# DjangoIngWeb
Aplicación web con Django y Sqlite3 - Carlos Rivadeneira

## Descripción
La aplicación web es un sistema login que posee un CRUD de tareas de una empresa que los aparta por finalizados o por completar, también los resalta
por importancia y brinda información horaria correspondiente a la finalización de tareas.

Se utilizó el framework Django ya que implementa el lenguaje de programación Python y da conexión con HTML, cuenta con un sistema de autenticación 
de usuarios, maneja diferentes tipos de versiones, trabaja por medio de un patrón MVC y cuenta con un panel de administración nativo del framework, mismo
que puede ser ampliado mediante el uso de código.

Se espera que el proyecto pueda ser desplegado mediante un servicio que permite el uso de framework.

## Prerequisitos
Para poder ejecutar el código se necesita de una versión de Python, Venv(Entorno Virtual) y Visual Studio Code

## Instalación
Este proyecto está basado en el Framework de Django y es necesario su instalación mediante un aterminal de Visual Studio Code con el siguiente comando:
```bash
python3 -m pip install Django
```

Para poder instalar el entorno virtual de Python se necesita ejecutar el siguiente código dentro de la terminal:
```bash
python3 -m venv venv
```
Este comando creará el directorio venv dentro del proyecto con el entorno virtual

Para poder ejecutar la aplicación dentro de localhost se necesita abrir la ruta donde se encuentra el archivo manage.py y ejecutar el comando:
```bash
python manage.py runserver
```
Esto abrirá un despliegue local en el que se puede abrir la aplicación en un navegador como Chrome
