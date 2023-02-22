# PWM example for RPi Pico
# Used for motor - works w/ 12V input at different speeds
# Simply cuts off at 5V when not at max PWM, though decelerates more slowly than if entirely cut off

import time
import pwmio
import board
import digitalio

led = pwmio.PWMOut(board.GP16, frequency=5000, duty_cycle=0)

while True:
    led.duty_cycle = (2 ** 16 -1) # 65535 - full scope of PWM
    time.sleep(5)
    led.duty_cycle = (2 ** 15 -1) # 32767
    time.sleep(5)
    led.duty_cycle = 0
    time.sleep(5)
  
