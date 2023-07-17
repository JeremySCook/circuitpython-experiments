import board
import touchio
import time

touch_pinA = touchio.TouchIn(board.GP14)
touch_pinB = touchio.TouchIn(board.GP15)

while True:
    print((touch_pinA.raw_value, touch_pinB.raw_value, \
    (touch_pinA.raw_value - touch_pinB.raw_value)))
    time.sleep(.1)
