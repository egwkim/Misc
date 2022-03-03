'''
x^x = n!
Solve for x using newton's method and plot (x,n)
'''


import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math

lines, = plt.plot([], [])

x=1

x_data=[]
y_data=[]

'''
for n in range(100):
    for j in range(100):
        x-=(x**x-math.factorial(n))/(x**x*(1+math.log(x)))
    
    x_data.append(x)
    y_data.append(n)
'''

s=0
for n in range(1,100000):
    s+=math.log(n)
    for j in range(100):
        x-=(x*math.log(x)-s)/(1+math.log(x))
    x_data.append(n)
    y_data.append(x/n)

plt.plot(x_data,y_data, color="b")

plt.show()