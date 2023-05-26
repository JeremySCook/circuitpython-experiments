import time
import pwmio
import board

speaker = pwmio.PWMOut(board.GP26, frequency=440, duty_cycle=32768, variable_frequency = 1) 
# initializer creates instance of pwmio class
# modify speaker.duty_cycle to change perceived volume
# duty cycle full PWM range is 0 to 65535. 65535 which would mean on all the time
# and not really oscillating

while True:
    speaker.frequency = 440
    time.sleep(1)
    speaker.frequency = 800
    time.sleep(1)
