from flaskr import create_app
from .modelos import db, Cancion , Album

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

#prueba

with app.app_context():
    c = Cancion(titulo ='Prueba', minutos=2, segundos=25 , interprete ="Santiago")
    c2 = Cancion(titulo ='Prueba2', minutos=2, segundos=25 , interprete ="Santiag")
    db.session.add(c2)
    db.session.commit()
    print(Cancion.query.all())
    a = Album(titulo ='PruebaAlbum', anio=2024, descripcion ="Descripcion de prueba")
    db.session.add(a)
    db.session.commit()
    print(Album.query.all())