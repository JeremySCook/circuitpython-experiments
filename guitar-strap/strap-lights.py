# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Analog In example"""
import time
import board
from analogio import AnalogIn
# from rainbowio import colorwheel
import neopixel
# import math
import simpleio

pixel_pin = board.GP0
num_pixels = 12

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

analog_in = AnalogIn(board.A0)
samples_number = 50
analog_min = 2
analog_max = 3.3

def get_voltage(pin):
    totalAnalog = 0
    for i in range(samples_number):
        if (pin.value * 3.3/65536) > totalAnalog:
            totalAnalog = pin.value * 3.3/65536
        time.sleep(.001)
    return totalAnalog

def color_sound(color, wait, LED_value):
    for i in range(num_pixels):
        if i < 20: #for some reason not showing LEDs, serial monitor indicates show, works with different code
            pixels[i] = color
            pixels.show
            time.sleep(0.01)
            print("show")
        else:
            pixels[i] = BLANK
            pixels.show
            time.sleep(0.01)
            print("no-show")

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
BLANK = (0, 0, 0)

while True:
    magnitude = get_voltage(analog_in)
    # print(magnitude)
    mapped_value = simpleio.map_range(magnitude, analog_min, analog_max, 0, 11)
    int_mapped_value = int(mapped_value)
    print(int_mapped_value)
    color_sound(RED, .001, int_mapped_value)
    time.sleep(0.1)
