import numpy as np

vector = np.array([1, 2, 3, 4])

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Vector (unidimensional):")
print(vector)
print("Dimensión del vector:", vector.ndim)
print("Forma del vector:", vector.shape)

print("\n" + "="*40 + "\n")

print("Matriz (bidimensional):")
print(matriz)
print("Dimensión de la matriz:", matriz.ndim)
print("Forma de la matriz:", matriz.shape)

print("\n" + "="*40 + "\n")

print("Suma de todos los elementos del vector:", vector.sum())
print("Suma de todos los elementos de la matriz:", matriz.sum())

print("\n" + "="*40 + "\n")

print("Primer elemento del vector:", vector[0])
print("Elemento en la segunda fila, tercera columna de la matriz:", matriz[1, 2])

print("\n" + "="*40 + "\n")

print("Producto escalar del vector:", np.dot(vector, vector))
print("Producto de matrices:")
print(np.dot(matriz, matriz))