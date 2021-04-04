# https://github.com/adafruit/Adafruit_CircuitPython_BME280/blob/master/adafruit_bme280.py

import board
import busio
import adafruit_bme280

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x77)
#or with other sensor address
#bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

# OR create library object using our Bus SPI port
#spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
#bme_cs = digitalio.DigitalInOut(board.D10)
#bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25


def get_values():
    #print("\nTemperature: %0.1f C" % bme280.temperature)
    #print("Humidity: %0.1f %%" % bme280.relative_humidity)
    #print("Pressure: %0.1f hPa" % bme280.pressure)
    #print("Altitude = %0.2f meters" % bme280.altitude)

    return [
        ['temp', bme280.temperature],
        ['relative_humidity', bme280.relative_humidity],
        ['pressure', bme280.pressure],
        ['altitude', bme280.altitude]
    ]

