from fastapi import FastAPI
from dotenv import load_dotenv


from api.routes import router


load_dotenv()

app = FastAPI(
    title='FastAPI + Celery Demo',
    description='Учебный проект для фоновых задач',
)

app.include_router(router, prefix="/api")
