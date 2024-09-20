import pandas as pd

df = pd.read_csv('plazavea.csv')

print("1. Los 10 primeros productos:")
print(df.head(10))
print("\n")

producto_menor = df.loc[df['Precio Lista'].idxmin()]
print("2. Producto con menor precio lista:")
print(f"Nombre: {producto_menor['Nombre']}")
print(f"Marca: {producto_menor['Marca']}")
print(f"Precio Lista: {producto_menor['Precio Lista']}")
print("\n")

mayor_precio_oh = df.loc[df['Precio Oh'].idxmax()]
print("3. Producto con mayor precio Oh:")
print(f"Nombre: {mayor_precio_oh['Nombre']}")
print(f"Marca: {mayor_precio_oh['Marca']}")
print(f"Precio Oh: {mayor_precio_oh['Precio Oh']}")
print("\n")

promedio = df['Precio Online'].mean()
print("4. Precio online promedio de todos los productos:")
print(f"Precio online promedio: {promedio:.2f}")