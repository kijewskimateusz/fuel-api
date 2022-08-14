from db import petrol_db
from db import petrol_station_db
from fastapi import FastAPI
from models import Petroleum
from models import PetrolStation

app = FastAPI()


@app.get("/fuels/")
async def read_fuels(skip: int = 0, limit: int = 10):
    return petrol_db[skip : skip + limit]


@app.post("/fuels/")
async def create_fuel(petroleum: Petroleum):
    petrol_db.append(petroleum)
    return petroleum.name.upper()


@app.get("/petrol_stations/")
async def read_petrol_stations(skip: int = 0, limit: int = 10):
    return petrol_station_db[skip : skip + limit]


@app.post("/petrol_stations/")
async def create_petrol_station(petrol_station: PetrolStation):
    petrol_station_db.append(petrol_station)
    return petrol_station
