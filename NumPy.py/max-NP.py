import numpy as np

#Create a program that finds the maximum element in each row of a 2D NumPy array.

x = np.array([[8,3],[5,2]])

y = np.max(x,axis=1)

print(y)