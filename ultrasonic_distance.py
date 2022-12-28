# Modified from code found here: https://learn.adafruit.com/ultrasonic-sonar-distance-sensors/python-circuitpython
# For usage on RPi Pico @JeremySCook 12/28/2022
# Works with VBUS or VSYS ~5VDC on Raspberry Pi Pico

import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP17, echo_pin=board.GP16)

while True:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
