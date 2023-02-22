import board
import touchio
import time

touch_pin18 = touchio.TouchIn(board.GP18)
touch_pin18.threshold = 3000 # 3000 is inconsistent with the smaller wire
touch_pin19 = touchio.TouchIn(board.GP19)
touch_pin19.threshold = 3000

while True:
    print((touch_pin18.raw_value,touch_pin19.raw_value))
    print ("GP18 ", touch_pin18.value,"  GP19 ", touch_pin19.value)
    time.sleep(.1)
