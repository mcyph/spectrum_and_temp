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


spectrometer.init()
#print(spectrometer.hwVersion())
spectrometer.setIntegrationTime(254)
spectrometer.setGain(3)
spectrometer.setBlueLED(False)


VALUE_TYPES = [
    [410, 'violet1', 'darkviolet'],
    [435, 'violet2', 'violet'],
    [460, 'blue1', 'darkblue'],
    [485, 'blue2', 'blue'],
    [510, 'cyan', 'cyan'],
    [535, 'green1', 'lightgreen'],
    [560, 'green2', 'darkgreen'],
    [585, 'yellow', 'yellow'],
    [610, 'orange', 'orange'],
    [645, 'red1', 'orangered'],
    [680, 'red2', 'red'],
    [705, 'red3', 'firebrick'],
    [730, 'red4', 'darkred'],
    [760, 'ir1', 'maroon'],
    [810, 'ir2', 'maroon'],
    [860, 'ir3', 'maroon'],
    [900, 'ir4', 'maroon'],
    [940, 'ir5', 'maroon'],
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
