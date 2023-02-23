# Binary control example for RPi Pico
# Using L293D motor driver

import time
import board
import digitalio

enable = digitalio.DigitalInOut(board.GP18)
enable.direction = digitalio.Direction.OUTPUT
enable.value = 0

rotate1A = digitalio.DigitalInOut(board.GP17)
rotate1A.direction = digitalio.Direction.OUTPUT
rotate1A.value = 0

rotate2A = digitalio.DigitalInOut(board.GP16)
rotate2A.direction = digitalio.Direction.OUTPUT
rotate2A.value = 0

while True:
    enable.value = 1
    rotate1A.value = 1
    rotate2A.value = 0
    time.sleep(1)
    
    rotate1A.value = 0
    rotate2A.value = 0
    time.sleep(1)
    
    rotate1A.value = 0
    rotate2A.value = 1
    time.sleep(1)
    
    rotate1A.value = 0
    rotate2A.value = 0
    time.sleep(1)
