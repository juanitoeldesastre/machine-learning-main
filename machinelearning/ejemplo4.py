import pandas as pd
# Leer el archivo CSV en un DataFrame de Pandas
df = pd.read_csv('notas_paquetes_ml_python.csv',sep=";")
# Mostrar las primeras 5 filas del DataFrame
print(df.head())
