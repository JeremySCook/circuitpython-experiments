# Based on code by todbot: https://github.com/todbot/picotouch/blob/main/circuitpython/picotouch/code.py
# Modified for3-pad MIDI thingy by @jeremyscook 3/6/2023

import time
import board
import touchio
import digitalio
import usb_midi
import adafruit_midi
from adafruit_midi.note_on import NoteOn
from adafruit_midi.pitch_bend import PitchBend
from adafruit_midi.control_change import ControlChange
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
    board.PAD1, board.PAD2, board.PAD3, board.PAD4, board.PAD5, board.PAD6,
    board.PAD7, board.PAD8, board.PAD9, board.PAD10, board.PAD11, board.PAD12,
    board.PAD13, board.PAD14, board.PAD15, board.PAD16, board.OP1, board.OP2,
    board.OP3
)

option1_pad = 16
option2_pad = 17
option3_pad = 18

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
            if i == option1_pad:
                print("option 1 pressed")
            elif i == option2_pad:
                print("option 2 pressed")
            elif i == option3_pad:
                print("option 3 pressed")
            else:
                led.value = True
                midi.send( PitchBend(8192) , channel=midi_channel)
                noteOn = NoteOn((12*octave) + i, midi_velocity)
                notes_on[i] = noteOn
                midi.send( noteOn, channel=midi_channel )
                print("touch pad", i+1)

        if touch.fell:
            led.value = False
            if i == option1_pad:
                print("option 1 released")
            elif i == option2_pad:
                print("option 2 released")
            elif i == option3_pad:
                print("option 3 released")
            else:
                noteOn = notes_on[i]
                noteOn.velocity = 0  # noteOff == noteOn w/ zero velocity (as well as NoteOff)
                midi.send( noteOn, channel=midi_channel )
                print("touch pad off", i+1)
