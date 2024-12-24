import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0,2*np.pi, 25)
b = np.array([np.sin(x) for x in a])

plt.plot(a, b, label='sin(x)')