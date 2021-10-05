from scipy import stats
import numpy as np 

lista = [1,7,2,2,3,4,5,6,6,6]

moda, count = stats.mode(np.array(lista))

print(moda)
print(count)
