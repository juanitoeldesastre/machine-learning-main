import numpy as np
import matplotlib.pyplot as plt

# Función para simular lanzamientos de moneda
def simular_moneda(n_lanzamientos):
    # 0 es cara, 1 es cruz
    resultados = np.random.choice([0, 1], size=n_lanzamientos)
    caras = np.sum(resultados == 0)
    cruces = np.sum(resultados == 1)
    
    print(f"Lanzamientos de moneda: {n_lanzamientos}")
    print(f"Caras: {caras} ({caras/n_lanzamientos*100:.2f}%)")
    print(f"Cruces: {cruces} ({cruces/n_lanzamientos*100:.2f}%)")
    
    # Visualización
    plt.bar(['Caras', 'Cruces'], [caras, cruces], color=['blue', 'green'])
    plt.title(f"Simulación de {n_lanzamientos} lanzamientos de moneda")
    plt.show()

# Función para simular tiradas de un dado
def simular_dado(n_tiradas):
    resultados = np.random.choice([1, 2, 3, 4, 5, 6], size=n_tiradas)
    frecuencias = np.bincount(resultados)[1:]  # Contamos las ocurrencias de cada número
    
    print(f"Tiradas de dado: {n_tiradas}")
    for i in range(6):
        print(f"Número {i+1}: {frecuencias[i]} ({frecuencias[i]/n_tiradas*100:.2f}%)")
    
    # Visualización
    plt.bar([1, 2, 3, 4, 5, 6], frecuencias, color='purple')
    plt.title(f"Simulación de {n_tiradas} tiradas de dado")
    plt.show()

# Función para simular extracción de cartas de una baraja (sin reemplazo)
def simular_cartas(n_extracciones):
    baraja = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4  # Baraja de 52 cartas
    resultados = np.random.choice(baraja, size=n_extracciones, replace=False)  # Sin reemplazo
    unique, counts = np.unique(resultados, return_counts=True)
    
    print(f"Extracciones de cartas: {n_extracciones}")
    for carta, count in zip(unique, counts):
        print(f"Carta {carta}: {count} ({count/n_extracciones*100:.2f}%)")
    
    # Visualización
    plt.bar(unique, counts, color='orange')
    plt.title(f"Simulación de {n_extracciones} extracciones de cartas")
    plt.show()

# Ejecución de simulaciones
simular_moneda(10000)   # Simulación de 10,000 lanzamientos de moneda
simular_dado(10000)     # Simulación de 10,000 tiradas de dado
simular_cartas(10)      # Simulación de 10 extracciones de cartas (sin reemplazo)
