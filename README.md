# 🚀 FastAPI + Celery + Redis — учебный проект

Учебный проект для изучения **Celery** и интеграции его с **FastAPI**.  
Проект демонстрирует корректную архитектуру фоновых задач, пригодную для продакшена и дипломной работы.

---

## 🧱 Архитектура

- **FastAPI** — принимает HTTP-запросы
- **Celery** — выполняет фоновые задачи
- **Redis** — broker + result backend
- API и Celery worker запускаются **как отдельные процессы**

```text
Client → FastAPI → Redis (broker) → Celery Worker
```

---

## 📁 Структура проекта

```text
app/
├── main.py                 # FastAPI приложение
├── core/
│   └── celery_app.py       # Инициализация Celery
├── api/
│   └── routes.py           # HTTP endpoints
└── tasks/
    └── demo.py             # Celery задачи
```

---

## 📦 Установка зависимостей

```bash
pip install fastapi uvicorn celery redis
```

(опционально для типизации)
```bash
pip install celery-types
```

---

## 🧠 Переменные окружения

```bash
export CELERY_BROKER_URL=redis://localhost:6379/0
export CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

---

## 🟥 Запуск Redis

```bash
docker run -d --name redis -p 6379:6379 redis:7
```

Проверка:
```bash
redis-cli ping
# PONG
```

---

## ▶️ Запуск FastAPI

```bash
uvicorn app.main:app --reload
```

---

## ⚙️ Запуск Celery worker

```bash
celery -A app.core.celery_app worker -l info
```

Для отладки:
```bash
celery -A app.core.celery_app worker -P solo -l info
```

---

## 📬 Вызов фоновой задачи

```http
POST /tasks
Content-Type: application/json

{
  "message": "Hello Celery"
}
```

Ответ:
```json
{
  "task_id": "uuid"
}
```

---

## 📌 Принципы

- Celery app создаётся один раз
- FastAPI и worker — разные процессы
- Все настройки через env

---

## 📚 Документация

https://docs.celeryq.dev/en/stable/
