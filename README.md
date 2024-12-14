# FINAL PROJECT

Este repositorio contiene un proyecto desarrollado en Python. Sigue las instrucciones a continuación para configurar el entorno y ejecutar el proyecto.

## Requisitos

Asegúrate de tener instalado:

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Configuración de variables de entorno

```
# MYSQL
AWS_MYSQL_URL=
AWS_MYSQL_PORT=
AWS_MYSQL_USER=
AWS_MYSQL_PASSWORD=
AWS_MYSQL_DB_NAME=

# S3
AWS_S3_REGION=
AWS_S3_BUCKET_NAME=
AWS_S3_ACCESS_KEY=
AWS_S3_SECRET_ACCESS_KEY=

# IMAGGA
IMAGGA_API_KEY=
IMAGGA_API_SECRET=
IMAGGA_ENDPOINT=

```

## Configuración del entorno de desarrollo sin Docker

1. **Crear el entorno virtual**:
   Ejecuta el siguiente comando para crear un entorno virtual en la carpeta `venv`:
   ```bash
   python -m venv venv
   ```
2. **Activar el ambiente virtual**:
   Ejecutar el siguiente comando para activar el ambiente virtual `venv`:

    - Para activar en Linux y MacOs ejecutar el siguiente comando:
   ```bash
   source venv/bin/activate
   ```

    - Para activar en Windows ejecutar el siguiente comando:
   ```bash
   activate
   ```

3. **Crear el entorno virtual**:
   Ejecuta el siguiente comando para crear un entorno virtual en la carpeta `venv`:
   ```bash
   pip install -r requirements.txt
   ```

## Levantamiento del servidor

**Ejecutar la aplicación**: ejecutar el archivo principal `run.py`

   ```bash
      pip index.py
   ```

## Configuración del entorno con Docker

1. **Generar instancia de Docker**:

   ```bash
   docker build -t flask_meme_app .
   ```
2. **Ejecutar la Instancia**:

   ```bash
   docker run -it -p 7000:5000 flask_meme_app
   ```
3. **Ejecutar la instancia y almacenarla**:

   Este comando correra la instancia de Docker y la almacenara dentro del contexto de Docker.
   ```bash
   docker run -d -p 80:5000 --name flask_meme_app flask_meme_app
   ```
   
