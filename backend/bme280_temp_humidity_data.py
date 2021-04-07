# https://github.com/adafruit/Adafruit_CircuitPython_BME280/blob/master/adafruit_bme280.py

import time
import board
import busio
import adafruit_bme280


# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x77)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25


def get_values():
    time.sleep(0.5)
    try:
        return [
            ['temp', bme280.temperature],
            ['relative_humidity', bme280.relative_humidity],
            ['pressure', bme280.pressure],
            ['altitude', bme280.altitude]
        ]
    except OSError:
        bme280._reset()

        return [
            ['temp', bme280.temperature],
            ['relative_humidity', bme280.relative_humidity],
            ['pressure', bme280.pressure],
            ['altitude', bme280.altitude]
        ]

