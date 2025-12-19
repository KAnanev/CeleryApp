import time
import logging

from core.celery_app import celery_app


logger = logging.getLogger('CeleryApp')

@celery_app.task(name='demo.add')
def add(x: int, y: int) -> int:
    logger.info("Task started", extra={"x": x, "y": y})
    time.sleep(2)
    logger.info("Task finished")
    return x + y
