import matplotlib.pyplot as plt
import numpy

x_axis = [x for x in range(-3, 4)]
y_axis = [x*x for x in x_axis]
#plt.plot(x_axis, y_axis)
# plt.show()

import math



def frange(l, u, step):
    while l < u:
        yield l
        l += step

#x_axis = [x for x in range(-2*math.pi , 2*math.pi)]
#x_axis = iter(frange(-2*math.pi , 2*math.pi, math.pi / 8))
x_axis = numpy.linspace(-2*math.pi , 2*math.pi , 20)
print(x_axis)
y_axis = [math.sin(x) for x in x_axis]
plt.plot(x_axis, y_axis)

lower, upper = -2*math.pi,  2*math.pi
x_axis = list(frange(lower, upper, math.pi/8))
y_axis = [math.cos(x) for x in x_axis]
plt.plot(x_axis, y_axis)
plt.show()