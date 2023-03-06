import board
import touchio
import time

touch_pin0 = touchio.TouchIn(board.GP0)
touch_pin1 = touchio.TouchIn(board.GP1)
touch_pin2 = touchio.TouchIn(board.GP2)

while True:
    print("GP0 ", touch_pin0.value, "  GP1 ", touch_pin1.value, "  GP2 ", touch_pin2.value)
    time.sleep(.01)
