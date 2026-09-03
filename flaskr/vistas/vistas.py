from flask_restful import Resource

from flaskr.modelos.modelos import Usuario, UsuarioSchema
from ..modelos import db, Cancion, CancionSchema
from flask import request
from flask_jwt_extended import jwt_required, create_access_token

cancion_schema = CancionSchema()
usuario_schema = UsuarioSchema()

class VistaCanciones(Resource):
    @jwt_required()
    def get(self):
        return [cancion_schema.dump(cancion) for cancion in Cancion.query.all()]
    
    @jwt_required()
    def post(self):
        nueva_cancion = Cancion(titulo=request.json['titulo'],
                                minutos=request.json['minutos'],
                                segundos=request.json['segundos'],
                                interprete=request.json['interprete'])
        db.session.add(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)


class VistaCancion(Resource):
    @jwt_required()
    def get(self, cancion_id):
        cancion = Cancion.query.get_or_404(cancion_id)
        return cancion_schema.dump(cancion)
    @jwt_required()
    def put(self, cancion_id):
        cancion = Cancion.query.get_or_404(cancion_id)
        cancion.titulo = request.json.get('titulo',cancion.titulo)
        cancion.minutos = request.json.get('minutos',cancion.minutos)
        cancion.segundos = request.json.get('segundos',cancion.segundos)
        cancion.interprete = request.json.get('interprete',cancion.interprete)
        db.session.commit()
        return cancion_schema.dump(cancion)
    @jwt_required()
    def delete(self, cancion_id):
        cancion = Cancion.query.get_or_404(cancion_id)
        db.session.delete(cancion)
        db.session.commit()
        return 'Operacion Exitosa', 204
    
class VistaSignIn(Resource):
    def post(self):
        nuevo_usuario = Usuario(nombre=request.json['nombre'], contraseña=request.json['contrasena'])
        token_de_acceso = create_access_token(identity=request.json['nombre'])
        db.session.add(nuevo_usuario)
        db.session.commit()
        return {'mensaje':'Usuario creado exitosamente','token_de_acceso': token_de_acceso}, 201