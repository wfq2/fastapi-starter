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
        assert response.status_code == 200
        form_data = {"username": "wfq2@cornell.edu", "password": "test"}
        login_response = await client.post("/api/users/token", data=form_data)
        assert login_response.status_code == 200
        assert login_response.json()["access_token"]
        return login_response.json()["access_token"]

    @pytest.mark.asyncio
    async def test_get_user_by_token(self):
        client = AsyncClient(app=app, base_url="http://localhost")
        token = await self.test_put_user_and_get_token()
        response = await client.get(f"/api/user/me", headers={"Authorization": f"Bearer {token}"})
        print(response.json())
        assert response.json()["first_name"] == "w"
