from flask_restful import Resource
from ..modelos import db, Cancion, CancionSchema
from flask import request

cancion_schema = CancionSchema()

class VistaCanciones(Resource):
    def get(self):
        return [cancion_schema.dump(cancion) for cancion in Cancion.query.all()]
    
    def post(self):
        nueva_cancion = Cancion(titulo=request.json['titulo'],
                                minutos=request.json['minutos'],
                                segundos=request.json['segundos'],
                                interprete=request.json['interprete'])
        db.session.add(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)

class VistaCancion(Resource):
    def get(self, cancion_id):
        cancion = Cancion.query.get_or_404(cancion_id)
        return cancion_schema.dump(cancion)
    
    def put(self, cancion_id):
        cancion = Cancion.query.get_or_404(cancion_id)
        cancion.titulo = request.json.get('titulo',cancion.titulo)
        cancion.minutos = request.json.get('minutos',cancion.minutos)
        cancion.segundos = request.json.get('segundos',cancion.segundos)
        cancion.interprete = request.json.get('interprete',cancion.interprete)
        db.session.commit()
        return cancion_schema.dump(cancion)
    
    def delete(self, cancion_id):
        cancion = Cancion.query.get_or_404(cancion_id)
        db.session.delete(cancion)
        db.session.commit()
        return 'Operacion Exitosa', 204