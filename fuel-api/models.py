from typing import Union

from pydantic import BaseModel
from pydantic import HttpUrl


class Petroleum(BaseModel):
    id: int
    name: str
    short_name: str
    description: Union[str, None] = None
    tax: Union[float, None] = None


class Image(BaseModel):
    url: HttpUrl
    name: str


class PetrolStation(BaseModel):
    id: int
    name: str
    sold_petroleum: set[str] = set()
    City: Union[str, None] = None
    Address: Union[str, None] = None
    image: Union[Image, None] = None
    Active: bool
