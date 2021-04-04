# https://github.com/LiamsGitHub/AS7265x-spectrometer/blob/master/spectrometer.py

# Script to test spectrometer.py
import spectrometer


"""
#spectrometer members:
def init()
def boardPresent()
def hwVersion()
def swVersion()
def temperatures()
def setBlueLED(state)
def shutterLED(device,state)
def setLEDDriveCurrent(current)
def setIntegrationTime(time)
def setGain(gain)
def readRAW()
def readCAL()
"""


VALUE_TYPES = [
    [410, 'violet1'],
    [435, 'violet2'],
    [460, 'blue1'],
    [485, 'blue2'],
    [510, 'green1'],
    [535, 'green2'],
    [560, 'green3'],
    [585, 'yellow'],
    [610, 'orange'],
    [645, 'red1'],
    [680, 'red2'],
    [705, 'red3'],
    [730, 'red4'],
    [760, 'ir1'],
    [810, 'ir2'],
    [860, 'ir3'],
    [900, 'ir4'],
    [940, 'ir5'],
]


def get_raw_values():
    raw_values = spectrometer.readRAW()
    return [VALUE_TYPES[x]+[value]
            for x, value
            in enumerate(raw_values)]


def get_calibrated_values():
    calibrated_values = spectrometer.readCAL()
    return [VALUE_TYPES[x]+[value]
            for x, value
            in enumerate(calibrated_values)]


spectrometer.init()
spectrometer.hwVersion()
print(get_raw_values())
print(get_calibrated_values())

