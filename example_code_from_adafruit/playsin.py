from digitalio import DigitalInOut, Direction
import audioio
import board
import array
import time
import math

note_freq = {
'A6':1760,
'G♯6':1661.22,
'A♭6':1661.22,
'G6':1567.98,
'F♯6':1479.98,
'G♭6':1479.98,
'F6':1396.91,
'E6':1318.51,
'D♯6':1244.51,
'E♭6':1244.51,
'D6':1174.66,
'C♯6':1108.73,
'D♭6':1108.73,
'C6':1046.5,
'B5':987.767,
'A♯5':932.328,
'B♭5':932.328,
'A5':880,
'G♯5/A♭5':830.609,
'G5':783.991,
'F♯5/G♭5':739.989,
'F5':659.255,
'D♯5/E♭5':622.254,
'D5':587.33,
'C♯5/D♭5':554.365,
'C5':523.251,
'B4':493.883,
'A♯4/B♭4':466.164,
'A4':440,
'G♯4/A♭4':415.305,
'G4':391.995,
'F♯4/G♭4':369.994,
'F4':349.228,
'E4':329.628,
'D♯4/E♭4':311.127,
'D4':293.665,
'C♯4/D♭4':	277.183,
'C4':261.626,
'B3':246.942,
'A♯3/B♭3':233.082,
'A3':220
}


FREQUENCY = 440    # 440 Hz middle 'A'
SAMPLERATE = 8000  # 8000 samples/second, recommended!

# Generate one period of sine wav.
length = SAMPLERATE // FREQUENCY
sine_wave = array.array("H", [0] * length)
for i in range(length):
    sine_wave[i] = int(math.sin(math.pi * 2 * i / 18) * (2 ** 15) + 2 ** 15)

# enable the speaker
spkrenable = DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = Direction.OUTPUT
spkrenable.value = True


sample = audioio.AudioOut(board.SPEAKER, sine_wave)
sample.frequency = SAMPLERATE
sample.play(loop=True)  # keep playing the sample over and over
time.sleep(0.25)           # until...
sample.stop()           # we tell the board to stop
