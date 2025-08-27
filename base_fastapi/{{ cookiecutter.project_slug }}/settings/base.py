from functools import lru_cache
import pathlib

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
import toml

from type_stubs.logging_levels import LogLevelsT

from .paths import BASE_DIR


_pyproject_data = toml.load(BASE_DIR.joinpath("pyproject.toml"))


class Settings(BaseSettings):
    app_name: str = _pyproject_data["project"]["name"]
    version: str = _pyproject_data["project"]["version"]
    environment: str = Field(
        default="local_development",
        description="Environment in which the application is running (e.g., development, production, staging)",
    )
    log_level: LogLevelsT = Field(
        default="INFO",
        description="Logging level for the application (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)",
    )
    debug: bool = Field(default=False, description="Enable debug mode")
    base_dir: pathlib.Path = BASE_DIR
    pytest_running: bool = Field(default=False, description="Run pytest")


@lru_cache
def get_settings() -> Settings:
    """
    Get the application settings.
    Uses LRU cache to store the settings for performance.
    """
    return Settings()
