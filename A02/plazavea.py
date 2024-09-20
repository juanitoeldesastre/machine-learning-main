import csv

# Datos de productos de tecnología
Tech = [
    {"Nombre": "Smartphone Galaxy S21", "Marca": "Samsung", "Precio Lista": 3999.90, "Precio Online": 3799.90, "Precio Oh": 3599.90},
    {"Nombre": "Laptop MacBook Air M1", "Marca": "Apple", "Precio Lista": 5999.90, "Precio Online": 5799.90, "Precio Oh": 5499.90},
    {"Nombre": "Televisor OLED 55'", "Marca": "LG", "Precio Lista": 5999.90, "Precio Online": 5899.90, "Precio Oh": 5599.90},
    {"Nombre": "Smartwatch Versa 3", "Marca": "Fitbit", "Precio Lista": 1299.90, "Precio Online": 1199.90, "Precio Oh": 1099.90},
    {"Nombre": "Tablet Galaxy Tab S7", "Marca": "Samsung", "Precio Lista": 2999.90, "Precio Online": 2899.90, "Precio Oh": 2699.90},
    {"Nombre": "Cámara Reflex D5600", "Marca": "Nikon", "Precio Lista": 3299.90, "Precio Online": 3099.90, "Precio Oh": 2899.90},
    {"Nombre": "Consola PS5", "Marca": "Sony", "Precio Lista": 3499.90, "Precio Online": 3399.90, "Precio Oh": 3299.90},
    {"Nombre": "Auriculares WH-1000XM4", "Marca": "Sony", "Precio Lista": 1399.90, "Precio Online": 1299.90, "Precio Oh": 1199.90},
    {"Nombre": "Monitor Gaming 27'", "Marca": "Acer", "Precio Lista": 1999.90, "Precio Online": 1899.90, "Precio Oh": 1799.90},
    {"Nombre": "Impresora Multifuncional", "Marca": "HP", "Precio Lista": 899.90, "Precio Online": 799.90, "Precio Oh": 699.90},
    {"Nombre": "Mouse Inalámbrico MX", "Marca": "Logitech", "Precio Lista": 299.90, "Precio Online": 279.90, "Precio Oh": 259.90},
    {"Nombre": "Teclado Mecánico RGB", "Marca": "Corsair", "Precio Lista": 499.90, "Precio Online": 479.90, "Precio Oh": 449.90},
    {"Nombre": "Parlante Bluetooth", "Marca": "JBL", "Precio Lista": 699.90, "Precio Online": 679.90, "Precio Oh": 649.90},
    {"Nombre": "Laptop IdeaPad 3", "Marca": "Lenovo", "Precio Lista": 2699.90, "Precio Online": 2599.90, "Precio Oh": 2399.90},
    {"Nombre": "Smart TV 43'", "Marca": "Hisense", "Precio Lista": 1699.90, "Precio Online": 1599.90, "Precio Oh": 1499.90},
    {"Nombre": "Tablet iPad 10.2'", "Marca": "Apple", "Precio Lista": 2499.90, "Precio Online": 2399.90, "Precio Oh": 2299.90},
    {"Nombre": "Router WiFi 6", "Marca": "TP-Link", "Precio Lista": 499.90, "Precio Online": 479.90, "Precio Oh": 459.90},
    {"Nombre": "Disco Duro Externo 1TB", "Marca": "Seagate", "Precio Lista": 309.90, "Precio Online": 279.90, "Precio Oh": 259.90},
    {"Nombre": "Laptop Gaming ROG", "Marca": "Asus", "Precio Lista": 5999.90, "Precio Online": 5799.90, "Precio Oh": 5699.90},
    {"Nombre": "Smartphone iPhone 13", "Marca": "Apple", "Precio Lista": 4799.90, "Precio Online": 4699.90, "Precio Oh": 4499.90},
]

archivo_csv = "plazavea.csv"

with open(archivo_csv, mode='w', newline='', encoding='utf-8') as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=["Nombre", "Marca", "Precio Lista", "Precio Online", "Precio Oh"])
    
    escritor.writeheader()

    escritor.writerows(Tech)

print(f"Archivo '{archivo_csv}' generado con éxito.")
