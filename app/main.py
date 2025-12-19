from fastapi import FastAPI

from api.routes import router


app = FastAPI(
    title='FastAPI + Celery Demo',
    description='Учебный проект для фоновых задач',
)

app.include_router(router, prefix="/api")
