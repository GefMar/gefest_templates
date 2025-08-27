from http import HTTPStatus

from httpx import ASGITransport, AsyncClient
import pytest

from app import app


@pytest.mark.asyncio
async def test_ping():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/ping")

    assert response.status_code == HTTPStatus.OK
    assert response.headers["content-type"] == "application/json"
    response_data = response.json()
    assert response_data["status"] == "OK"
    assert "server_time" in response_data
