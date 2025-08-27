__all__ = ("APP_STARTUP_TIME",)

from prometheus_client import Gauge


APP_STARTUP_TIME = Gauge("app_startup_duration_seconds", "Time it took to start the FastAPI app (lifespan)")
