from datetime import datetime
from typing import Union

from pydantic import BaseModel
from pydantic import Field
from pydantic import HttpUrl


class Petroleum(BaseModel):
    id: int
    name: str = Field(
        title="The name of the petroleum",
        max_length=20,
        example="Diesel",
        default="",
    )
    short_name: str = Field(
        title="The ISO petroleum short name",
        max_length=5,
        example="ON",
        default="",
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
        default=1.00,
    )
    created_at: Union[datetime, None] = Field(
        title="Creation time",
        example="2021-07-20 16:26:24",
        default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
    updated_at: Union[datetime, None] = Field(
        title="Update time",
        example="2021-07-20 16:26:24",
        default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )


class Image(BaseModel):
    url: HttpUrl = Field("https://default_value.org/")
    name: Union[str, None] = None


class PetrolStation(BaseModel):
    id: int
    name: str
    sold_petroleum: set[str] = set()
    city: Union[str, None] = None
    address: Union[str, None] = None
    image: Union[Image, None] = None
    active: bool
    created_at: Union[datetime, None] = Field(
        title="Creation time",
        example="2021-07-20 16:26:24",
        default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
    updated_at: Union[datetime, None] = Field(
        title="Update time",
        example="2021-07-20 16:26:24",
        default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )


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
    created_at: datetime = Field(
        title="",
        example="",
        default=datetime.now(),
    )
