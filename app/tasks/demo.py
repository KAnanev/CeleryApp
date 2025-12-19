import logging
import time

from core.celery_app import celery_app
from core.config import redis_sync

logger = logging.getLogger('CeleryApp')

@celery_app.task(
    name='demo.add',
    acks_late=True,
    autoretry_for=(Exception,),
    retry_kwargs={'max_retries': 3},
    retry_backoff=2,
    soft_time_limit=5,
    time_limit=7,
)
def add(x: int, y: int, request_id: str) -> int:
    cached = redis_sync.get(request_id)
    if cached is not None:
        logger.info("Cached result", extra={"request_id": request_id})
        return int(cached)

    if x < 0:
        raise ValueError("x must be >= 0")

    logger.info("Task started", extra={"x": x, "y": y, "request_id": request_id})

    time.sleep(2)
    result = x + y

    redis_sync.set(request_id, result, ex=3600)

    logger.info("Task finished", extra={"request_id": request_id})
    return result
