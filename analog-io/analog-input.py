# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT
# Adapted by @jeremyscook April 2023
# Modified from: https://learn.adafruit.com/circuitpython-essentials/circuitpython-analog-in
# More plotting info: https://learn.adafruit.com/make-it-graph-plot/circuitpython-and-mu

"""CircuitPython Essentials Analog In example"""
import time
import board
from analogio import AnalogIn

analog_in = AnalogIn(board.A0)


def get_voltage(pin):
    return (pin.value * 3.3) / 65536


while True:
    print((get_voltage(analog_in),))
    time.sleep(0.1)
