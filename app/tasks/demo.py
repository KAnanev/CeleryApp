import time

from core.celery_app import celery_app


@celery_app.task(name="add")
def add(x, y):
    print("started")
    time.sleep(2)
    print("finished")
    return x + y
