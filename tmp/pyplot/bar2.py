import matplotlib.pyplot as plt
import numpy as np

cars = ['Lada', 'KIA', 'Hundai', 'VW']
weights1 = [28621, 19818, 17462, 11400]
weights2 = [30012, 18531, 14062, 8527]
x = np.arange(len(cars))
width = 0.25
fig, ax = plt.subplots()
ax.bar(x - width/2, weights1, width, label='August 2020')
ax.bar(x + width/2, weights2, width, label='August 2019')
ax.set_ylabel('Sales')
ax.set_title('Sales by model')
ax.set_xticks(x)
ax.set_xticklabels(cars)
ax.legend()
plt.show()