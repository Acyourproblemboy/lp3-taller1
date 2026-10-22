"""
Recursos (rutas) de la API de Videos.

Un Resource de Flask-RESTful asocia una ruta con un método de Python por
cada método HTTP: get(), put(), patch(), delete().
"""

from flask_restful import Resource, reqparse, abort, fields, marshal_with

from ..models import db
from ..models.video import VideoModel

# Campos que se incluyen al serializar un VideoModel como JSON.
# Lo usa el decorador @marshal_with en cada método.
resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer,
}

# Parser para el cuerpo de las solicitudes PUT (crear video):
# los tres campos son obligatorios.
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="El nombre del video es requerido", required=True)
video_put_args.add_argument("views", type=int, help="El número de vistas del video es requerido", required=True)
video_put_args.add_argument("likes", type=int, help="El número de likes del video es requerido", required=True)

# Parser para el cuerpo de las solicitudes PATCH (actualizar video):
# los tres campos son opcionales, solo se actualiza lo que llegue.
video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Nombre del video")
video_update_args.add_argument("views", type=int, help="Número de vistas del video")
video_update_args.add_argument("likes", type=int, help="Número de likes del video")


def abort_if_video_doesnt_exist(video_id):
    """Busca un video por su ID y lo retorna; si no existe, aborta con 404.

    TODO 1: Consultar la base de datos con
            VideoModel.query.filter_by(id=video_id).first()
            (retorna el video o None si no existe)
    TODO 2: Si el resultado es None, llamar a
            abort(404, message=f"No se encontró un video con el ID {video_id}")
    TODO 3: Si existe, retornar el video
    """
    pass  # <-- reemplaza esta línea por tu implementación


class Video(Resource):
    """Recurso para gestionar un video individual (ruta /api/videos/<video_id>).

    Métodos:
        get: obtener un video por ID
        put: crear un video con un ID específico
        patch: actualizar un video existente
        delete: eliminar un video existente
    """

    @marshal_with(resource_fields)
    def get(self, video_id):
        """Obtiene un video por su ID.

        TODO 1: Obtener el video con abort_if_video_doesnt_exist(video_id)
                (si no existe, esa función ya responde con 404)
        TODO 2: Retornar el video. @marshal_with se encarga de
                convertirlo a JSON usando resource_fields.
        """
        pass  # <-- reemplaza esta línea por tu implementación

    @marshal_with(resource_fields)
    def put(self, video_id):
        """Crea un nuevo video con el ID indicado en la URL.

        TODO 1: Leer los datos enviados en el cuerpo de la solicitud:
                args = video_put_args.parse_args()
        TODO 2: Verificar que NO exista ya un video con ese ID, con
                VideoModel.query.filter_by(id=video_id).first()
                Si existe, llamar a
                abort(409, message=f"Ya existe un video con el ID {video_id}")
        TODO 3: Crear el objeto VideoModel con id=video_id y los valores
                de args["name"], args["views"] y args["likes"]
        TODO 4: Guardarlo en la base de datos:
                db.session.add(video)
                db.session.commit()
        TODO 5: Retornar el video creado junto con el código 201:
                return video, 201
        """
        pass  # <-- reemplaza esta línea por tu implementación

    @marshal_with(resource_fields)
    def patch(self, video_id):
        """Actualiza los campos enviados de un video existente.

        TODO 1: Leer los datos enviados: args = video_update_args.parse_args()
        TODO 2: Obtener el video con abort_if_video_doesnt_exist(video_id)
        TODO 3: Para cada campo (name, views, likes): si el campo llegó en
                la solicitud, actualizar el atributo del video.
                OJO: compara con "is not None" y NO uses "if args['views']:",
                porque 0 es un valor válido (un video puede tener 0 vistas)
                y se interpretaría como "no enviado".
        TODO 4: Guardar los cambios con db.session.commit()
        TODO 5: Retornar el video actualizado
        """
        pass  # <-- reemplaza esta línea por tu implementación

    def delete(self, video_id):
        """Elimina un video existente.

        TODO 1: Obtener el video con abort_if_video_doesnt_exist(video_id)
        TODO 2: Eliminarlo de la base de datos:
                db.session.delete(video)
                db.session.commit()
        TODO 3: Retornar una respuesta vacía con el código 204 (sin contenido):
                return "", 204
        """
        pass  # <-- reemplaza esta línea por tu implementación

