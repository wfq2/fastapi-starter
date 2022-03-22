from typing import Dict, Any

from src.places.db.place import Place
from src.places.db.place_dbo import PlaceDBO
from users.db.user import User
from users.db.user_dbo import UserDBO

TableMapping: Dict[str, Any] = {PlaceDBO.__name__: Place, UserDBO.__name__: User}
