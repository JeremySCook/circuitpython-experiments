# WIP, needs significant revision

import board
import touchio
import time
import pwmio
import digitalio

touch_pin0 = touchio.TouchIn(board.GP11)
touch_pin1 = touchio.TouchIn(board.GP1)
touch_pin2 = touchio.TouchIn(board.GP2)
touch_pin3 = touchio.TouchIn(board.GP3)
touch_pin4 = touchio.TouchIn(board.GP4)
touch_pin5 = touchio.TouchIn(board.GP5)
touch_pin6 = touchio.TouchIn(board.GP6)
touch_pin7 = touchio.TouchIn(board.GP7)
touch_pin8 = touchio.TouchIn(board.GP8)
touch_pin9 = touchio.TouchIn(board.GP9)
touch_pin10 = touchio.TouchIn(board.GP10)
touch_pin11 = touchio.TouchIn(board.GP11)

touch_pin0.threshold = 1500
touch_pin1.threshold = 1500
touch_pin2.threshold = 1500
touch_pin3.threshold = 1500
touch_pin4.threshold = 1500
touch_pin5.threshold = 1500
touch_pin6.threshold = 1500
touch_pin7.threshold = 1500
touch_pin8.threshold = 1500
touch_pin9.threshold = 1500
touch_pin10.threshold = 1500
touch_pin11.threshold = 1500

led = digitalio.DigitalInOut(board.LED) # defaults to input
led.direction = digitalio.Direction.OUTPUT

speaker = pwmio.PWMOut(board.GP27, frequency=440, duty_cycle=0, variable_frequency = 1) # initializer creates instance of pwmio class

while True:
    if touch_pin0.value:
        speaker.frequency = 65 # C2 ~65.41Hz
    if touch_pin1.value:
        speaker.frequency = 69 # C2# ~69.3Hz
    if touch_pin2.value:
        speaker.frequency = 73 # D ~73.42Hz
    if touch_pin3.value:
        speaker.frequency = 65 # C2 ~65.41Hz
    if touch_pin4.value:
        speaker.frequency = 69 # C2# ~69.3Hz
    if touch_pin5.value:
        speaker.frequency = 73 # D ~73.42Hz
    if touch_pin6.value:
        speaker.frequency = 65 # C2 ~65.41Hz
    if touch_pin7.value:
        speaker.frequency = 69 # C2# ~69.3Hz
    if touch_pin8.value:
        speaker.frequency = 73 # D ~73.42Hz
    if touch_pin9.value:
        speaker.frequency = 65 # C2 ~65.41Hz
    if touch_pin10.value:
        speaker.frequency = 69 # C2# ~69.3Hz
    if touch_pin11.value:
        speaker.frequency = 73 # D ~73.42Hz
      
    time.sleep(.02) # 10ms sleep time
    
    if touch_pin0.value or touch_pin1.value or touch_pin2.value or touch_pin3.value\
    or touch_pin4.value or touch_pin5.value or touch_pin6.value or touch_pin7.value\
    or touch_pin8.value or touch_pin9.value or touch_pin10.value or touch_pin11.value:
        led.value = True
        speaker.duty_cycle = 32768
    else:
        led.value = False
        speaker.duty_cycle = 0
    print("GP0 ", touch_pin0.value, touch_pin0.raw_value, "  GP1 ", touch_pin1.value, "  GP11 ", touch_pin11.value, touch_pin11.raw_value)
