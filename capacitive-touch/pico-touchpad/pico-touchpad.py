# Based on code by todbot: https://github.com/todbot/picotouch/blob/main/circuitpython/picotouch/code.py
# Modified for3-pad MIDI thingy by @jeremyscook 3/6/2023

import time
import board
import touchio
import digitalio
import usb_midi
import adafruit_midi
from adafruit_midi.note_on  import NoteOn
from adafruit_midi.pitch_bend  import PitchBend
from adafruit_midi.control_change  import ControlChange
from adafruit_debouncer import Debouncer, Button

led = digitalio.DigitalInOut(board.LED) # defaults to input
led.direction = digitalio.Direction.OUTPUT

debug = True
octave = 4

midi_velocity = 64  # midpoint
midi_channel = 0  # 0-15
midi_cc_num = 1   # standard modwheel

touch_threshold_adjust = 300

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1])

touch_pins = (
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5,
    board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11,
    board.GP12, board.GP13, board.GP14, board.GP15
)
touch_pads = []
touch_ins = []

for pin in touch_pins:
    touchin = touchio.TouchIn(pin)
    touchin.threshold += touch_threshold_adjust
    touch_pads.append( Button(touchin, value_when_pressed=True))
    touch_ins.append(touchin)  # for debug

num_touch_pads = len(touch_pads)

notes_on = [0] * num_touch_pads  # list of notes currently sounding

print("\n----------")
print("picotouch hello")

while True:
    for i in range(num_touch_pads):
        touch = touch_pads[i]
        touch.update()
        if touch.rose:
            led.value = True
            midi.send( PitchBend(8192) , channel=midi_channel)
            noteOn = NoteOn((12*octave) + i, midi_velocity)
            notes_on[i] = noteOn
            midi.send( noteOn, channel=midi_channel )
                
        if touch.fell:
            led.value = False
            noteOn = notes_on[i]
            noteOn.velocity = 0  # noteOff == noteOn w/ zero velocity (as well as NoteOff)
            midi.send( noteOn, channel=midi_channel )
