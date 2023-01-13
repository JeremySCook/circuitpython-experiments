import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

btn1_pin = board.GP16

keyboard = Keyboard(usb_hid.devices)

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

while True:
    if not btn1.value:
        print("button 1 pressed")
        keyboard.press(Keycode.B)
        time.sleep(.2)
        keyboard.release(Keycode.B)
