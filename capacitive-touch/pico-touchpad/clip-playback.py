# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
CircuitPython single MP3 playback example for Raspberry Pi Pico.
Plays a single MP3 once.
-Modified JSCook 5/11/2023 from example found here: https://learn.adafruit.com/mp3-playback-rp2040/pico-mp3
-JSCook 5/22/2023 WIP for multiple clip playback based on touchpad - still need a filter to prevent pops? Can be fixed programatically?
"""
import board
import audiomp3
import audiopwmio
import digitalio
import touchio
import time

audio = audiopwmio.PWMAudioOut(board.GP26)

speaker_stereo = digitalio.DigitalInOut(board.GP27)
speaker_stereo.direction = digitalio.Direction.INPUT # set to tri-state if stereo not use

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

decoder = audiomp3.MP3Decoder(open("bariuke-22050-32k.mp3", "rb"))

while True:
    if touch_pin0.value:
        audio.play(decoder)
        while audio.playing:
            pass

print("Done playing!")
