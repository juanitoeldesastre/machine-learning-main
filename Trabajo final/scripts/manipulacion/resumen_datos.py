import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def resumen_datos():
    productos = pd.read_csv('../../data/productos.csv')
    usuarios = pd.read_csv('../../data/usuarios.csv')
    interacciones = pd.read_csv('../../data/interacciones.csv')

    print("Productos:")
    print(productos.head())

    print("\nUsuarios:")
    print(usuarios.head())

    print("\nInteracciones:")
    print(interacciones.head())

    plt.figure(figsize=(12, 6))
    sns.countplot(y='Ubicación', data=usuarios, hue='Ubicación', palette='coolwarm')
    plt.title('Distribución de Usuarios por Ubicación')
    plt.savefig('distribucion_usuarios_ubicacion.png')  
    plt.close()

    plt.figure(figsize=(12, 6))
    sns.countplot(x='Marca', data=productos, palette='Set2')
    plt.title('Número de Productos por Marca')
    plt.xticks(rotation=45)
    plt.savefig('productos_por_marca.png') 
    plt.close()

if __name__ == '__main__':
    resumen_datos()
