#Implement a program that calculates the determinant of a square matrix using NumPy.
import numpy as np

x = np.array([[[1,2,3],[4,5,6],[7,8,9]]])

def squree(val):
    return np.linalg.matrix_power(x,2)

squre = squree(x)

print(np.linalg.det(squre))