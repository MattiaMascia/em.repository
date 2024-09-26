import numpy as np
import random
#PAGINA 225
#1
array = np.linspace(0, 10, 50)
print(array)
#2
rand_array = np.random.random(50)
print(rand_array)
#3
new_arr = array + rand_array
print(new_arr)
#4
print(np.sum(new_arr))
#5
somma_maggiori_5 = np.sum(new_arr[new_arr>5])
print(somma_maggiori_5)


