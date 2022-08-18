petrol_db = [
    {"id": 1, "name": "Diesel", "short_name": "ON", "description": "", "tax": 1.1},
    {"id": 2, "name": "Gasoline", "short_name": "PB95", "description": ""},
    {"id": 3, "short_name": "LPG", "description": "", "tax": 1.3},
]

petrol_station_db = [
    {
        "id": 1,
        "name": "Auchan",
        "sold_petroleum": [],
        "city": "",
        "street": "",
        "active": False,
    },
    {
        "id": 2,
        "name": "BP",
        "sold_petroleum": [],
        "city": "",
        "street": "",
        "active": False,
    },
]


petrol_price_db = [
    {
        "id": 1,
        "petroleum_id": 1,
        "petrol_station_id": 1,
        "price": 1.01,
    },
    {
        "id": 2,
        "petroleum_id": 1,
        "petrol_station_id": 2,
        "price": 1.02,
    },
    {
        "id": 3,
        "petroleum_id": 2,
        "petrol_station_id": 1,
        "price": 2.01,
    },
    {
        "id": 4,
        "petroleum_id": 2,
        "petrol_station_id": 2,
        "price": 2.02,
    },
    {
        "id": 5,
        "petroleum_id": 3,
        "petrol_station_id": 1,
        "price": 3.01,
    },
    {
        "id": 6,
        "petroleum_id": 3,
        "petrol_station_id": 2,
        "price": 3.02,
    },
]
