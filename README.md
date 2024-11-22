# Sistema de Citas Medicas
Proyecto Citas Medicas

# Creado por:
- Samuel Acevedo
- Laura Gabriela Capera
- Natanael Herrera

## Descripción

Este proyecto consiste en el desarrollo de un sistema para la generacio de citas medicas, 
con el fin de prestar un mejor servicio a la comunidad.

La aplicacion consta de datatabse, backend, frontend todo empaquetado en contenedores docker y se accesa a travez del contendor proxy.

# Database
La base de datos se llama citasmedicas, creada en mysql 8.0, consta de tabalas para citas medics, pacientes y medicos.
entro de la carpeta encontrara el respectivo Dockerfile con la definicion del contenedor que se usara para desplegarla.

# Backend
Es un proyecto en python, la api construida en FastApi, se conecta a la base de datos citasmedicas, para procesar la informacion.
Dentro de la carpeta encontrara el respectivo Dockerfile con la definicion del contenedor que se usara para desplegarlo.

# Frontend
Proyecto construido en python usando el Framework Flask y consume la api del backend.
Dentro de la carpeta encontrara el respenctivo archivo Dockerfile, que usara para desplegarlo

# Proxy
Construido sobre nginx, se conecta al frontend al puerto 5000 de flask que corre en el contenedor del frontend.
Cuenta con su archivo Dockerfile un archivo de configuracion del proxy reverso de nginx


# Interfaz de Documentación Interactiva de la API
Dentro del backend corre elserviro uvicorn main:app --reload, el cual redirecciona a la url http://localhost:8000/docs
La interfaz generada automáticamente basada en Swagger UI, uvicorn para probar APIs RESTful localmente.

# Archivo docker-compose
El archivo docker-compose.yml contiene la informacio para construir cada contenedor, esta ubicado en la raiz del proyecto.

# Intalacion
Pudes clonar el proyecto desde github
git clone https://github.com/nhzamorano/trabajo_final.git

# INstalacion LOcal
Instala las dependencias desde el archivo requirements.txt
pip install -r requirements.txt

# Instalacion en docker
Ejecutas en linux donde previamente hayas instaldo docker: docker compose up --build -d ubicado en la raiz del proyecto donde este el docker-compose.yml
