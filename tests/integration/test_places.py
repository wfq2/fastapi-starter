import asyncio
import uuid

import pytest
from src.app import app
from httpx import AsyncClient


class TestPlaces:

    @pytest.mark.asyncio
    async def test_get_places(self):
        client = AsyncClient(app=app, base_url="http://localhost")
        response = await client.put(f"/api/place", json={"name": "test"})
        response2 = await client.get(f"/api/place?place_id={response.json()['id']}")
        assert response2.json()["id"] == response.json()["id"]

    @pytest.mark.asyncio
    async def test_insert_tons_of_places(self):
        client = AsyncClient(app=app, base_url="http://localhost")

        async def insert_many(num_inserts):
            for i in range(num_inserts):
                await client.put(f"/api/place", json={"name": str(uuid.uuid4())})

        await asyncio.gather(*[insert_many(400) for i in range(10)])
        print("test")
