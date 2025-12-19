# Celery + Redis — быстрый старт

## 1. Установка зависимостей

```bash
pip install celery redis
```

(опционально для типизации)
```bash
pip install celery-types
```

---

## 2. Запуск Redis

### Через Docker (рекомендуется)
```bash
docker run -d --name redis -p 6379:6379 redis:7
```

### Через систему (Ubuntu)
```bash
sudo apt install redis-server
sudo systemctl start redis
```

Проверка:
```bash
redis-cli ping
# PONG
```

---

## 3. Запуск Celery worker

```bash
celery -A app.celery_app worker -l info
```

или (для dev / отладки):
```bash
celery -A app.celery_app worker -P solo -l info
```

---

## 4. Вызов задачи

```python
from app.tasks import add

result = add.delay(2, 3)
print(result.id)
```

Проверка статуса:
```python
from celery.result import AsyncResult

r = AsyncResult(task_id)
print(r.status)
print(r.result)
```

---

## Документация

https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html
