from celery import Celery

celery_app = Celery(__name__, broker='redis://localhost:6379/0')

@celery_app.task(name='registrar_log')
def registrar_log(nombre_usuario, fecha_hora):
    with open('log_singin.txt', 'a+') as f:
        f.write(f'Usuario: {nombre_usuario}, Fecha y hora: {fecha_hora}\n')