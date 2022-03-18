from src.places.db.place_dbo import PlaceDBO


def get_default_place_dbo() -> PlaceDBO:
    place = PlaceDBO(name="default")
    return place
