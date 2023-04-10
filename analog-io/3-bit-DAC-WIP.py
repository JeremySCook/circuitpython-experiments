# Not yet working

import board
import digitalio
import time

step_delay = .1

DAC_pin = (
    board.GP20, board.GP19, board.GP18
)

for DAC in DAC_pin:
    DAC_pin(DAC).direction = digitalio.Direction.OUTPUT

while True:
    DAC_pin(0).value = 0
    DAC_pin(1).value = 0
    DAC_pin(2).value = 0
    

    print("binary 0")
    time.sleep(step_delay)
