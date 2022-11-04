import wave
import struct
import math

pi = math.pi
phi = (1 + math.sqrt(5))/2  # golden ratio

sampleRate = 44100  # samples/sec (Fs)


def sine(f: float, t: float):
    return math.sin(2*pi*f*t/sampleRate)


def chord(file: wave.Wave_write, base: float, multiplier: float, duration: float,
          fade: bool = True, fade_duration: float = 1, fade_coeff: float = 0.02):
    frame = bytes()
    for i in range(int(duration*sampleRate)):
        # Write every half second
        if (i+1) % int(sampleRate/2) == 0:
            file.writeframes(frame)
            frame = bytes()

        # Generate sine value
        value = 0
        value += sine(base, i)
        value += sine(base * multiplier, i)

        # Fade out for one second
        if fade and i > (duration-fade_duration)*sampleRate:
            time = i/sampleRate - duration + fade_duration
            value *= fade_coeff**(time / fade_duration)

        # Amplify and add to frame
        value = int(2047*value)
        frame += struct.pack('<h', value)
    file.writeframes(frame)


def load_wav(filename: str, length: int):
    wave_data = []
    with wave.open(filename, 'r') as file:
        if file.getnchannels() != 1:
            return
        if file.getframerate() != sampleRate:
            return
        if file.getsampwidth() != 2:
            return
        while True:
            frames: bytes = file.readframes(1)
            if not frames:
                break
            wave_data += list(struct.unpack('<h', frames))
        if len(wave_data) > length:
            wave_data = wave_data[:length]
        else:
            wave_data += [0] * (length - len(wave_data))
    return wave_data


def golden_rhythm(out: wave.Wave_write, bpm: float, beats: int, beat1: str, beat2: str = None):
    if beat2 == None:
        beat2 = beat1

    frame: bytes = bytes()

    # Total number of samples
    duration: int = int(beats * sampleRate * 60 // bpm)

    # The number of samples in one beat
    beat_duration: int = int(sampleRate * 60 // bpm)

    # Load sounds
    a_sound = load_wav(beat1, beat_duration)
    b_sound = load_wav(beat2, int(beat_duration*phi)+1)

    frame = bytes()
    for i in range(duration):
        if (i+1) % int(sampleRate/2) == 0:
            # Write every half second
            out.writeframes(frame)
            frame = bytes()

        # Play a_sound every 60 / bpm seconds
        # Play b_sound every phi * 60 / bpm seconds
        value = a_sound[i % beat_duration] + \
            b_sound[int(i % (beat_duration*phi))]
        value //= 2
        frame += struct.pack('<h', value)

    out.writeframes(frame)


def fibonacci_rhythm(out: wave.Wave_write, beat1: str, beat2: str = None):
    if beat2 == None:
        beat2 = beat1

    a = 13
    b = 21
    bpm = 60 * a * 2

    # The number of samples in one beat
    beat_duration = sampleRate * 60 // bpm

    # Sound to play every a beats
    a_sound = load_wav(beat1, beat_duration * a)

    # Sound to play every b beats
    b_sound = load_wav(beat2, beat_duration * b)

    # Total number of samples
    duration = sampleRate * a * b * 60 // bpm

    frame = bytes()
    for i in range(duration):
        if (i+1) % int(sampleRate/2) == 0:
            # Write every half second
            out.writeframes(frame)
            frame = bytes()

        # Add a_beat and b_beat
        value = a_sound[i % len(a_sound)] + b_sound[i % len(b_sound)]
        value //= 2
        frame += struct.pack('<h', value)

    out.writeframes(frame)


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
            bpm = int(input('BPM: '))
            beats = int(input('Total beats: '))
            golden_rhythm(file, bpm, beats, 'a.wav', 'a.wav')
        elif mode == "4":
            fibonacci_rhythm(file)
        else:
            print("Invalid input")
