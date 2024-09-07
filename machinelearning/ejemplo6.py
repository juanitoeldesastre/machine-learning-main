import pandas as pd
import numpy as np
# Usando Pandas para leer el CSV
df = pd.read_csv('archivo.csv')
print("DataFrame con Pandas:")
print(df.head())
# Usando NumPy para leer el CSV
data = np.genfromtxt('archivo.csv', delimiter=',', skip_header=1,dtype=int)
print("Array con NumPy:")
print(data)