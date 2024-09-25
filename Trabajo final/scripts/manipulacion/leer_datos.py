import pandas as pd

def cargar_datos():
    productos = pd.read_csv('../../data/productos.csv')
    usuarios = pd.read_csv('../../data/usuarios.csv')
    interacciones = pd.read_csv('../../data/interacciones.csv')
    
    print("Productos:")
    print(productos.head())
    print("\nUsuarios:")
    print(usuarios.head())
    print("\nInteracciones:")
    print(interacciones.head())

    return productos, usuarios, interacciones

if __name__ == '__main__':
    productos, usuarios, interacciones = cargar_datos()
