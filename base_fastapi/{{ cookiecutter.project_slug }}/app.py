from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
import logging
import time
from typing import Any

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from prometheus_fastapi_instrumentator import Instrumentator

from metrics import APP_STARTUP_TIME
import routes
from settings import get_settings
from settings.logging_config import setup_logging


_settings = get_settings()
setup_logging(_settings.log_level)
_logger = logging.getLogger("app")
_instrumentator = Instrumentator(
    should_group_status_codes=True,
    should_ignore_untemplated=True,
)


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, Any]:
    _logger.info("lifespan: starting up...")
    start = time.perf_counter()
    _app.state.settings = _settings
    duration = time.perf_counter() - start
    APP_STARTUP_TIME.set(duration)
    _instrumentator.expose(_app, include_in_schema=False)
    yield
    _logger.info("Lifespan: shutting down...")


app = FastAPI(
    title=f"{_settings.app_name} API",
    description="",
    version="1.0.0",
    lifespan=lifespan,
    default_response_class=ORJSONResponse,
)

app.include_router(routes.root_router, prefix="")
_instrumentator.instrument(app, metric_namespace=_settings.app_name)
