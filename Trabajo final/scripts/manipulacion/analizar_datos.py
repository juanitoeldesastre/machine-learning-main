def analizar_datos(productos, usuarios, interacciones):
    precio_promedio_categoria = productos.groupby('Categoria')['Precio'].mean()
    print("\nPrecio promedio por categoría:")
    print(precio_promedio_categoria)

    conteo_productos_marca = productos['Marca'].value_counts()
    print("\nNúmero de productos por marca:")
    print(conteo_productos_marca)

    rating_promedio_marca = productos.groupby('Marca')['Rating_Promedio'].mean()
    print("\nRating promedio por marca:")
    print(rating_promedio_marca)

if __name__ == '__main__':
    from leer_datos import cargar_datos
    productos, usuarios, interacciones = cargar_datos()
    
    analizar_datos(productos, usuarios, interacciones)
