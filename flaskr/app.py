from flaskr import create_app
from .modelos import db, Cancion , Album , Usuario , Medio
from .modelos import AlbumSchema
from flask_restful import Api
from .vistas import VistaCanciones, VistaCancion

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaCanciones, '/canciones')
api.add_resource(VistaCancion, '/canciones/<int:cancion_id>')