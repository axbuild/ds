import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(100) * 0.1 + 0.5        # x-координаты наших точек
plt.scatter(x, x + 0.5 + np.random.randn(x.shape[0]) * 0.1, c = 'b')    # первое множество
plt.scatter(x, -x + 0.4 + np.random.randn(x.shape[0]) * 0.1, c = 'r')   # второе множество
plt.show()