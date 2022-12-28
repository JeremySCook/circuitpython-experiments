"""
Modified from code found here: 
https://learn.adafruit.com/ultrasonic-sonar-distance-sensors/python-circuitpython
For usage on RPi Pico @JeremySCook 12/28/2022

Builtin LED goes high when distance is under 10 cm
Works with VBUS or VSYS ~5VDC on Raspberry Pi Pico
"""

import time
import board
import adafruit_hcsr04
import digitalio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP17, echo_pin=board.GP16)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    try:
        print((sonar.distance,))
        if sonar.distance < 10:
            led.value = 1
        else:
            led.value = 0
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
