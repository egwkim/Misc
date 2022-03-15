import matplotlib.pyplot as plt
#import matplotlib.colors
import cmath

fig = plt.figure(figsize=(6, 6))

ax = fig.add_subplot()
ax.set_aspect('equal')

x_list = []
y_list = []

#start = 1j*cmath.pi*(1-1/5)
#end = 1j*cmath.pi*(1+1/5)

start = 0
end = 1j*cmath.pi*2

accuracy = 300000
for i in range(accuracy):
    z = ((cmath.exp(start + (end - start) * (i / accuracy)) + 1)/2) ** 1j
    #z = ((cmath.exp(start + (end - start) * (i / accuracy)) + 1)) ** 1j
    
    x_list.append(z.real)
    y_list.append(z.imag)

    #plt.plot(z.real, z.imag, '.', matplotlib.colors.hsv_to_rgb([i/accuracy, 1, 1]))


plt.plot(x_list[:100000],y_list[:100000],'.', color='r')
plt.plot(x_list[100000:200000],y_list[100000:200000],'.', color='g')
plt.plot(x_list[200000:],y_list[200000:],'.', color='b')


plt.show()
