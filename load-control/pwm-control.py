import time
import pwmio
import board

speaker = pwmio.PWMOut(board.GP15, frequency=440, duty_cycle=32768, variable_frequency = 0) 
# initializer creates instance of pwmio class
# modify speaker.duty_cycle to change perceived volume
# duty cycle full PWM range is 0 to 65535. 65535 which would mean on all the time
# and not really oscillating

while True:
    speaker.duty_cycle = 65535
    print(speaker.duty_cycle)
    time.sleep(1)
    speaker.duty_cycle = int(65535/3)
    print(speaker.duty_cycle)
    time.sleep(1)
