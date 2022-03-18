from kink import di

from src.db.repository import Repository
from src.db.session import get_session
from src.places.place_service import PlaceService


def init_container():
    di["db_session"] = lambda di: get_session()
    di[Repository] = lambda di: Repository(di["db_session"])
    di[PlaceService] = lambda di: PlaceService(di[Repository])
