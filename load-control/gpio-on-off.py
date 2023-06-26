import time
import board
import digitalio
import time

step_delay = 1

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

output_right = digitalio.DigitalInOut(board.GP16)
output_right.direction = digitalio.Direction.OUTPUT

# output_left = digitalio.DigitalInOut(board.GP15)
# output_left.direction = digitalio.Direction.OUTPUT

while True:
    output_right.value = 1
    # output_left.value = 1
    led.value = 1
    time.sleep(step_delay)
    
    output_right.value = 0
    # output_left.value = 0
    led.value = 0
    time.sleep(step_delay + 2)
