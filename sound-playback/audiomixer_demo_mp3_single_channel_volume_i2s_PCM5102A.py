# audiomixer_demo_i2s.py -- show how to fade up and down playing loops
# Code based on that of https://github.com/todbot/circuitpython-tricks/blob/main/larger-tricks/audiomixer_demo.py
# WAV file used found here: https://github.com/todbot/circuitpython-tricks/tree/main/larger-tricks/wav
# 30 Nov 2022 - @todbot / Tod Kurt
# 15 Dec 2022 - @jeremyscook
# July 31 2022 - @jeremyscook modified for PCM5102A I2S DAC boards
# Reference: https://todbot.com/blog/2023/05/16/cheap-stereo-line-out-i2s-dac-for-circuitpython-arduino-synths/
# Arrange DAC on breadboard w/ SCK directly attached to RPi Pico GND, BCK to GPIO 17, DIN to GPIO 16
# Sound file available here: https://github.com/JeremySCook/circuitpython-experiments/tree/main/sound-playback/MP3s

import time
import board
import audiocore
import audiomp3
import audiomixer
import audiobusio

i2s_bclk = board.GP17  # BCK on PCM5102 (connect PCM5102 SCK pin to Gnd)
i2s_wsel = board.GP18 # LCK on PCM5102
i2s_data = board.GP16 # DIN on PCM5102
num_voices = 1

audio = audiobusio.I2SOut(bit_clock=i2s_bclk, word_select=i2s_wsel, data=i2s_data)

mixer = audiomixer.Mixer(voice_count=num_voices, sample_rate=22050, channel_count=1,
                         bits_per_sample=16, samples_signed=True)
audio.play(mixer) # attach mixer to audio playback

print("audio is now playing")

# set some initial levels
mixer.voice[0].level = 1  # MP3 file playing at full volume

# load wav and start drum loop playing
mp30 = audiomp3.MP3Decoder(open("mp3/bariuke-22050.mp3", "rb"))
mixer.voice[0].play( mp30, loop=True )

while True:
    print("voice 0 level=%1.2f" % mixer.voice[0].level)

# end
