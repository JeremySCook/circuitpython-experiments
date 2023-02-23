# PWM control example for RPi Pico
# Using L293D motor driver
# Pico tried ~ 4:00 on Feb 23rd had issue

import time
import pwmio
import board
import digitalio

enable = digitalio.DigitalInOut(board.GP18)
enable.direction = digitalio.Direction.OUTPUT
enable.value = 0

rotate1A = pwmio.PWMOut(board.GP17, frequency=5000, duty_cycle=0)
rotate2A = pwmio.PWMOut(board.GP16, frequency=5000, duty_cycle=0)

while True:
    enable.value = 1
    
    for x in range(35000, 65535, 600):
        rotate1A.duty_cycle = x
        rotate2A.duty_cycle = 0
        print("1A.duty_cycle ", rotate1A.duty_cycle)
        time.sleep(.1)
    
    rotate1A.duty_cycle = 65535 # top speed
    print("1A.duty_cycle ", rotate1A.duty_cycle)
    time.sleep(1)
    
    for x in range(35000, 65535, 600):
        rotate1A.duty_cycle = 0
        rotate2A.duty_cycle = x
        print("2A.duty_cycle ", rotate2A.duty_cycle)
        time.sleep(.1)

    rotate2A.duty_cycle = 65535 # top speed
    print("2A.duty_cycle ", rotate2A.duty_cycle)
    time.sleep(1)
