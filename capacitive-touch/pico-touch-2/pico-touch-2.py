# Write your code here :-)
import board
import touchio
import time
import digitalio

touch_pin0 = touchio.TouchIn(board.GP0)
touch_pin1 = touchio.TouchIn(board.GP1)
touch_pin2 = touchio.TouchIn(board.GP2)

led = digitalio.DigitalInOut(board.LED) # defaults to input
led.direction = digitalio.Direction.OUTPUT

while True:
    if touch_pin0.value or touch_pin1.value or touch_pin2.value:
        led.value = True
    else:
        led.value = False
    print("GP0 ", touch_pin0.value, "  GP1 ", touch_pin1.value, "  GP2 ", touch_pin2.value)
    time.sleep(.01)
