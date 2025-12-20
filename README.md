
# 🚀 FastAPI + Celery + Redis + Flower

Полноценный учебный и продакшен-ориентированный проект для изучения **Celery**  
в связке с **FastAPI**, **Redis**, **Celery Beat** и **Flower**.

Проект доведён до состояния, пригодного для:
- дипломной работы
- pet-проекта
- базового продакшен-шаблона

---

## 🧱 Архитектура

```text
Client
  ↓
FastAPI (HTTP API)
  ↓
Redis (broker / result backend)
  ↓
Celery Worker (фоновые задачи)
  ↑
Celery Beat (периодические задачи)

Flower — мониторинг Celery
```

---

## 📁 Структура проекта

```text
project-root/
├── docker-compose.yml
├── .env
└── app/
    ├── Dockerfile
    ├── requirements.txt
    ├── main.py
    ├── api/
    │   └── routes.py
    ├── core/
    │   ├── celery_app.py
    │   ├── config.py
    │   ├── logging.py
    │   └── schemas.py
    ├── tasks/
    │   ├── __init__.py
    │   ├── demo.py
    │   └── maintenance.py
```

---

## ⚙️ Используемые технологии

- Python 3.11
- FastAPI
- Celery 5
- Redis 7
- Celery Beat
- Flower
- Docker / Docker Compose

---

## 🔐 Безопасность

- Redis изолирован в приватной Docker-сети
- Redis защищён паролем (AUTH)
- Worker и Beat не имеют публичных интерфейсов
- Flower защищён basic-auth
- Все секреты передаются через `.env`

---

## 🧠 Принципы Celery

- **at-least-once delivery**
- идемпотентные задачи
- retry только для внешних зависимостей
- инфраструктурные ошибки решаются инфраструктурой

---

## 🐳 Docker

### Dockerfile
Используется **один Docker-образ** для:
- FastAPI
- Celery worker
- Celery beat
- Flower

Контейнеры запускаются под **не-root пользователем**.

---

## ▶️ Запуск проекта

### 1️⃣ Подготовить `.env`

```env
API_PORT=8000
FLOWER_PORT=5555

REDIS_HOST=redis
REDIS_PORT=6379
REDIS_PASSWORD=supersecret

CELERY_BROKER_URL=redis://:${REDIS_PASSWORD}@redis:6379/0
CELERY_RESULT_BACKEND=redis://:${REDIS_PASSWORD}@redis:6379/1

FLOWER_BASIC_AUTH=admin:admin
```

---

### 2️⃣ Запуск

```bash
docker compose up --build
```

---

### 3️⃣ Доступы

| Сервис | URL |
|-----|----|
| FastAPI | http://localhost:8000/docs |
| Flower | http://localhost:5555 |
| Redis | доступен только внутри Docker |

---

## 🧪 Примеры задач

### Периодическая задача (Heartbeat)

```python
@celery_app.task(name='maintenance.heartbeat')
def heartbeat():
    count = redis_sync.incr('maintenance:heartbeat:count')
    logger.info(
        'heartbeat',
        extra={
            'count': count,
            'task_id': current_task.request.id,
        },
    )
```

---

## 🩺 Мониторинг

### Flower
- состояние worker'ов
- список задач
- retry / failures
- состояние broker (Redis)

---

## 🛑 Остановка

Корректная остановка:

```bash
docker compose down
```

Контейнерам отправляется `SIGTERM`,  
Celery корректно завершает работу.

---

## 🏁 Статус проекта

✅ Архитектура  
✅ Docker  
✅ Celery worker / beat  
✅ Мониторинг  
✅ Безопасность  

---

## 📚 Документация

- Celery — https://docs.celeryq.dev
- FastAPI — https://fastapi.tiangolo.com
- Flower — https://flower.readthedocs.io

---
