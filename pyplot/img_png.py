import matplotlib.pyplot as plt

plt.plot([x**2 for x in range(-10, 11)])
plt.savefig('parabolic.png')        # график будет сохранён в файле parabolic.png