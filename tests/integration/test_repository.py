import pytest

from src.places.db.place_dbo import PlaceDBO
from tests.integration.helpers import get_default_place_dbo


class TestRepository:

    @pytest.mark.asyncio
    async def test_put(self, repository):
        dbo = get_default_place_dbo()
        r = await repository.put(dbo)
        assert r == dbo
        get_response = await repository.get(PlaceDBO, dbo.id)
        assert get_response == dbo

    @pytest.mark.asyncio
    async def test_upsert(self, repository):
        dbo = get_default_place_dbo()
        async with repository.db_session.begin():
            r = await repository.put(dbo)
        assert r == dbo
        dbo.name = "updated_name"
        upsert_response = await repository.upsert(PlaceDBO, dbo.id, dbo)
        assert upsert_response.name == "updated_name"
        get_response = await repository.get(PlaceDBO, dbo.id)
        assert get_response.id == dbo.id
        assert get_response.name == "updated_name"
