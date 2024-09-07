#print("hola mundo") 
import numpy as np
# Crear vectores
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])
# Suma de vectores
vector_sum = vector_a + vector_b
# Producto escalar
dot_product = np.dot(vector_a, vector_b)
# Crear matrices
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
# Suma de matrices
matrix_sum = matrix_a + matrix_b
# Multiplicación de matrices
matrix_product = np.dot(matrix_a, matrix_b)
print("Vector Sum:", vector_sum)
print("Dot Product:", dot_product)
print("Matrix Sum:\n", matrix_sum)
print("Matrix Product:\n", matrix_product)