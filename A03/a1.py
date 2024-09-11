# Paso 1: Importar las bibliotecas necesarias
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

# Paso 2: Cargar el conjunto de datos de diabetes
diabetes = load_diabetes()
X = diabetes.data  # Características médicas
y = (diabetes.target > diabetes.target.mean()).astype(int)  # Etiqueta binaria (1 si el nivel de riesgo es alto, 0 si es bajo)

# Paso 3: Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 4: Escalar las características
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Paso 5: Crear y entrenar el modelo (usando regresión logística)
model = LogisticRegression()
model.fit(X_train, y_train)

# Paso 6: Hacer predicciones sobre el conjunto de prueba
y_pred = model.predict(X_test)

# Paso 7: Evaluar la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy * 100:.2f}%")

# Paso 8: Predecir con nuevos datos (características de nuevos pacientes)
X_new = np.array([
    [0.03807591,  0.05068012,  0.06169621,  0.02187235, -0.0442235, -0.03482076, -0.04340085, -0.00259226,  0.01990749, -0.01764613],
    [-0.00188202, -0.04464164,  0.05068012,  0.01103904,  0.01549073,  0.0123073,  0.02377494, -0.03949338, -0.06833339, -0.09220405],
    [0.08529891, -0.04464164,  0.04552903, -0.03734449,  0.07441156,  0.05822365,  0.03444344,  0.02377494, -0.01811827,  0.04448548]
])

# Escalar los nuevos datos utilizando el mismo escalador
X_new_scaled = scaler.transform(X_new)

# Hacer predicciones con los nuevos datos
predicciones = model.predict(X_new_scaled)

# Mostrar los resultados
for i, pred in enumerate(predicciones):
    resultado = "Diabetes" if pred == 1 else "No Diabetes"
    print(f"Paciente {i+1}: {resultado}")
