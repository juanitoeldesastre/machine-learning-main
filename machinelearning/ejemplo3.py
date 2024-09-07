import pandas as pd
# Leer el archivo CSV en un DataFrame de Pandas
df = pd.read_csv('archivo.csv')
# Mostrar las primeras 5 filas del DataFrame
print(df.head(n=7))
print('la edad de el id 1 es ',df['edad'][1])