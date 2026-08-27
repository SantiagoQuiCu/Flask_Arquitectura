from flaskr import create_app
from .modelos import db, Cancion , Album , Usuario , Medio

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

#prueba

with app.app_context():
    a = Album(titulo='Album2', anio=2023, descripcion='Descripcion del album 2', medio=Medio.CD, usuario=1)
    Cancion2 = Cancion.query.get(2)
    Cancion2.albumes.append(a)
    db.session.add(a)
    db.session.commit()