import numpy as np

data = np.array([1, 2, 3, 4, 5], )
print("Array creado:", data)

reshaped_data = data.reshape((5, 1))
print("Array reestructurado:\n", reshaped_data)

mean_value = np.mean(data)
print("Promedio del array:", mean_value)

random_array = np.random.rand(5)
print("Array de números aleatorios:", random_array)

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
dot_product = np.dot(array1, array2)
print("Producto punto:", dot_product)
