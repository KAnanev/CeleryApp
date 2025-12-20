# Подключаем .env, если файл существует
# '-' перед include = не падать, если файла нет
-include ../.env

# Экспортируем переменные в shell команд
export


# ======================================================
# Project settings
# ======================================================

# Папка виртуального окружения
VENV=.venv

# Явный путь к python и pip внутри venv
# (мы НЕ используем source activate)
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

# Точка входа Celery:
# app.core.celery_app — модуль
# celery_app          — объект Celery внутри него
CELERY_APP=core.celery_app:celery_app

# Файл с зависимостями
REQ=requirements.txt

# Файл-маркер:
# создаётся после успешной установки зависимостей
# используется make для понимания, что pip уже отработал
REQ_MARKER=$(VENV)/.requirements.installed

# ======================================================
# Docker Redis (dev)
# ======================================================

REDIS_CONTAINER=redis-dev
# Значение по умолчанию, если в .env не задано
REDIS_PORT ?= 6379
REDIS_IMAGE=redis:7

# Запуск Redis в Docker (dev)
# --rm        → контейнер удаляется после остановки
# -p          → проброс порта
# --name      → фиксированное имя контейнера
.PHONY: redis-up
redis-up:
	docker run -d \
		--name $(REDIS_CONTAINER) \
		-p $(REDIS_PORT):6379 \
		$(REDIS_IMAGE)

# Остановка Redis контейнера
.PHONY: redis-stop
redis-stop:
	docker stop $(REDIS_CONTAINER) || true

# Очистка всех данных Redis (dev only!)
.PHONY: redis-flush
redis-flush:
	docker exec $(REDIS_CONTAINER) redis-cli FLUSHALL

# Полный сброс Redis (контейнер + данные)
.PHONY: redis-reset
redis-reset: redis-stop
	docker rm $(REDIS_CONTAINER) || true

# ======================================================
# Virtual environment
# ======================================================

# Создаёт виртуальное окружение, если его ещё нет
# Идемпотентная цель: повторный вызов ничего не делает
.PHONY: venv
venv:
	test -d $(VENV) || python3.11 -m venv $(VENV)

# Полностью удаляет виртуальное окружение
# Используется при "чистой" пересборке
.PHONY: clean
clean:
	rm -rf $(VENV)


# ======================================================
# Pip & dependencies
# ======================================================

# Устанавливает зависимости, ТОЛЬКО если:
#  - изменился requirements.txt
#  - или виртуальное окружение создано заново
#
# После успешной установки создаётся файл-маркер
# $(VENV)/.requirements.installed
$(REQ_MARKER): $(REQ) | venv
	# Обновляем pip и инструменты сборки внутри venv
	$(PYTHON) -m pip install --upgrade pip setuptools wheel

	# Устанавливаем зависимости проекта
	$(PIP) install -r $(REQ)

	# Создаём файл-маркер успешной установки
	touch $(REQ_MARKER)

# Публичная цель для установки зависимостей
# Делегирует работу файловой цели выше
.PHONY: install
install: $(REQ_MARKER)


# ======================================================
# FastAPI
# ======================================================

# Запуск FastAPI приложения в режиме разработки
# Перед запуском гарантирует наличие зависимостей
.PHONY: run
run: install
	$(PYTHON) -m uvicorn main:app \
		--host 0.0.0.0 \
		--port 8000 \
		--reload


# ======================================================
# Celery
# ======================================================

# Запуск Celery worker
# Используется Redis (или другой брокер) из настроек приложения
.PHONY: celery
celery: install
	$(PYTHON) -m celery -A $(CELERY_APP) worker -l info

# Запуск Flower — web-интерфейса мониторинга Celery
# Доступен по адресу http://localhost:5555
.PHONY: flower
flower: install
	$(PYTHON) -m celery -A $(CELERY_APP) flower --port=5555

# ======================================================
# Stop FastAPI
# ======================================================

# Корректно останавливает FastAPI (uvicorn)
# SIGTERM → uvicorn завершает текущие запросы
.PHONY: stop-api
stop-api:
	kill -TERM $$(pgrep -f "uvicorn") 2>/dev/null || true

# ======================================================
# Stop services
# ======================================================

# Корректно останавливает Celery worker
# SIGTERM → Celery завершает текущие задачи
.PHONY: stop-celery
stop-celery:
	pkill -TERM -f "celery.*worker" || true

# Корректно останавливает Flower
.PHONY: stop-flower
stop-flower:
	pkill -TERM -f "celery.*flower" || true

print-env:
	@echo CELERY_BROKER_URL=$(CELERY_BROKER_URL)
	@echo CELERY_RESULT_BACKEND=$(CELERY_RESULT_BACKEND)

