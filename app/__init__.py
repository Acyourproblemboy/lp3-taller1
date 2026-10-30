"""Inicialización de la aplicación Flask."""

from flask import Flask
from flask_restful import Api

from app.config import config
from app.models import db
from app.resources.video import Video, VideoList


# Registrar los recursos
def create_app(config_name):
    """Crea y configura una instancia de la aplicación."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    api = Api(app)
    api.add_resource(Video, "/api/videos/<int:video_id>")
    api.add_resource(VideoList, "/api/videos")  # <-- Nuevo endpoint

    with app.app_context():
        db.create_all()

    return app
