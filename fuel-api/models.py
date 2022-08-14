from typing import List
from typing import Union

from pydantic import BaseModel


class Petroleum(BaseModel):
    id: int
    name: str
    short_name: int
    description: Union[str, None] = None
    tax: Union[float, None] = None


class PetrolStation(BaseModel):
    id: int
    name: str
    sold_petroleum: List
    City: Union[str, None] = None
    Address: Union[str, None] = None
    Active: bool
