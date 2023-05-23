# Write your code here :-)
import board
import touchio
import time
import pwmio
import digitalio

touch_pin0 = touchio.TouchIn(board.GP0)
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
touch_pin12 = touchio.TouchIn(board.GP12)
touch_pin13 = touchio.TouchIn(board.GP13)
touch_pin14 = touchio.TouchIn(board.GP14)
touch_pin15 = touchio.TouchIn(board.GP15)

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
touch_pin12.threshold = 1500
touch_pin13.threshold = 1500
touch_pin14.threshold = 1500
touch_pin15.threshold = 1500

led = digitalio.DigitalInOut(board.LED) # defaults to input
led.direction = digitalio.Direction.OUTPUT

speaker = pwmio.PWMOut(board.GP26, frequency=440, duty_cycle=0, variable_frequency = 1) # initializer creates instance of pwmio class

speaker_stereo = digitalio.DigitalInOut(board.GP27)
speaker_stereo.direction = digitalio.Direction.INPUT # set to tri-state if stereo not used

while True:
    if touch_pin0.value:
        speaker.frequency = 65 # C2 ~65.41Hz
    if touch_pin1.value:
        speaker.frequency = 69 # C2# ~69.3Hz
    if touch_pin2.value:
        speaker.frequency = 73 # D ~73.42Hz
    if touch_pin3.value:
        speaker.frequency = 78
    if touch_pin4.value:
        speaker.frequency = 82
    if touch_pin5.value:
        speaker.frequency = 87
    if touch_pin6.value:
        speaker.frequency = 93
    if touch_pin7.value:
        speaker.frequency = 98
    if touch_pin8.value:
        speaker.frequency = 104
    if touch_pin9.value:
        speaker.frequency = 110
    if touch_pin10.value:
        speaker.frequency = 117
    if touch_pin11.value:
        speaker.frequency = 123
    if touch_pin12.value:
        speaker.frequency = 131
    if touch_pin13.value:
        speaker.frequency = 139
    if touch_pin14.value:
        speaker.frequency = 147
    if touch_pin15.value:
        speaker.frequency = 156
        
    time.sleep(.02) # 10ms sleep time
    
    if touch_pin0.value or touch_pin1.value or touch_pin2.value or touch_pin3.value\
    or touch_pin4.value or touch_pin5.value or touch_pin6.value or touch_pin7.value\
    or touch_pin8.value or touch_pin9.value or touch_pin10.value or touch_pin11.value\
    or touch_pin12.value or touch_pin13.value or touch_pin14.value or touch_pin15.value:
        led.value = True
        speaker.duty_cycle = 32768
    else:
        led.value = False
        speaker.duty_cycle = 0
    print("GP0 ", touch_pin0.value, touch_pin0.raw_value, "  GP1 ", touch_pin1.value, "  GP11 ", touch_pin11.value, touch_pin11.raw_value)
