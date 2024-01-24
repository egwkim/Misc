from math import sin, cos, sqrt

# Orientation of the light source
# 0, 0 is perpendicular to the screen (outwards)
light_alt = 0
light_long = 0

chars = ".,-~:;=!*#$@"

height = 30
width = 2*height
r = 15

while 1:
    o = ""
    for y in (i-(height-1)/2 for i in range(height)):
        for x in ((i/2-(width-1)/4 for i in range(width))):
            if x**2 + y**2 > r**2:
                o += " "
            else:
                z = sqrt(r**2 - x**2 - y**2)
                b = z * (
                    x * cos(light_alt) * sin(light_long)
                    + y * sin(light_alt)
                    + z * cos(light_alt) * cos(light_long)
                ) / r**2
                b = max(b,0)
                o += chars[int(b*len(chars))]
        o += "\n"

    print(o)
    light_long += 0.01
    light_alt += 0.002
