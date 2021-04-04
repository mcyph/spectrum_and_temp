# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import busio
import adafruit_ccs811

i2c = busio.I2C(board.SCL, board.SDA)
ccs811 = adafruit_ccs811.CCS811(i2c, 0x5B)


def get_values():
    # Wait for the sensor to be ready
    while not ccs811.data_ready:
        time.sleep(0.01)

    #while True:
    #print("CO2: {} PPM, TVOC: {} PPB".format(ccs811.eco2, ccs811.tvoc))
    #time.sleep(0.5)
    return [
        ['eco2', ccs811.eco2],
        ['tvoc', ccs811.tvoc]
    ]
