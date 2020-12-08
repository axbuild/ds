import matplotlib.pyplot as plt
import numpy as np

ingredients = ['Powder', 'Milk', 'Sugar', 'Eggs', 'Salt']
weights = [300, 600, 50, 75, 5]
explode = (0, 0, 0.1, 0, 0)        # "подсвечиваем" данные про сахар
fig, ax = plt.subplots()
ax.pie(weights, explode=explode, labels=ingredients, autopct='%1.0f%%', shadow=True, startangle=90)
plt.show()