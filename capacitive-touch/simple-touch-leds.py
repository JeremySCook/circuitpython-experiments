import board
import touchio
import time
import digitalio

touch_pin18 = touchio.TouchIn(board.GP18)
touch_pin19 = touchio.TouchIn(board.GP19)

led0_pin = board.LED
led0_out = digitalio.DigitalInOut(led0_pin)
led0_out.direction = digitalio.Direction.OUTPUT

led1_pin = board.GP16
led1_out = digitalio.DigitalInOut(led1_pin)
led1_out.direction = digitalio.Direction.OUTPUT

while True:
    print("GP18 ", touch_pin18.value, " GP19 ", touch_pin19.value)
    time.sleep(.1)
    if touch_pin18.value:
        led1_out.value = 1
    else:
        led1_out.value = 0
        
    if touch_pin19.value:
        led0_out.value = 1
    else:
        led0_out.value = 0
