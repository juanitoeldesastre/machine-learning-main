import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import numpy as np

diabetes = load_diabetes()
X = diabetes.data  # Características médicas
y = (diabetes.target > diabetes.target.mean()).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.float32).unsqueeze(1)  # Agregar una dimensión para PyTorch
y_test_tensor = torch.tensor(y_test, dtype=torch.float32).unsqueeze(1)

class LogisticRegressionModel(nn.Module):
    def __init__(self, input_size):
        super(LogisticRegressionModel, self).__init__()
        self.linear = nn.Linear(input_size, 1)
    
    def forward(self, x):
        return torch.sigmoid(self.linear(x))

input_size = X_train.shape[1]
model = LogisticRegressionModel(input_size)

criterion = nn.BCELoss()  # Binary Cross Entropy Loss
optimizer = optim.SGD(model.parameters(), lr=0.01)

num_epochs = 100
for epoch in range(num_epochs):
    outputs = model(X_train_tensor)
    loss = criterion(outputs, y_train_tensor)
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

with torch.no_grad():
    y_pred_train = model(X_train_tensor)
    y_pred_train = (y_pred_train >= 0.5).float()
    train_accuracy = (y_pred_train.eq(y_train_tensor).sum() / y_train_tensor.shape[0]).item()

    y_pred_test = model(X_test_tensor)
    y_pred_test = (y_pred_test >= 0.5).float()
    test_accuracy = (y_pred_test.eq(y_test_tensor).sum() / y_test_tensor.shape[0]).item()

print(f'Precisión en el conjunto de entrenamiento: {train_accuracy * 100:.2f}%')
print(f'Precisión en el conjunto de prueba: {test_accuracy * 100:.2f}%')

X_new = np.array([
    [0.03807591,  0.05068012,  0.06169621,  0.02187235, -0.0442235, -0.03482076, -0.04340085, -0.00259226,  0.01990749, -0.01764613],
    [-0.00188202, -0.04464164,  0.05068012,  0.01103904,  0.01549073,  0.0123073,  0.02377494, -0.03949338, -0.06833339, -0.09220405],
    [0.08529891, -0.04464164,  0.04552903, -0.03734449,  0.07441156,  0.05822365,  0.03444344,  0.02377494, -0.01811827,  0.04448548]
])

X_new_scaled = scaler.transform(X_new)
X_new_tensor = torch.tensor(X_new_scaled, dtype=torch.float32)

with torch.no_grad():
    predicciones = model(X_new_tensor)
    predicciones = (predicciones >= 0.5).float()

for i, pred in enumerate(predicciones):
    resultado = "Diabetes" if pred == 1 else "No Diabetes"
    print(f"Paciente {i+1}: {resultado}")
