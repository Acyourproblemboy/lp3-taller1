
## 1. Crear un video (PUT)
{
    "id": 1,
    "name": "Tutorial de Flask",
    "views": 0,
    "likes": 0
}

## consultar video
{
    "id": 1,
    "name": "Tutorial de Flask",
    "views": 0,
    "likes": 0
}
## 2. Actualizar un video (PATCH)

{
    "id": 1,
    "name": "Tutorial de Flask",
    "views": 0,
    "likes": 0
}

## 2. consultar un video si ya existe (PUT 409)
{
    "message": "Ya existe un video con el ID 1"
}

## 2. consultar un video si ya existe (PUT 400)
{
    "message": {
        "likes": "El n\u00famero de likes del video es requerido"
    }
}

## 2. consultar un video si ya existe (PUT 404)
{
    "message": "No se encontr\u00f3 un video con el ID 999"
}