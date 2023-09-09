# celery_config.py
from celery import Celery

celery = Celery(
    'myapp',
    backend='redis://localhost:6379/0',
    broker='redis://localhost:6379/0'
)
