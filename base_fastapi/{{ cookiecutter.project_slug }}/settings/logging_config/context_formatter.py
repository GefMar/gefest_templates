__all__ = ("ContextFormatter",)

import logging

from ..base import get_settings


_settings = get_settings()


class ContextFormatter(logging.Formatter):
    def format(self, record):
        record.environment = _settings.environment
        record.service_name = _settings.app_name
        return super().format(record)
