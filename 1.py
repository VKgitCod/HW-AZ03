import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0, 1, 1000)

plt.hist(data, bins=1000)

plt.title("Гистограмма")
plt.xlabel("Ось Х")
plt.ylabel("Ось Y")

plt.show()