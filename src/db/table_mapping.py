from typing import Dict, Any

from dates.models.availability import Availability
from items.db.item_dbo import ItemDBO
from items.db.time_based_price_dbo import TimeBasedPriceDBO
from items.db.item import Item
from items.db.time_based_price import TimeBasedPrice
from src.places.db.place import Place
from src.places.db.place_dbo import PlaceDBO
from users.db.user import User
from users.db.user_dbo import UserDBO
from dates.db.availability_dbo import AvailabilityDBO

TableMapping: Dict[str, Any] = {
    PlaceDBO.__name__: Place,
    UserDBO.__name__: User,
    AvailabilityDBO.__name__: Availability,
    ItemDBO.__name__: Item,
    TimeBasedPriceDBO.__name__: TimeBasedPrice,
}
