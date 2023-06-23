import board
import digitalio
import time

step_delay = .1

output_right = digitalio.DigitalInOut(board.GP16)
output_right.direction = digitalio.Direction.OUTPUT

output_left = digitalio.DigitalInOut(board.GP15)
output_left.direction = digitalio.Direction.OUTPUT

while True:
    output_left.value = 1
    time.sleep(1)
    output_left.value = 0
    time.sleep(3)
