import board
import touchio
import time
import pwmio
import digitalio

touch_pin0 = touchio.TouchIn(board.GP13)
touch_pin1 = touchio.TouchIn(board.GP14)
touch_pin2 = touchio.TouchIn(board.GP15)

touch_pin0.threshold = 3000
touch_pin1.threshold = 3000
touch_pin2.threshold = 3000

led = digitalio.DigitalInOut(board.LED) # defaults to input
led.direction = digitalio.Direction.OUTPUT

speaker = pwmio.PWMOut(board.GP26, frequency=440, duty_cycle=0, variable_frequency = 1) # initializer creates instance of pwmio class

while True:
    if touch_pin0.value:
        speaker.frequency = 196 # G
    if touch_pin1.value:
        speaker.frequency = 147 # D
    if touch_pin2.value:
        speaker.frequency = 110 # A
        
    time.sleep(.02) # 10ms sleep time
    
    if touch_pin0.value or touch_pin1.value or touch_pin2.value:
        led.value = True
        speaker.duty_cycle = 32768
    else:
        led.value = False
        speaker.duty_cycle = 0
    print("GP0 ", touch_pin0.value, touch_pin0.raw_value, touch_pin0.threshold, "  GP1 ", touch_pin1.value, "  GP2 ", touch_pin2.value)
