from datetime import timedelta

from celery import Celery
from celery.signals import setup_logging as celery_setup_logging

from core.config import settings
from core.logging import setup_logging


@celery_setup_logging.connect
def _setup_celery_logging(**kwargs):
    setup_logging()


celery_app = Celery(
    'celery_app',
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

celery_app.autodiscover_tasks(
    ['tasks'],
)

celery_app.conf.beat_schedule = {
    'maintenance-heartbeat-10st': {
        'task': 'maintenance.heartbeat',
        'schedule': timedelta(seconds=10),
    }
}
