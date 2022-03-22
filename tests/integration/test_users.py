import pytest
from httpx import AsyncClient

from src.app import app


class TestUsers:

    @pytest.mark.asyncio
    async def test_put_user(self):
        client = AsyncClient(app=app, base_url="http://localhost")
        response = await client.put(f"/api/user", json={"first_name": "w", "last_name": "lname", "email": "wfq2@cornell.edu", "password": "test"})
        print(response.status_code == 200)

    @pytest.mark.asyncio
    async def test_put_user_and_get_token(self):
        client = AsyncClient(app=app, base_url="http://localhost")
        response = await client.put(f"/api/user",
                                    json={"first_name": "w", "last_name": "lname", "email": "wfq2@cornell.edu",
                                          "password": "test"})
        print(response.json())
        assert response.status_code == 200
        form_data = {"username": "wfq2@cornell.edu", "password": "test"}
        login_response = await client.post("/api/users/token", data=form_data)
        print(login_response.json())