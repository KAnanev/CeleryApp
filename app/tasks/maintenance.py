from celery import current_task

from core.celery_app import celery_app
from core.config import redis_sync
from core.logging import get_logger


logger = get_logger('CeleryApp', component='maintenance')


@celery_app.task(name='maintenance.heartbeat')
def heartbeat():
    count = redis_sync.incr('maintenance:heartbeat:count')
    logger.info('heartbeat', extra={
        'count': count,
        'task_id': current_task.request.id,

    })
