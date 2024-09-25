import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np

def clustering_productos():
    productos = pd.read_csv('../../data/productos.csv')

    X = productos[['Precio', 'Rating_Promedio']]

    if X.isnull().sum().any():
        print("Existen valores nulos en el dataset. Por favor, limpia los datos.")
        return
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    sse = []
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X_scaled)
        sse.append(kmeans.inertia_)
    
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, 11), sse, marker='o')
    plt.title('Método del codo para determinar el número óptimo de clusters')
    plt.xlabel('Número de clusters')
    plt.ylabel('SSE (Inercia)')
    plt.show()

    kmeans = KMeans(n_clusters=3, random_state=42)
    productos['Cluster'] = kmeans.fit_predict(X_scaled)

    plt.figure(figsize=(10, 6))
    plt.scatter(productos['Precio'], productos['Rating_Promedio'], c=productos['Cluster'], cmap='viridis', s=50)
    centroids = scaler.inverse_transform(kmeans.cluster_centers_)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, alpha=0.75, label='Centroides')
    plt.title('Clustering de Productos basado en Precio y Rating Promedio')
    plt.xlabel('Precio')
    plt.ylabel('Rating Promedio')
    plt.legend()
    plt.show()

    print('Centroides de los clusters:')
    print(pd.DataFrame(centroids, columns=['Precio', 'Rating_Promedio']))
    
    productos.to_csv('../../data/productos_clusterizados.csv', index=False)
    print("Resultados guardados en 'productos_clusterizados.csv'.")

if __name__ == '__main__':
    clustering_productos()
