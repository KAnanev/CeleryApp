import os

from celery import Celery

from dotenv import load_dotenv
load_dotenv()

BACKEND = os.getenv('BACKEND')
BROKER = os.getenv('BROKER')

celery_app = Celery(
    'celery_app',
    broker=BROKER,
    backend=BACKEND,
)

celery_app.autodiscover_tasks(
    ['tasks'],
    related_name='demo',
)
