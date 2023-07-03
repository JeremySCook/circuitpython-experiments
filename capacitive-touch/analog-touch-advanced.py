import board
import touchio
import time

cap_steps = 5

touch_pinA = touchio.TouchIn(board.GP14)
touch_pinAmin = 1100
touch_pinAmax = 2300
touch_pinA_steps = ((touch_pinAmax - touch_pinAmin)/cap_steps)

touch_pinB = touchio.TouchIn(board.GP15)
touch_pinB.threshold = 3000
touch_pinBmin = 1250
touch_pinBmax = 2500
touch_pinB_steps = ((touch_pinBmax - touch_pinBmin)/cap_steps)

def total_touch(touch_pin):
    total_value = 0
    for i in range(10):
        total_value += touch_pin.raw_value
    total_value = total_value/10
    return total_value

def pin_steps(average_value, touch_pinmin, touch_pinsteps):
    step_value = int((average_value - touch_pinmin)/touch_pinsteps)
    return step_value

while True:
    
    #print((total_touch(touch_pinA),total_touch(touch_pinB)))
    print(pin_steps(total_touch(touch_pinA), touch_pinAmin, touch_pinA_steps)\
    ,pin_steps(total_touch(touch_pinB), touch_pinBmin, touch_pinB_steps))
