import pandas as pd
import numpy as np
# Creación de un DataFrame en Pandas
data = {
 'A': [1, 2, 3, 4],
 'B': [5, 6, 7, 8]
 
}
df = pd.DataFrame(data)
# Selección y Filtrado
filtered_df = df[df['A'] > 2]
#print(filtered_df)
# Estadísticas Descriptivas
mean_value = df['A'].mean()
# Operaciones con NumPy
array = np.array([[1, 2], [3, 4]])
# Producto punto
dot_product = np.dot(array, array)
# Transformación de Arrays
reshaped_array = array.reshape((4, 1))
print("Filtered DataFrame:")
print(filtered_df)
print("Mean Value of Column A:", mean_value)
print("Dot Product of Array:")
print(dot_product)
print("Reshaped Array:")
print(reshaped_array)