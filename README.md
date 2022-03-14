# Reto Omnilatam

Este proyecto se realiza como reto y prueba de habilidades de un programador BACK-END python.


# Herramientas

##### 1) Lenguaje de programación

- [Python 3.9](https://www.python.org/downloads/release/python-396/ "Python3")

##### 2) IDE

- [Pycharm](https://www.jetbrains.com/es-es/pycharm/download/#section=windows "Pycharm")

##### 3) Motor de base de datos


- [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads "PostgreSQL")


# Instalacion en local

##### 1) Clonar o descargar el proyecto del repositorio

`git clone https://github.com/marcosandresgarcia/reto_omni.git`

##### 2) Crear un entorno virtual para posteriormente instalar las librerias del proyecto

- `python3 -m venv venv` (Windows)
-  `virtualenv venv -ppython3` (Linux)

##### 3) Activar el entorno virtual de nuestro proyecto

- `cd venv\Scripts\activate.bat` (Windows)
- `source venv/bin/active` (Linux)

##### 4) Instalar todas las librerias del proyecto que se encuentran en la carpeta requeriments

- `pip install -r requeriments/local.txt`

##### 5) Crear la base de datos con las migraciones y el superuser para iniciar sesión

- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`


# Instalación en Docker

#####  1) Cree las variables de entorno:

#####  2) Construya los servicios:

- `docker-compose build`

#####  3) Inicie servicios:

- `docker-compose up`
