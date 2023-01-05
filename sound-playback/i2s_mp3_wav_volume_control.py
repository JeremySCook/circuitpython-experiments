# audiomixer_demo_i2s.py -- show how to fade up and down playing loops
# Code based on that of https://github.com/todbot/circuitpython-tricks/blob/main/larger-tricks/audiomixer_demo.py
# WAV file used found here: https://github.com/todbot/circuitpython-tricks/tree/main/larger-tricks/wav
# 30 Nov 2022 - @todbot / Tod Kurt
# 15 Dec 2022 - @jeremyscook

import time
import board
import audiocore
import audiomp3
import audiomixer
import audiobusio

i2s_bclk = board.GP0   # BCK on PCM5102 I2S DAC (SCK pin to Gnd)
i2s_wsel = board.GP1  # LCLK on PCM5102
i2s_data = board.GP2  # DIN on PCM5102
num_voices = 2

audio = audiobusio.I2SOut(bit_clock=i2s_bclk, word_select=i2s_wsel, data=i2s_data)

mixer = audiomixer.Mixer(voice_count=num_voices, sample_rate=22050, channel_count=1,
                         bits_per_sample=16, samples_signed=True)
audio.play(mixer) # attach mixer to audio playback

print("audio is now playing")

# set some initial levels
mixer.voice[0].level = 0.0  # drums off
mixer.voice[1].level = 0.5  # bari-uke on 50%

# load wav and start drum loop playing
wave0 = audiocore.WaveFile(open("wav/drumsacuff_22k_s16.wav","rb"))
mixer.voice[0].play( wave0, loop=True )

# load MP3 and start bari-uke playing
mp30 = audiomp3.MP3Decoder(open("mp3/bariuke-22050-32k.mp3", "rb"))
mixer.voice[1].play( mp30, loop=True )

time.sleep(1.0)  # let drums play a bit

# fade each channel up and down
up_down_inc = 0.002
while True:
    print("voice 1 level=%1.2f" % mixer.voice[1].level)
    print("voice 0 level=%1.2f" % mixer.voice[0].level)
    mixer.voice[0].level = min(max(mixer.voice[0].level - up_down_inc, 0), .5)
    mixer.voice[1].level = min(max(mixer.voice[1].level + up_down_inc, 0), .5)
    if mixer.voice[0].level == 0 or mixer.voice[1].level == 0:
        up_down_inc = -up_down_inc
    time.sleep(0.1)
