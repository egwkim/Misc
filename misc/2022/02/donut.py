from math import sin, cos
import os
def cls(): os.system('cls')


x_rotation = 0
y_rotation = 0

while(1):
    buffer = [' ']*1760
    z_buffer = [0]*1760
    for j in [aa*0.01 for aa in range(0, 628, 7)]:
        for i in [aaa*0.01 for aaa in range(0, 628, 2)]:
            c = sin(i)
            d = cos(j)
            e = sin(x_rotation)
            f = sin(j)
            g = cos(x_rotation)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = cos(i)
            m = cos(y_rotation)
            n = sin(y_rotation)
            t = c * h * g - f * e
            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            o = int(x + 80 * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if (22 > y and y > 0 and x > 0 and 80 > x and D > z_buffer[o]):
                z_buffer[o] = D
                buffer[o] = ".,-~:;=!*#$@"[N if N>0 else 0]
    
    out_str = ""
    for k in range(1761):
        out_str += buffer[k] if k%80 else "\n"
    
    #cls()
    print(out_str)
    
    x_rotation += 0.04
    y_rotation += 0.02