# SPDX-FileCopyrightText: 2022 John Park for Adafruit Industries
# SPDX-License-Identifier: MIT

# Breakbeat Breadboard based on:
# @todbot / Tod Kurt - https://github.com/todbot/plinkykeeb
# Convert files to appropriate WAV format (mono, 22050 Hz, 16-bit signed) with command:
#  sox loop.mp3 -b 16 -c 1 -r 22050 loop.wav
# put samples in "/wav" folder

# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Modified - Still WIP JSCook 5/23/2023
Possible to use MP3 files? Out of space with just a few clips.
"""

import time
import board
import digitalio
import touchio
import audiocore
import audiomixer
from audiopwmio import PWMAudioOut as AudioOut
from adafruit_debouncer import Debouncer, Button

# wait a little bit so USB can stabilize and not glitch audio
time.sleep(1)
print("Hello")

# list of (samples to play, mixer gain level)
wav_files = (
    ('wav/amen_22k16b_160bpm.wav', 1.0),
    ('wav/pt_limor_modem_vox_01.wav', 0.4),
    ('wav/snowpeaks_22k_s16.wav', 0.8),
    ('wav/doom_22050.wav', 1)
)

touch_pins = (
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5,
    board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11,
    board.GP12, board.GP13, board.GP14, board.GP15
)
touch_pads = []
touch_ins = []

for pin in touch_pins:
    touchin = touchio.TouchIn(pin)
    touchin.threshold = 1500
    touch_pads.append( Button(touchin, value_when_pressed=True))
    touch_ins.append(touchin)  # for debug

num_touch_pads = len(touch_pads)


audio = AudioOut(board.GP26)

speaker_stereo = digitalio.DigitalInOut(board.GP27)
speaker_stereo.direction = digitalio.Direction.INPUT # set to tri-state if stereo not use

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

mixer = audiomixer.Mixer(voice_count=len(wav_files), sample_rate=22050, channel_count=1,
                         bits_per_sample=16, samples_signed=True)
audio.play(mixer) # attach mixer to audio playback

for i in range(len(wav_files)):  # start all samples at once for use w handle_mixer
    wave = audiocore.WaveFile(open(wav_files[i][0],"rb"))
    mixer.voice[i].play(wave, loop=True)
    mixer.voice[i].level = 0

def handle_mixer(num, pressed):
    voice = mixer.voice[num]   # get mixer voice
    if pressed:
        wave = audiocore.WaveFile(open(wav_files[i][0],"rb"))
        voice.play(wave, loop=True)
        voice.level = 1 # play at level in wav_file list
        print("playing clip ", num)
    else: # released
        voice.level = 0  # mute it


while True:
    for i in range(len(wav_files)):
        touch = touch_pads[i]
        touch.update()
        if touch.rose:
            led.value = True
            handle_mixer(i, True)
            print(i, " True")
        if touch.fell:
            led.value = False
            handle_mixer(i, False)
            print(i, " Fale")
