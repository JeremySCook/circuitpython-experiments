import board
import touchio
import time
import digitalio

touch_pinA = touchio.TouchIn(board.PAD1)
touch_pinB = touchio.TouchIn(board.PAD2)

led0_pin = board.LEDA
led0_out = digitalio.DigitalInOut(led0_pin)
led0_out.direction = digitalio.Direction.OUTPUT

led1_pin = board.LEDB
led1_out = digitalio.DigitalInOut(led1_pin)
led1_out.direction = digitalio.Direction.OUTPUT

while True:
    print("GP18 ", touch_pinA.value, " GP19 ", touch_pinB.value)
    time.sleep(.1)
    if touch_pinA.value:
        led1_out.value = 1
    else:
        led1_out.value = 0
        
    if touch_pinB.value:
        led0_out.value = 1
    else:
        led0_out.value = 0
