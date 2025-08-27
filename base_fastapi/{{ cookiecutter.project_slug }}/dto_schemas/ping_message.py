__all__ = ("PingMessageDTO",)

import datetime

from pydantic import BaseModel, Field


class PingMessageDTO(BaseModel):
    status: str
    server_time: datetime.datetime = Field(default_factory=lambda: datetime.datetime.now(tz=datetime.UTC))
