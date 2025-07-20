import numpy as np

print('Diagonal Matrix')

x = np.array([1,2,3,4])

def dig(matrix):
    return np.diag(matrix)

y = dig(x)
print(y)

