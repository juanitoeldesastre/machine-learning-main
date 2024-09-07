import pandas as pd
import numpy as np
# Leer el archivo CSV en un DataFrame de Pandas
df = pd.read_csv('archivo.csv',sep=",",na_values=['NA','N/A','NULL'])
# Mostrar las primeras 5 filas del DataFrame
print(df.head())

df2 = pd.read_csv('archivo.csv',sep=",",usecols=['dni','nro_cuenta'])
print(df2.head())

print('***********************\n')
df3 = np.genfromtxt('archivo.csv',delimiter=",",skip_header=1)
print(df3)

print('***********************\n')

df4 = np.genfromtxt('archivo.csv',delimiter=",",skip_header=1,dtype=int)
print(df4)

print('***********************\n')
df5 = np.genfromtxt('archivo.csv',delimiter=",",skip_header=1,dtype=int,filling_values=0)
print(df5)

print('***********************\n')
df6 = np.genfromtxt('archivo.csv',delimiter=",",skip_header=1,dtype=None,names=True,encoding=None)
print(df6)