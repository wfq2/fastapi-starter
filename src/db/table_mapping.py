from typing import Dict, Any

from src.places.db.place import Place
from src.places.db.place_dbo import PlaceDBO

TableMapping: Dict[str, Any] = {PlaceDBO.__name__: Place}
