# celery_config.py
from celery import Celery

celery = Celery(
    'myapp',
    backend='redis://localhost:6380/0',
    broker='redis://localhost:6380/0'
)
