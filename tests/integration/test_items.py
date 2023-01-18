import json

import pytest
from httpx import AsyncClient
from src.app import app


class TestItems:

    @pytest.mark.asyncio
    async def test_put_item(self):
        client = AsyncClient(app=app, base_url="http://localhost")
        item_in = {
            "name": "test_item",
            "description": "an item",
            "base_price": 5
        }
        response = await client.put(f"/api/item", json=item_in)
        assert response.status_code == 200
        response2 = await client.get(f"/api/item?item_id={response.json()['id']}")
        assert response2.json()["id"] == response.json()["id"]
        time_based_price_in = {
            "price": 5,
            "item_id": response.json()['id'],
            "start_hour": 0,
            "end_hour": 0,
            "start_minutes": 0,
            "end_minutes": 0,
            "day_of_the_week": 0
        }
        response3 = await client.put(f"/api/time_based_price", json=time_based_price_in)
        assert len(json.loads(response3.text)["time_based_prices"]) > 0