import pandas as pd
import random
from faker import Faker

fake = Faker(['es_MX', 'es_CO', 'es_AR', 'es_CL'])

categorias = ["Tecnología", "Electrónica", "Ropa", "Gaming", "Electrohogar"]
marcas = ["LG", "Sony", "HA", "Akita", "GE", "Samsung", "Nike", "Apple", "Xiaomi", "Panasonic"]
acciones = ["Compra", "Vista", "Añadir a lista de deseos", "Carrito"]
monedas = ["MXN", "COP", "ARS", "CLP"]

def generar_csv_productos(n):
    productos = []
    for i in range(1, n + 1):
        producto = {
            "ID_Producto": i,
            "Categoria": random.choice(categorias),
            "Precio": round(random.uniform(10, 1000), 2),
            "Moneda": random.choice(monedas),
            "Marca": random.choice(marcas),
            "Descripción": fake.catch_phrase(),
            "Rating_Promedio": round(random.uniform(1, 5), 1)
        }
        productos.append(producto)
    df = pd.DataFrame(productos)
    df.to_csv('productos.csv', index=False)
    print("CSV de productos generado.")

def generar_csv_usuarios(n):
    usuarios = []
    for i in range(1, n + 1):
        usuario = {
            "ID_Usuario": i,
            "Nombre": fake.name(),
            "Edad": random.randint(18, 65),
            "Género": random.choice(["Masculino", "Femenino"]),
            "Ubicación": fake.city(),  # Solo genera la ciudad
            "Preferencias": ", ".join(random.sample(categorias, random.randint(1, 3))),
            "Likes": random.sample(range(1, 101), random.randint(1, 5))
        }
        usuarios.append(usuario)
    df = pd.DataFrame(usuarios)
    df.to_csv('usuarios.csv', index=False)
    print("CSV de usuarios generado.")

def generar_csv_interacciones(n_usuarios, n_productos, n_interacciones):
    interacciones = []
    for i in range(1, n_interacciones + 1):
        interaccion = {
            "ID_Interacción": i,
            "ID_Usuario": random.randint(1, n_usuarios),
            "ID_Producto": random.randint(1, n_productos),
            "Acción": random.choice(acciones),
            "Fecha": fake.date_this_year(),
            "Calificación": random.choice([0, random.randint(1, 5)])  
        }
        interacciones.append(interaccion)
    df = pd.DataFrame(interacciones)
    df.to_csv('interacciones.csv', index=False)
    print("CSV de interacciones generado.")

n_productos = 100  
n_usuarios = 50  
n_interacciones = 500 

generar_csv_productos(n_productos)
generar_csv_usuarios(n_usuarios)
generar_csv_interacciones(n_usuarios, n_productos, n_interacciones)
