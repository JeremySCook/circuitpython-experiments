# PWM example for RPi Pico
# cycles from fully on 65535 to 4095 - builtin LED
# still shines even though a fraction of full value

import time
import pwmio
import board
import digitalio

led = pwmio.PWMOut(board.LED, frequency=60, duty_cycle=0)

while True:
    led.duty_cycle = (2 ** 16 -1) #65535 - full scope of PWM
    time.sleep(1)
    led.duty_cycle = (2 ** 14 -1)
    time.sleep(1)
    led.duty_cycle = (2 ** 12 -1)
    time.sleep(1)
