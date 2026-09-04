from flaskr import create_app
from flask import Flask
from flask_restful import Resource, Api
from flask import Flask, request
from .modelos import db, Cancion, CancionSchema

app = create_app('default')
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()

api = Api(app)

cancion_schema = CancionSchema()

class VistaTablaPuntaje(Resource):
    def get(self):
        return [cancion_schema.dump(cancion) for cancion in Cancion.query.all()]
        
api.add_resource(VistaTablaPuntaje, '/tablaPuntajes')


