import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

n = 100000
k = 1000

points = np.zeros(k)


fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot()
ax.axis('off')

text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


def animate(i):
    global points
    points += np.random.choice([-1, 1], k)

    x_data = []
    y_data = []

    sum_abs_s = 0

    for s in set(points):
        count = np.count_nonzero(points == s)
        x_data.append(s)
        y_data.append(count)
        sum_abs_s += s * count if s > 0 else -s * count

    p, = ax.plot(x_data, y_data, 'o', color='b')
    l = ax.vlines(x_data, 0, y_data)

    text.set_text(f'pi = {(2 * k**2 * i / sum_abs_s ** 2):.2f}\nn = {i}')

    return p, l, text


anim = animation.FuncAnimation(
    fig, animate, range(1, n+1), interval=10, blit=True, repeat=False, cache_frame_data=False)

plt.show()
