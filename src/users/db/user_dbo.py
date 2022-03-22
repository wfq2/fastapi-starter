from db.base_dbo import BaseDBO


class UserDBO(BaseDBO):
    first_name: str
    last_name: str
    email: str
    hashed_password: str
    disabled: bool = False
