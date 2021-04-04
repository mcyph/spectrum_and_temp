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
    [410, 'violet1', 'violet'],
    [435, 'violet2', 'violet'],
    [460, 'blue1', 'blue'],
    [485, 'blue2', 'blue'],
    [510, 'green1', 'green'],
    [535, 'green2', 'green'],
    [560, 'green3', 'green'],
    [585, 'yellow', 'yellow'],
    [610, 'orange', 'orange'],
    [645, 'red1', 'red'],
    [680, 'red2', 'red'],
    [705, 'red3', 'red'],
    [730, 'red4', 'red'],
    [760, 'ir1', 'ir'],
    [810, 'ir2', 'ir'],
    [860, 'ir3', 'ir'],
    [900, 'ir4', 'ir'],
    [940, 'ir5', 'ir'],
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
spectrometer.setIntegrationTime(255)
spectrometer.setGain(3)
