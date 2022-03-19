from kink import di

from src.db.repository import Repository
from src.db.session import get_session
from src.places.place_service import PlaceService


def init_container():
    di["session_maker"] = lambda di: get_session
    di[Repository] = lambda di: Repository()
    di[PlaceService] = lambda di: PlaceService(di[Repository])
