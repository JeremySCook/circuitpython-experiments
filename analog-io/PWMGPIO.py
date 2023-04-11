# Potentially add capacitor to even out

import board
import pwmio
import time

analog_out = pwmio.PWMOut(board.GP22, variable_frequency=True)
analog_out.frequency = 500

while True:
    analog_out.duty_cycle = 65535
    print(analog_out.duty_cycle)
    time.sleep(.5)
    analog_out.duty_cycle = int(50 / 100 * 65535)  # Expressed as percentage (50%)
    print(analog_out.duty_cycle)
    time.sleep(.5)
    analog_out.duty_cycle = 0
    print(analog_out.duty_cycle)
    time.sleep(.5)
