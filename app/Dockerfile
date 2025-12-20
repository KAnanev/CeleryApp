FROM python:3.11-slim

WORKDIR /app

# (опционально) чтобы меньше проблем с правами на запись в /app
RUN useradd -m -u 10001 celery

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ВАЖНО: дать права пользователю celery на рабочую директорию
RUN chown -R celery:celery /app

ENV PYTHONPATH=/app

USER celery

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
