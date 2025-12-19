import os

from celery import Celery


CELERY_BROKER_URL = os.getenv('BACKEND')
CELERY_RESULT_BACKEND = os.getenv('BROKER')

if not CELERY_BROKER_URL or not CELERY_RESULT_BACKEND:
    raise RuntimeError('Url is not set')

celery_app = Celery(
    'celery_app',
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND,
)

celery_app.autodiscover_tasks(
    ['tasks'],
    related_name='demo',
)
