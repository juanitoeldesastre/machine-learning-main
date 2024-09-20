import pandas as pd

df = pd.read_csv('datos.csv')
print("Datos cargados del archivo CSV:")
print(df.head())

grupo_ciudad = df.groupby('ciudad')['salario'].mean()
print("\nPromedio de salario por ciudad:")
print(grupo_ciudad)

df2 = pd.DataFrame({
    'id': [1, 2, 3],
    'departamento': ['Ventas', 'Marketing', 'Finanzas']
})

df_merge = pd.merge(df, df2, on='id')
print("\nDatos combinados entre los DataFrames:")
print(df_merge)

df_clean = df.dropna(subset=['edad'])
print("\nDatos después de eliminar filas con valores nulos en 'edad':")
print(df_clean)

stats = df.describe()
print("\nEstadísticas descriptivas de los datos:")
print(stats)
