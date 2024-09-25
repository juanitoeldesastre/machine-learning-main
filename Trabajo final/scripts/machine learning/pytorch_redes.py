import torch
import torch.nn as nn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class RedNeuronal(nn.Module):
    def __init__(self):
        super(RedNeuronal, self).__init__()
        self.fc1 = nn.Linear(2, 16)  
        self.fc2 = nn.Linear(16, 8)
        self.fc3 = nn.Linear(8, 1)  

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        return x

def predecir_compras():
    interacciones = pd.read_csv('../../data/interacciones.csv')
    interacciones['Compra'] = interacciones['Acción'].apply(lambda x: 1 if x == 'Compra' else 0)

    X = interacciones[['ID_Usuario', 'ID_Producto']]
    y = interacciones['Compra']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    X_train = torch.FloatTensor(X_train)
    y_train = torch.FloatTensor(y_train.values)
    X_test = torch.FloatTensor(X_test)
    y_test = torch.FloatTensor(y_test.values)

    modelo = RedNeuronal()
    criterio = nn.BCELoss()
    optimizador = torch.optim.Adam(modelo.parameters(), lr=0.001)
    epochs = 100
    for epoch in range(epochs):
        modelo.train()
        optimizador.zero_grad()
        salida = modelo(X_train)
        loss = criterio(salida.squeeze(), y_train)
        loss.backward()
        optimizador.step()

        if epoch % 10 == 0:
            print(f'Epoch {epoch}, Pérdida: {loss.item():.4f}')

    modelo.eval()
    with torch.no_grad():
        predicciones = modelo(X_test).squeeze()
        predicciones = (predicciones > 0.5).float()
        accuracy = (predicciones == y_test).sum().item() / y_test.size(0)
        print(f'Precisión de la red neuronal: {accuracy:.2f}')

if __name__ == '__main__':
    predecir_compras()
