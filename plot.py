from scipy.interpolate import griddata
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
X, Y = np.meshgrid(x, y)

def f(x, y):
    return x ** 2 * y ** 2 + 2

px, py = np.random.choice(x, 250), np.random.choice(y, 250)

z = griddata((px, py), f(px, py), (X, Y), method='cubic')

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.plot_surface(X, Y, z)

plt.show()

print ("Hello world")

