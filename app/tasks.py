import time

from app.celery_app import celery_app


@celery_app.task
def add(x, y):
    print("started")
    time.sleep(2)
    print("finished")
    return x + y
