from fastapi import FastAPI

from api.routes import router
from core.logging import setup_logging


setup_logging()

app = FastAPI(
    title='FastAPI + Celery Demo',
    description='Учебный проект для фоновых задач',
)

app.include_router(router, prefix="/api")
