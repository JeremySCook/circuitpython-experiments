import board
import touchio
import time
import digitalio

touch_pin0 = touchio.TouchIn(board.GP13)
touch_pin1 = touchio.TouchIn(board.GP14)
touch_pin2 = touchio.TouchIn(board.GP15)

led = digitalio.DigitalInOut(board.LED) # defaults to input
led.direction = digitalio.Direction.OUTPUT

opto_isolator = digitalio.DigitalInOut(board.GP27)
opto_isolator.direction = digitalio.Direction.OUTPUT

while True:
    if touch_pin0.value or touch_pin1.value or touch_pin2.value:
        led.value = True
        opto_isolator.value = True
    else:
        led.value = False
        opto_isolator.value = False
    print("GP0 ", touch_pin0.value, "  GP1 ", touch_pin1.value, "  GP2 ", touch_pin2.value)
    time.sleep(.01)
