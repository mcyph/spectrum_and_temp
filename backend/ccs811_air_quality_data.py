# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import busio
import adafruit_ccs811

i2c = busio.I2C(board.SCL, board.SDA)
ccs811 = adafruit_ccs811.CCS811(i2c, 0x5B)


def get_values():
    time.sleep(0.5)
    try:
        # Wait for the sensor to be ready
        while not ccs811.data_ready:
            time.sleep(0.01)

        return [
            ['eco2', ccs811.eco2],
            ['tvoc', ccs811.tvoc]
        ]
    except OSError:
        # Try to reset+try again if there are problems reading
        ccs811.reset()

        # Wait for the sensor to be ready
        while not ccs811.data_ready:
            time.sleep(0.01)

        return [
            ['eco2', ccs811.eco2],
            ['tvoc', ccs811.tvoc]
        ]
