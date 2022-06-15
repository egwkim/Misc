from random import sample
import wave
import struct
import math

pi = math.pi
phi = (1 + math.sqrt(5))/2  # golden ratio

sampleRate = 44100  # samples/sec (Fs)


def sine(f: float, t: float):
    return math.sin(2*pi*f*t/sampleRate)


def chord(file: wave.Wave_write, base: float, multiplier: float, duration: float, fade: bool = True, fade_duration: float = 1):
    duration = 2.5  # seconds
    frequency = 440  # Hz
    frame = bytes()
    for i in range(int(duration*sampleRate)):
        # Write every half second
        if (i+1) % int(sampleRate/2) == 0:
            file.writeframes(frame)
            frame = bytes()

        # Generate sine value
        value = 0
        value += sine(frequency, i)
        value += sine(frequency * phi, i)

        # Fade out for one second
        if i > (duration-1)*sampleRate:
            value *= 0.02**(i/sampleRate - duration + 1)

        # Amplify and add to frame
        value = int(2047*value)
        frame += struct.pack('<h', value)

    if frame:
        file.wirteframes(frame)


def golden_rhythm(file: wave.Wave_write):
    frame = bytes()
    bpm = 120
    # Play sound every 60 / bpm secons
    # Play sound every phi * 60 / bpm seconds


def fibonacci_rhythm(file: wave.Wave_write):
    a = 13
    b = 21

    bpm = 60 * a

    # Sound to play every a beats
    a_sound = []
    with wave.open('a.wav', 'r') as file:
        if file.getnchannels() != 1:
            return
        if file.getframerate() != sampleRate:
            return
        if file.getsampwidth != 2:
            return
        frames: bytes = file.readframes(sampleRate)
        a_sound += list(struct.unpack('<h', frames))
        if len(a_sound) > beat_duration:
            a_sound = a_sound[:beat_duration]

    # Sound to play every b beats
    b_sound = []
    with wave.open('b.wav', 'r') as file:
        if file.getnchannels() != 1:
            return
        if file.getframerate() != sampleRate:
            return
        if file.getsampwidth != 2:
            return
        frames: bytes = file.readframes(sampleRate)
        b_sound += list(struct.unpack('<h', frames))
        if len(b_sound) > beat_duration:
            b_sound = b_sound[:beat_duration]

    # Total number of samples
    duration = (sampleRate * a * b * 60 // bpm) + \
        max(len(a_sound), len(b_sound)) + 1

    # A number of samples in one beat
    beat_duration = sampleRate * 60 / bpm

    # Play sound every a beats
    a_beat: list = a_sound + [0] * (beat_duration * a - len(a_sound))

    # Play sound every b beats
    b_beat: list = b_sound + [0] * (beat_duration * b - len(b_sound))

    frame = bytes()
    for i in range(duration):
        if (i+1) % int(sampleRate/2) == 0:
            # Write every half second
            file.writeframes(frame)
            frame = bytes()

        # Add a_beat and b_beat
        value = a_beat[i % beat_duration * a] + b_beat[i % beat_duration * b]
        frame += struct.pack('<h', value)

    if frame:
        file.writeframes(frame)


if __name__ == "__main__":
    mode = input("1: golden chord\n"
                 "2: A - F chord\n"
                 "3: golden rhythm\n"
                 "4: fibonacci rhythm\n"
                 "input: ")

    with wave.open('sound.wav', 'w') as file:
        file.setnchannels(1)  # mono
        file.setsampwidth(2)  # 16-bit
        file.setframerate(sampleRate)

        if mode == "1":
            chord(file, 440, phi, 2.5)
        elif mode == "2":
            chord(file, 440, 1.6, 2.5)
        elif mode == "3":
            golden_rhythm(file)
        elif mode == "4":
            fibonacci_rhythm(file)
        else:
            print("Invalid input")
