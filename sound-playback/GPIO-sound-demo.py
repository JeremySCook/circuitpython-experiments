# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
CircuitPython single MP3 playback example for Raspberry Pi Pico.
Plays a single MP3 once.
-Modified JSCook 5/11/2023 from example found here: https://learn.adafruit.com/mp3-playback-rp2040/pico-mp3
"""
import board
import audiomp3
import audiopwmio

audio = audiopwmio.PWMAudioOut(board.GP26)

decoder = audiomp3.MP3Decoder(open("bariuke-22050-32k.mp3", "rb"))

while True:
    audio.play(decoder)
    while audio.playing:
        pass

print("Done playing!")
