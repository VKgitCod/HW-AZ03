import matplotlib.pyplot as plt
import numpy as np

random_array1 = np.random.rand(5)
random_array2 = np.random.rand(5)

plt.scatter(random_array1, random_array2)

plt.title("Диаграмма рассеяния")
plt.xlabel("Ось Х")
plt.ylabel("Ось Y")

plt.show()