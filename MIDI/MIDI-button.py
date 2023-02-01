# modification of code: https://docs.circuitpython.org/projects/midi/en/latest/
# Adds a button on pin 16
# @JeremySCook 12/27/2022

import time
import random
import usb_midi
import adafruit_midi
import board
import digitalio

from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
from adafruit_midi.pitch_bend import PitchBend
from adafruit_midi.control_change import ControlChange

button = digitalio.DigitalInOut(board.GP16)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)
key_on = 0

print("Midi test")

print("Default output MIDI channel:", midi.out_channel + 1)

midi.send(ControlChange(64, 0))  # sustain CC - e.g. 0 = off, 127 = on

while True:
    if button.value == 0 and key_on == 0:
        midi.send(NoteOn(44, 120))  # G sharp 2nd octave, 44th key on piano - velocity = 120
        key_on = 1
        time.sleep(.05) # debounce
        # midi.send(NoteOff(44, 120))
    elif button.value == 1 and key_on == 1:
        midi.send(NoteOff(44, 120))
        key_on = 0
        time.sleep(.05) # debounce
