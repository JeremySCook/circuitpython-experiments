# Turns on onboard LED at different intensities. Can experiement with frequency

import board
import pwmio
import time

led = pwmio.PWMOut(board.LED, variable_frequency=True)
led.frequency = 30

while True:
    led.duty_cycle = 65535
    time.sleep(1)
    led.duty_cycle = int(50 / 100 * 65535)  # Expressed as percentage (50%)
    time.sleep(1)
    led.duty_cycle = 0
    time.sleep(1)
