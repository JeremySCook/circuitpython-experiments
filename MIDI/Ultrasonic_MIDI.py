"""
prototype code using two ultrasonic sensors to send MIDI signals
For usage on RPi Pico @JeremySCook 12/28/2022

Builtin LED goes high when distance is under 12 cm
Works with VBUS or VSYS ~5VDC on Raspberry Pi Pico

SoopaDoopa Update 2023-11-18: Repeated calls to adafruit_hcsr04 within the loop was causing the code to fail on recent versions of CircuitPython on Pi Pico W.
Modified to code only get the distance of each HC-SR04 ultrasonic sensors only once per loop, storing the results in variables.

"""

import time
import board
import usb_midi
import adafruit_midi
import adafruit_hcsr04
import digitalio

from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
from adafruit_midi.pitch_bend import PitchBend
from adafruit_midi.control_change import ControlChange

sonar1 = adafruit_hcsr04.HCSR04(trigger_pin=board.GP17, echo_pin=board.GP16)
sonar2 = adafruit_hcsr04.HCSR04(trigger_pin=board.GP19, echo_pin=board.GP18)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)
key_on = 0
distance_note = 0
current_note = 0
midi.send(ControlChange(64, 0))  # sustain CC - e.g. 0 = off, 127 = on

while True:
    try:
        print(current_note)

        sonar1Distance = sonar1.distance
        sonar2Distance = sonar2.distance
        
        #print(int(sonar1.distance))
        if sonar1Distance < 12 and led.value == 0:
            current_note = int(sonar2Distance/4) + 40
            midi.send(NoteOn(current_note, 120))  # G sharp 2nd octave (1 per Garageband), 44th key on piano - velocity = 120
            key_on = 1
            led.value = 1
            
        # midi.send(NoteOff(44, 120))
        elif sonar1Distance >= 12 and key_on == 1: # Add a dead zone?          
            midi.send(NoteOff(current_note, 120))
            key_on = 0
            led.value = 0
    except RuntimeError:
        print("Retrying sonar1!")
    time.sleep(0.05)

