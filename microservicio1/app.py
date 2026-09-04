from microservicio1 import create_app
from flask_restful import Resource, Api
from flask import Flask, request
import requests
import json
from celery import Celery

celery_app = Celery(__name__, broker='redis://localhost:6379/0')

@celery_app.task(name='tabla.registrar')
def registrar_puntaje(cancion):
    pass

app = create_app('default')
app.context = app.app_context()
app.context.push()

api = Api(app)

class VistaPuntaje(Resource):
    def post(self,id_cancion):
        content = requests.get(f'http://127.0.0.1:5000/cancion/{id_cancion}')
        if content.status_code == 404:
            return content.json(), 404
        else :
            cancion = content.json()
            cancion['puntaje'] = request.json['puntaje']
            args = (cancion,)
            registrar_puntaje.apply_async(args)
            return json.dumps(cancion)
        
api.add_resource(VistaPuntaje, '/cancion/<int:id_cancion>/puntuar')