from kink import di

from items.item_service import ItemService
from src.db.repository import Repository
from src.db.session import get_session
from src.places.place_service import PlaceService
from users.security_service import SecurityService
from users.user_service import UserService


def init_container():
    di["session_maker"] = lambda di: get_session
    di[Repository] = lambda di: Repository()
    di[PlaceService] = lambda di: PlaceService(di[Repository])
    di[UserService] = lambda di: UserService(di[Repository])
    di[SecurityService] = lambda di: SecurityService(di[UserService])
    di[ItemService] = lambda di: ItemService(di[Repository])
