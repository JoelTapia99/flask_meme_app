# FINAL PROJECT

Este repositorio contiene un proyecto desarrollado en Python. Sigue las instrucciones a continuación para configurar el
entorno y ejecutar el proyecto.

## Requisitos

Asegúrate de tener instalado:

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Configuracion de variables de entorno

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

## Configuración del entorno

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
      pip run.py 
   ```

```
git clone https://github.com/FaztWeb/flask-sqlalchemy-crud
cd flask-sqlalchemy-crud
pip install -r requirements.txt
python index.py
```