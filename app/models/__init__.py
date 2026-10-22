"""
Inicialización del paquete models.

Aquí se crea la instancia de SQLAlchemy que usan todos los modelos.
Se asocia a la aplicación Flask en create_app() con db.init_app(app).
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

