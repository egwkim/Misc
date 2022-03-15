import matplotlib.pyplot as plt
import cmath

fig = plt.figure(figsize=(6, 6))

ax = fig.add_subplot()
#ax = fig.add_subplot(xlim=(0, 40000), ylim=(-20000, 20000))
#ax.set_aspect('equal')

x_list = []
y_list = []

#start = 1j*cmath.pi*(1-1/5)
#end = 1j*cmath.pi*(1+1/5)

start = 0
end = 1j*cmath.pi*2

accuracy = 300000
for i in range(accuracy):
    z = ((cmath.exp(start + (end - start) * (i / accuracy)) + 1)/2) ** 3
    x_list.append(z.real)
    y_list.append(z.imag)
    #print(i, z, z.real, z.imag)


plt.plot(x_list, y_list)
plt.show()
