from datetime import datetime

from db import petrol_db
from db import petrol_price_db
from db import petrol_station_db
from fastapi import FastAPI
from fastapi import Path
from fastapi import Query
from models import Petroleum
from models import PetrolPrice
from models import PetrolStation

app = FastAPI()


@app.get(
    "/fuels/", response_model=list[Petroleum], response_model_exclude={"description"}
)
async def read_fuels(
    skip: int = Query(default=0, gt=0, lt=5),
    limit: int = Query(default=10, gt=0, lt=1000),
):
    return petrol_db[skip : skip + limit]


@app.get(
    "/fuels/{fuel_id}", response_model=Petroleum, response_model_exclude_unset=False
)
async def read_fuel(
    fuel_id: int = Path(title="The ID of the petroleum to get", ge=1),
):
    item_dic = [dic for dic in petrol_db if dic["id"] == fuel_id]
    if item_dic:
        return item_dic[0]
    else:
        return Petroleum(id=-1, description=f"No fuel with that ID {fuel_id}")


@app.post("/fuels/", response_model=Petroleum)
async def create_fuel(petroleum: Petroleum):
    petrol_db.append(petroleum)
    return petroleum


@app.post("/fuels/custom_date", response_model=Petroleum)
async def create_fuel_with_date(
    petroleum: Petroleum,
    created_at: datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    updated_at: datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
):
    petroleum.updated_at = updated_at
    petroleum.created_at = created_at
    petrol_db.append(petroleum)
    return petroleum


@app.get("/petrol_stations/", response_model=list[PetrolStation])
async def read_petrol_stations(
    skip: int = Query(default=0, gt=0, lt=5),
    limit: int = Query(default=10, gt=0, lt=1000),
):
    return petrol_station_db[skip : skip + limit]


@app.get("/petrol_stations/{petrol_station_id}", response_model=PetrolStation)
async def read_petrol_station(
    petrol_station_id: int = Path(title="The ID of the petroleum to get", ge=1)
):
    item_dic = [dic for dic in petrol_station_db if dic["id"] == petrol_station_id]
    if item_dic:
        return item_dic[0]
    else:
        return PetrolStation(
            id=-1,
            name=f"No petrol station with that ID {petrol_station_id}",
            active=False,
        )


@app.post("/petrol_stations/", response_model=PetrolStation)
async def create_petrol_station(petrol_station: PetrolStation):
    petrol_station_db.append(petrol_station)
    return petrol_station


@app.get(
    "/prices/", response_model=list[PetrolPrice], response_model_exclude={"created_at"}
)
async def read_petrol_price(
    skip: int = Query(default=0, gt=0, lt=5),
    limit: int = Query(default=10, gt=0, lt=1000),
):
    return petrol_price_db[skip : skip + limit]
