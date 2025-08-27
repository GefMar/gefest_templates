import logging

from uvicorn.config import LOGGING_CONFIG

from type_stubs.logging_levels import LogLevelsT

from .context_formatter import ContextFormatter


def setup_logging(level: LogLevelsT) -> None:
    config = LOGGING_CONFIG.copy()
    config["loggers"]["uvicorn"]["level"] = level
    config["loggers"]["uvicorn.error"]["level"] = level
    config["loggers"]["uvicorn.access"]["level"] = level

    config["formatters"]["default"] = {
        "()": ContextFormatter,
        "fmt": "[%(asctime)s] [%(levelname)s] [%(service_name)s] [%(environment)s] %(name)s: %(message)s",
        "datefmt": "%Y-%m-%d %H:%M:%S",
    }

    config["loggers"]["app"] = {
        "handlers": ["default"],
        "level": level,
    }

    logging.config.dictConfig(config)
