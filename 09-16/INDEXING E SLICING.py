import numpy as np
import random
#PAGINA 218
#1
arr = np.random.randint(10, 51, size=20)
print(arr)
#2
print(arr[0:10])
#3
print(arr[15:])
#4
print(arr[5:15])
#5
print(arr[::3])
#6
arr[5:10] = 99
print(arr)