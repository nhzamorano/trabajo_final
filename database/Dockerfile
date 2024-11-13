# Imagen base
FROM mysql:8.0

# Copiar el archivo SQL de inicialización al directorio de MySQL que ejecuta scripts al inicio
COPY init.sql /docker-entrypoint-initdb.d/

#
ENV MYSQL_ROOT_PASSWORD=sistemas
ENV MYSQL_DATABASE=citasmedicas
ENV MYSQL_USER=admin
ENV MYSQL_PASSWORD=sistemas
