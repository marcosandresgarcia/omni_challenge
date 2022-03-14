# challenger Omnilatam

This project was made as a challenge and test of skills of a BACK-END python developer.

# Tools

##### 1) Lenguage

- [Python 3.9](https://www.python.org/downloads/release/python-396/ "Python3")

##### 2) IDE

- [Pycharm](https://www.jetbrains.com/es-es/pycharm/download/#section=windows "Pycharm")

##### 3) Data bases


- [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads "PostgreSQL")


# Installation on local

##### 1) Clone or download the project from the repository

`git clone https://github.com/marcosandresgarcia/omni_challenge.git`

##### 2) Create a virtual environment to later install the project libraries

- `python3 -m venv venv` (Windows)

##### 3) Activate the virtual environment of our project

- `cd venv\Scripts\activate.bat` (Windows)

##### 4) Install all the libraries of the project that are in the requirements folder

- `pip install -r requeriments/local.txt`

##### 5) Create the database with the migrations and the superuser to login

- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`


# Installation on Docker

#####  1) Create the environment variables:

#####  2) Build the services:

- `docker-compose build`

#####  3) Start services:

- `docker-compose up`
