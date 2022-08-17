from db import petrol_db
from db import petrol_price_db
from db import petrol_station_db
from fastapi import FastAPI
from fastapi import Path
from fastapi import Query
from models import Petroleum
from models import PetrolStation

app = FastAPI()


@app.get("/fuels/")
async def read_fuels(
    skip: int = Query(default=0, gt=0, lt=5),
    limit: int = Query(default=10, gt=0, lt=1000),
):
    return petrol_db[skip : skip + limit]


@app.get("/fuels/{fuel_id}")
async def read_fuel(
    fuel_id: int = Path(title="The ID of the petroleum to get", ge=1),
):
    item_dic = [dic for dic in petrol_db if dic["id"] == fuel_id]
    if item_dic:
        return item_dic[0]
    else:
        return f"No entry of petrol in database for id {fuel_id}"


@app.post("/fuels/")
async def create_fuel(petroleum: Petroleum):
    petrol_db.append(petroleum)
    return petroleum


@app.get("/petrol_stations/")
async def read_petrol_stations(
    skip: int = Query(default=0, gt=0, lt=5),
    limit: int = Query(default=10, gt=0, lt=1000),
):
    return petrol_station_db[skip : skip + limit]


@app.get("/petrol_stations/{petrol_station_id}")
async def read_petrol_station(
    petrol_station_id: int = Path(title="The ID of the petroleum to get", ge=1)
):
    item_dic = [dic for dic in petrol_station_db if dic["id"] == petrol_station_id]
    if item_dic:
        return item_dic[0]
    else:
        return f"No entry of petrol station in database for id {petrol_station_id}"


@app.post("/petrol_stations/")
async def create_petrol_station(petrol_station: PetrolStation):
    petrol_station_db.append(petrol_station)
    return petrol_station


@app.get("/prices/")
async def read_petrol_price(
    skip: int = Query(default=0, gt=0, lt=5),
    limit: int = Query(default=10, gt=0, lt=1000),
):
    return petrol_price_db[skip : skip + limit]
