import matplotlib.pyplot as plt
import numpy as np

cars = ['Lada', 'KIA', 'Hundai', 'VW']
weights = [28621, 19818, 17462, 11400]
x = np.arange(len(cars))
width = 0.5
fig, ax = plt.subplots()            # снова работаем с фигурами и осями
ax.bar(x, weights, width, label='August 2020')
ax.set_ylabel('Sales')
ax.set_title('Sales by model')
ax.set_xticks(x)                # указываем, где отрисовывать метки
ax.set_xticklabels(cars)            # указываем текст меток
ax.legend()
plt.show()