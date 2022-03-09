import matplotlib.pyplot as plt
import numpy as np

a = np.random.normal(170, 10, 250)
print(a)
plt.hist(a)
plt.show()

a = np.array([170, 10, 250])
print(a)
plt.hist(a)
plt.show()
