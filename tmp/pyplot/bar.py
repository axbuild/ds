import matplotlib.pyplot as plt
import numpy as np

weights = [28621, 19818, 17462, 11400]
x = np.arange(len(weights))
plt.bar(x, weights)
plt.show()