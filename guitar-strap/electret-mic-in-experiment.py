# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Analog In example"""
import time
import board
from analogio import AnalogIn

analog_in = AnalogIn(board.A0)
samples_number = 10

def get_voltage(pin):
    totalAnalog = 0
    for i in range(samples_number):
        if (pin.value * 3.3/65536) > totalAnalog:
            totalAnalog = pin.value * 3.3/65536
        time.sleep(.01)
    return totalAnalog


while True:
    print((get_voltage(analog_in),))
    time.sleep(0.1)
