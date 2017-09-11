import matplotlib.pyplot as plt
import numpy
from math import pi , sin , cos, tan

lower , upper  = -2*pi , 2*pi
x_axis = numpy.linspace(lower, upper , 20)
y_axis = [sin(x) for x in x_axis]
plt.plot(x_axis, y_axis)

y_axis = [cos(x) for x in x_axis]
plt.plot(x_axis , y_axis)

y_axis = [tan(x) for x in x_axis]
plt.scatter(x_axis, y_axis)

plt.show()