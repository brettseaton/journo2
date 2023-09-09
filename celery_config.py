# celery_config.py
from celery import Celery

celery = Celery(
    'myapp',
    backend='redis://10.72.58.179:6379/0',
    broker='redis://10.72.58.179:6379/0'
)
