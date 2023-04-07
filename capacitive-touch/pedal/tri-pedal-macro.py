# Based on code by todbot: https://github.com/todbot/picotouch/blob/main/circuitpython/picotouch/code.py
# Modified for 3-pad "RP20FOOTIE" by @jeremyscook 4/7/2023

# To use:
#
# 1. Install needed libraries:
#   circup install adafruit_hid adafruit_debouncer adafruit_ticks
#
# 2. Copy over this file as code.py:
#   cp picotouch/code.py /Volumes/CIRCUITPY/code.py
#
# To change keys, edit 'keymap' as desired
#
# List of keycodes: https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/main/adafruit_hid/keycode.py
#
# on Pico / RP2040, need 1M pull-down on each input  (picotouch board has this)
#

import time
import board
import touchio
import digitalio

from adafruit_debouncer import Debouncer, Button

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

debug = True

# put your keymap here
keymap = (
    # description  # list of keycodes or string to print out
    ("Capital A",  (Keycode.SHIFT, Keycode.A) ),   # key  0
    ("Hello world", "Hello world"),  # key  1
    (None, None),
)

touch_threshold_adjust = 300

touch_pins = (
    board.GP13, board.GP14, board.GP15
)

kbd = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(kbd)

led = digitalio.DigitalInOut(board.LED) # defaults to input
led.direction = digitalio.Direction.OUTPUT

touch_ins = []  # for debug
touch_pads = []
for pin in touch_pins:
    touchin = touchio.TouchIn(pin)
    touchin.threshold += touch_threshold_adjust
    touch_pads.append( Button(touchin, value_when_pressed=True))
    touch_ins.append(touchin)  # for debug
num_touch_pads = len(touch_pads)

print("\n----------")
print("picotouch_macropad hello")

while True:
    for i in range(num_touch_pads):
        touch = touch_pads[i]
        touch.update()
        key_desc, key_sequence = keymap[i]
        if touch.rose:
            led.value = True
            if debug: print('key press   %2d' % i, "touchdata:",touch_ins[i].raw_value, touch_ins[i].threshold)
            if key_desc and key_sequence:  # only if keymap entry exists for this key
                print("key_desc:",key_desc,"sequence:",key_sequence)
                if not isinstance(key_sequence,str):
                    kbd.press(*key_sequence)
                else:
                    keyboard_layout.write(key_sequence)

        if touch.fell:
            led.value = False
            if debug: print("key release %2d" % i, "touchdata:",touch_ins[i].raw_value, touch_ins[i].threshold)
            if key_desc and key_sequence:  # only if keymap entry exists for this key
                if not isinstance(key_sequence,str):
                    kbd.release(*key_sequence)
