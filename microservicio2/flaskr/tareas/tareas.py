from ..modelos import Cancion,CancionSchema
from ..app import db
from celery import Celery
from celery.signals import task_postrun

celery_app = Celery(__name__, broker='redis://localhost:6379/0')

cancion_schema = CancionSchema()

@celery_app.task(name='tabla.registrar')
def registrar_puntaje(cancion_json):
    cancion = Cancion.query.get(cancion_json['id'])
    if not cancion:
        cancion_new = Cancion(titulo=cancion_json['titulo'], minutos=cancion_json['minutos'], segundos=cancion_json['segundos'], interprete=cancion_json['interprete'], puntajes=[cancion_json['puntaje']])
        db.session.add(cancion_new)
    else:
        cancion.puntajes = cancion.puntajes + [cancion_json['puntaje']]
    db.session.commit()

@task_postrun.connect()
def cerrar_sesion(*args, **kwargs):
    db.session.remove()
