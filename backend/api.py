from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import as7265x_spectral_data
import bme280_temp_humidity_data
import ccs811_air_quality_data


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {
        "spectral_raw": as7265x_spectral_data.get_raw_values(),
        "spectral_calibrated": as7265x_spectral_data.get_calibrated_values(),
        "temp_humidity": bme280_temp_humidity_data.get_values(),
        "air_quality": ccs811_air_quality_data.get_values()
    }


