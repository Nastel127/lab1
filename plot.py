import matplotlib.pyplot as plt

plt.plot([n for _, n in sizes], times, 'o-')
plt.xscale('log', base=2)
plt.yscale('log', base=2)
plt.ylabel('время, мс')
plt.xlabel('Размер массива m')
plt.title('Зависимость времени от размера массива M')
plt.grid(True, alpha=0.3)
plt.show()