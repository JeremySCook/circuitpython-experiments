import time
import pwmio
import board

ezfan = pwmio.PWMOut(board.GP15, frequency=440, duty_cycle=0, variable_frequency=0)

while True:
    ezfan.duty_cycle = 65535
    print(ezfan.duty_cycle)
    time.sleep(1)
    ezfan.duty_cycle = int(65535/3)
    print(ezfan.duty_cycle)
    time.sleep(1)
