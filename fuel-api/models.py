from datetime import datetime
from typing import Union
from uuid import UUID

from pydantic import BaseModel
from pydantic import Field
from pydantic import HttpUrl


class Petroleum(BaseModel):
    id: UUID
    name: str = Field(
        title="The name of the petroleum",
        max_length=20,
        example="Diesel",
    )
    short_name: str = Field(
        title="The ISO petroleum short name",
        max_length=5,
        example="ON",
    )
    description: Union[str, None] = Field(
        default=None,
        title="The description of the petroleum",
        max_length=300,
        example="Diesel Petroleum",
    )
    tax: float = Field(
        title="The percent amount of tax applied to petroleum",
        gt=0,
        example=8,
    )


class Image(BaseModel):
    url: HttpUrl
    name: Union[str, None] = None


class PetrolStation(BaseModel):
    id: int
    name: str
    sold_petroleum: set[str] = set()
    city: Union[str, None] = None
    address: Union[str, None] = None
    image: Union[Image, None] = None
    active: bool


class PetrolPrice(BaseModel):
    id: int = Field(
        title="ID of petrol price record",
        gt=0,
        example=1,
    )
    petroleum_id: int = Field(
        title="ID of petroleum",
        gt=0,
        example=1,
    )
    petrol_station_id: int = Field(
        title="ID of petrol station",
        gt=0,
        example=1,
    )
    price: float = Field(
        title="petrol price at the measurement",
        gt=0,
        example=1,
    )
    created_at: datetime
