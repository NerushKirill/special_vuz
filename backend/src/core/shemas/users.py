from pydantic import BaseModel
from datetime import date


class User(BaseModel):
    first_name: str
    last_name: str
    age: int
    birthday: date
    photo: str
