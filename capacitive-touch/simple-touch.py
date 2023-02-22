import board
import touchio
import time

touch_pin18 = touchio.TouchIn(board.GP18)
touch_pin19 = touchio.TouchIn(board.GP19)

while True:
    print("GP18 ", touch_pin18.value, "  GP19 ", touch_pin19.value)
    time.sleep(.1)
