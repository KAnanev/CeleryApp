from redis import Redis
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str


settings = Settings()
redis_sync: Redis = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    password=settings.REDIS_PASSWORD,
    decode_responses=True,
)
