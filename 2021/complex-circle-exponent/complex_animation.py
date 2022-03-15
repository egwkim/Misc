import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import cmath


fig = plt.figure(figsize=(6, 6))

ax = fig.add_subplot()
ax.set_aspect('equal')

exponent_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def animate(k):
    
    x_list = []
    y_list = []

    #start = 1j*cmath.pi*(1-1/5)
    #end = 1j*cmath.pi*(1+1/5)
    
    start = 0
    end = 1j*cmath.pi*2

    accuracy = 5000
    for i in range(accuracy):
        z = ((cmath.exp(start + (end - start) * (i / accuracy)) + 1)/2) ** k
        x_list.append(z.real)
        y_list.append(z.imag)

    
    exponent_text.set_text(f'{k:.2f}')

    lines, = ax.plot(x_list, y_list, color='b')
    
    return lines, exponent_text


ani = animation.FuncAnimation(fig, animate,
frames=np.arange(1,10.01,0.01), interval=10, blit=True, repeat=False)

plt.show()
