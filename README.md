# Lenguaje de Programación 3 - Taller 1

![commits](https://badgen.net/github/commits/Acyourproblemboy/lp3-taller1?icon=github) 
![last_commit](https://img.shields.io/github/last-commit/Acyourproblemboy/lp3-taller1)

- ver [badgen](https://badgen.net/) o [shields](https://shields.io/) para otros tipos de _badges_

## Autor

- [Andres Stivens Cortes Ponce](https://github.com/Acyourproblemboy/lp3-taller1.git)

## Descripción del Proyecto

    Es una API desarrollada en Python utilizando Flask, Flask-RESTful y Flask-SQLAlchemy para la gestión de un catálogo de videos. La aplicación permite almacenar, consultar, actualizar y eliminar registros de videos (con campos para id, título, número de vistas y likes) guardados en una base de datos SQLite.
    Además, incluye mejoras adicionales como la obtención de la lista completa de videos y tambien se puede filtrar  por nombre y paginación de resultados

## Instalación

Sigue estos pasos para instalar y ejecutar el proyecto en tu entorno local:

1. Clonar el proyecto
```bash
git clone https://github.com/Acyourproblemboy/lp3-taller1.git
```

2. Revisar la [`GUIA.md`](docs/GUIA.md)

# Crear el entorno virtual (se creará una carpeta venv/)
python3 -m venv venv
# Activarlo (Linux/WSL2)
source venv/bin/activate
pip install -r requirements.txt
pip install flask flask-restful flask-sqlalchemy
## Paso 10 — Ejecutar y probar la API

Con el entorno virtual activado y parado en la raíz del proyecto:

```bash
python3 run.py
```