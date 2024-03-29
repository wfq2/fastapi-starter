import pytest

from container.request_context import current_session
from src.places.db.place_dbo import PlaceDBO
from tests.integration.helpers import get_default_place_dbo


class TestRepository:

    @pytest.mark.asyncio
    async def test_insert(self, repository, db_session):
        current_session.set(db_session)
        dbo = get_default_place_dbo()
        async with repository.db_session.begin():
            r = await repository.insert(dbo)
        assert r == dbo
        get_response = await repository.get_by_id(PlaceDBO, dbo.id)
        assert get_response == dbo

    @pytest.mark.asyncio
    async def test_upsert(self, repository, db_session):
        current_session.set(db_session)
        dbo = get_default_place_dbo()
        async with repository.db_session.begin():
            r = await repository.insert(dbo)
        assert r == dbo
        dbo.name = "updated_name"
        await repository.upsert(PlaceDBO, dbo.id, dbo)
        upsert_response = await repository.get_by_id(PlaceDBO, dbo.id)
        assert upsert_response.name == "updated_name"
        get_response = await repository.get_by_id(PlaceDBO, dbo.id)
        assert get_response.id == dbo.id
        assert get_response.name == "updated_name"
