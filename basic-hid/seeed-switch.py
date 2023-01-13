import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

btn1_pin = board.D6
btn2_pin = board.D5
switch1_input = board.D4  # Yellow wire
switch1_LED = board.D3  # Black wire

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.UP

switch1 = digitalio.DigitalInOut(switch1_input)
switch1.direction = digitalio.Direction.INPUT
switch1.pull = digitalio.Pull.DOWN

LED = digitalio.DigitalInOut(switch1_LED)
LED.direction = digitalio.Direction.OUTPUT
LED.value = 1

while True:
    if not btn1.value:
        print("button 1 pressed")
        keyboard.press(Keycode.LEFT_SHIFT, Keycode.M)
        time.sleep(0.2)
        keyboard.release(Keycode.LEFT_SHIFT, Keycode.M)
    if not btn2.value:
        print("button 2 pressed")
        keyboard.press(Keycode.M)
        time.sleep(0.2)
        keyboard.release(Keycode.M)
    if switch1.value:
        print("switch is on")
        layout.write('hello there\n')
        LED.value = 0
        time.sleep(0.1)
        LED.value = 1
        time.sleep(.4)
        keyboard.release(Keycode.S)
