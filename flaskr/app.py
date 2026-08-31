from flaskr import create_app
from .modelos import db, Cancion , Album , Usuario , Medio
from .modelos import AlbumSchema

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

#prueba

with app.app_context():
    album_schema = AlbumSchema()
    A = Album(titulo="Album 1", anio=2023, descripcion="Descripcion del album 1", medio=Medio.DISCO)
    db.session.add(A)
    db.session.commit()
    print([album_schema.dumps(album) for album in Album.query.all()])   