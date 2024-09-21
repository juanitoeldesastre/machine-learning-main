import pandas as pd
import numpy as np

# Definir los datos simulados para ventas
np.random.seed(42)

# Fechas del año 2023 (simulación de 12 meses)
fechas = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')

# Productos y categorías simuladas
productos = ['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Teclado', 'Ratón']
categorias = ['Electrónica', 'Electrónica', 'Electrónica', 'Periféricos', 'Periféricos', 'Periféricos']

# Generar un DataFrame con datos aleatorios de ventas
data_ventas = {
    'Fecha': np.random.choice(fechas, size=500),
    'Producto': np.random.choice(productos, size=500),
    'Categoría': np.random.choice(categorias, size=500),
    'Cantidad Vendida': np.random.randint(1, 10, size=500),
    'Precio Unitario': np.random.uniform(50, 1500, size=500).round(2),  # Precios entre 50 y 1500
    'Costo Unitario': np.random.uniform(30, 1200, size=500).round(2),  # Costos entre 30 y 1200
    'Método de Pago': np.random.choice(['Tarjeta de crédito', 'Efectivo', 'Transferencia', 'PayPal'], size=500)
}

df_ventas = pd.DataFrame(data_ventas)

# Calcular el total de ventas (Precio Unitario * Cantidad Vendida)
df_ventas['Total Venta'] = df_ventas['Cantidad Vendida'] * df_ventas['Precio Unitario']

# Calcular el costo total (Costo Unitario * Cantidad Vendida)
df_ventas['Total Costo'] = df_ventas['Cantidad Vendida'] * df_ventas['Costo Unitario']

# Calcular la ganancia (Total Venta - Total Costo)
df_ventas['Ganancia'] = df_ventas['Total Venta'] - df_ventas['Total Costo']

# Mostrar las primeras filas del DataFrame simulado
df_ventas.head()
