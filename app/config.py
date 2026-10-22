"""
Configuración de la aplicación Flask.

Cada clase representa un ambiente. La función create_app() recibe el
nombre del ambiente y carga la clase correspondiente.
"""


class DevelopmentConfig:
    """Configuración para el entorno de desarrollo."""

    DEBUG = True
    # Con Flask-SQLAlchemy 3.x, una ruta relativa de SQLite se crea dentro
    # de la carpeta instance/ (instance/database.db)
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig:
    """Configuración para el entorno de producción."""

    DEBUG = False
    # En producción se recomendaría usar un motor más robusto (PostgreSQL, MySQL)
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig:
    """Configuración para pruebas: base de datos en memoria."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# Diccionario para seleccionar la configuración según el ambiente
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}

