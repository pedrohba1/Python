import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

salario = np.array([100,12,12,3,41,24,5])
salario2 = np.array([1100,52,12,3,512,3,61463])

arr = np.array([[1,2,3,4], [5,6,7,8]])
print(arr)
np.insert(arr, 1 ,10)

print(arr)

plt.plot(salario, c = 'Black',ls = '--', marker = 's', label = 'salario1')
plt.plot(salario2, c = 'Red',ls = '--', marker = 's', label = 'salario2	')
plt.legend()
#plt.show()