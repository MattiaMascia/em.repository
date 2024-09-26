# PAGINA 224
import numpy as np
#1
arr = np.linspace(0, 1, 12)
print(arr)
#2
reshaped_arr = arr.reshape((3, 4))
print(reshaped_arr)
#3
random_arr = np.random.rand(3,4)
print(random_arr)
#4
sum_value1 = np.sum(arr)
sum_value2 = np.sum(random_arr)
print(sum_value1)
print(sum_value2)
#5 reshape
reshaped_arr = arr.reshape((4, 3))
print(reshaped_arr)

