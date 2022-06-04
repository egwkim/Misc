import wave
import struct
import math

pi = math.pi
phi = (1 + math.sqrt(5))/2  # golden ratio

sampleRate = 44100  # samples/sec (Fs)


def sine(f: float, t: float):
    return math.sin(2*pi*f*t/sampleRate)


def chord(file:wave.Wave_read, base: float, multiplier: float, duration: float, fade:bool=True, fade_duration:float=1):
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


def golden_rhythm(file: wave.Wave_read):
    frame = bytes()


if __name__ == "__main__":
    mode = input("1: golden chord\n"
                 "2: A - F chord\n"
                 "3: golden rhythm\n"
                 "4: golden polyrhythm\n"
                 "5: golden music\n"
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
            golden_rhythm()
        elif mode == "4":
            # golden polyrhythm
            pass
        elif mode == "5":
            # golden music
            pass
        else:
            print("Invalid input")
