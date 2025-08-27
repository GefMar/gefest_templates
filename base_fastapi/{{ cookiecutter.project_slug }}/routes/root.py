__all__ = ("root_router",)

from fastapi import APIRouter

from dto_schemas.ping_message import PingMessageDTO


root_router = APIRouter(
    prefix="",
    tags=["root"],
)


@root_router.get("/ping")
async def ping() -> PingMessageDTO:
    return {"status": "OK"}
