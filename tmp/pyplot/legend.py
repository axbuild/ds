import matplotlib.pyplot as plt
import numpy as np
plt.axis([-50.0, 50.0, 0.0, 100.0])
x = np.arange(-20, 25)
plt.plot(x, x**2, label="x**2")# указываем название графика в label
plt.plot(x, (x-3)**2/3+7, label="(x-3)**2/3+7") # то же для второго графика
plt.xlabel('x')
plt.ylabel('y')
plt.legend()# сообщаем, что надо вывести легенду
#plt.legend(loc='center left')
plt.show()