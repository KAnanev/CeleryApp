import logging

from redis import Redis
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str
    REDIS_HOST: str
    REDIS_PORT: int


settings = Settings()
redis_sync: Redis = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    decode_responses=True,
)
logger = logging.getLogger('CeleryApp')
