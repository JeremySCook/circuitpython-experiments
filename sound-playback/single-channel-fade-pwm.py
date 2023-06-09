# audiomixer_demo.py -- show how to fade up and down playing loops
# note this causes glitches and crashes on RP2040
# 9 Feb 2022 - @todbot / Tod Kurt
# 9 June 2023 modified by @JeremyScook to fade one channel up and down by itself
# Original: https://github.com/todbot/circuitpython-tricks/tree/main/larger-tricks
# Wav files: https://github.com/todbot/circuitpython-tricks/tree/main/larger-tricks/wav

import time
import board
import audiocore
import audiomixer
from audiopwmio import PWMAudioOut as AudioOut  # for RP2040 etc
# from audioio import AudioOut as AudioOut  # for SAMD51/M4 etc

num_voices = 1

# audio pin is almost any pin on RP2040, let's do A0 (RP2040 GPIO226) or RX (RP2040 GPIO1)
# audio pin is A0 on SAMD51 (Trelllis M4, Itsy M4, etc)
audio = AudioOut(board.GP15)
mixer = audiomixer.Mixer(voice_count=num_voices, sample_rate=22050, channel_count=1,
                         bits_per_sample=16, samples_signed=True)
# attach mixer to audio playback
audio.play(mixer)

mixer.voice[0].level = 1.0
#mixer.voice[1].level = 0.0

# start drum loop playing
wave0 = audiocore.WaveFile(open("wav/drumsacuff_22k_s16.wav","rb"))
mixer.voice[0].play( wave0, loop=True )

# start synth loop playing
#wave1 = audiocore.WaveFile(open("wav/snowpeaks_22k_s16.wav","rb"))
#mixer.voice[1].play( wave1, loop=True )

time.sleep(1.0)  # let drums play a bit

# fade each channel up and down
up_down_inc = 0.03
while True:
    #mixer.voice[1].level = min(max(mixer.voice[1].level + up_down_inc, 0), 1)
    mixer.voice[0].level = min(max(mixer.voice[0].level - up_down_inc, 0), 1)
    if mixer.voice[0].level == 0 or mixer.voice[0].level == 1:
        up_down_inc = -up_down_inc
    time.sleep(0.1)
