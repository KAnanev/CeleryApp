import logging
import logging.config
from typing import Any


# =========================
# LoggerAdapter
# =========================

class ContextLogger(logging.LoggerAdapter):
    def process(self, msg: str, kwargs: dict[str, Any]):
        kwargs.setdefault("extra", {})
        kwargs["extra"].setdefault("count", "-")
        kwargs["extra"].setdefault("task_id", "-")
        kwargs["extra"].setdefault("component", self.extra.get("component", "-"))
        return msg, kwargs


# =========================
# Logging config
# =========================

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,  # ВАЖНО!
    "formatters": {
        "default": {
            "format": (
                "%(asctime)s | "
                "%(levelname)-8s | "
                "%(name)s | "
                "%(component)s | "
                "%(message)s | "
                "count=%(count)s | "
                "task_id=%(task_id)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "celery": {
            "format": (
                "%(asctime)s | "
                "%(levelname)-8s | "
                "%(name)s | "
                "%(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
        "celery_console": {
            "class": "logging.StreamHandler",
            "formatter": "celery",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        # Celery internal logs
        "celery": {
            "handlers": ["celery_console"],
            "level": "INFO",
            "propagate": False,
        },
        "kombu": {
            "handlers": ["celery_console"],
            "level": "INFO",
            "propagate": False,
        },
        "amqp": {
            "handlers": ["celery_console"],
            "level": "WARNING",
            "propagate": False,
        },
    },
}


def setup_logging() -> None:
    logging.config.dictConfig(LOGGING_CONFIG)


def get_logger(name: str, component: str | None = None) -> ContextLogger:
    base = logging.getLogger(name)
    return ContextLogger(base, {"component": component or name})
