import pytest
from httpx import AsyncClient
from typing import Generator

from app.main import app


@pytest.fixture
async def async_client() -> Generator:
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
