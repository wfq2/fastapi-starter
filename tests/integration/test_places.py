import uuid

import pytest
from fastapi.testclient import TestClient
from src.app import app
from httpx import AsyncClient


class TestPlaces:

    @pytest.mark.asyncio
    async def test_get_places(self, db_session):
        client = AsyncClient(app=app, base_url="http://localhost")
        response = await client.put(f"/api/place", json={"name": "test"})
        response2 = await client.get(f"/api/place?id={response.json()['id']}")
        assert response2.json()["id"] == response.json()["id"]
