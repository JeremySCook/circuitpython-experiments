#By Jeremy Cook
#Public Domain

import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = 0

toggle = digitalio.DigitalInOut(board.GP0)
toggle.direction = digitalio.Direction.OUTPUT
toggle.value = 1 #set high initially so does not switch

while True:
    led.value = 1
    time.sleep(5)
    led.value = 0
    time.sleep(5)
    toggle.value = 0 #turns off and does not loop
    time.sleep(10) #delay to allow power down
