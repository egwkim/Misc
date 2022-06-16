import wave
import struct


def convert_1bit(source: wave.Wave_read, out: wave.Wave_write):
    params = source.getparams()
    out.setparams(params)
    out.setsampwidth(1)

    if params.sampwidth == 1:
        format = '<b'
    elif params.sampwidth == 2:
        format = '<h'
    elif params.sampwidth == 4:
        format = '<i'
    elif params.sampwidth == 8:
        format = '<q'
    else:
        print('Unsupported format')
        return

    while True:
        frame = source.readframes(1)
        if not frame:
            break
        value = struct.unpack(format, frame)[0]
        if value < 0:
            out.writeframes(struct.pack('<b', -128))
        else:
            out.writeframes(struct.pack('<b', 127))


if __name__ == '__main__':
    input_name = input('Input file name: ')
    output_name = input('Output file name: ')

    with wave.open(input_name, 'r') as input_file, wave.open(output_name, 'w') as output_file:
        convert_1bit(input_file, output_file)
