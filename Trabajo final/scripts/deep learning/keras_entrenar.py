import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  

from keras.models import Sequential
from keras.layers import Dense, Dropout, BatchNormalization
from keras.callbacks import EarlyStopping, ModelCheckpoint
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

def crear_modelo_keras():
    interacciones = pd.read_csv('../../data/interacciones.csv')
    interacciones['Compra'] = interacciones['Acción'].apply(lambda x: 1 if x == 'Compra' else 0)
    
    X = interacciones[['ID_Usuario', 'ID_Producto']]
    y = interacciones['Compra']
    
    column_transformer = ColumnTransformer(
        transformers=[('onehot', OneHotEncoder(handle_unknown='ignore'), ['ID_Usuario', 'ID_Producto'])],
        remainder='passthrough'
    )
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    X_train = column_transformer.fit_transform(X_train).toarray()
    X_test = column_transformer.transform(X_test).toarray()
    
    scaler = StandardScaler(with_mean=False)
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    modelo = Sequential([
        Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
        BatchNormalization(),
        Dropout(0.3),
        Dense(32, activation='relu'),
        BatchNormalization(),
        Dropout(0.3),
        Dense(1, activation='sigmoid')
    ])
    
    modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
    checkpoint = ModelCheckpoint('mejor_modelo_keras.keras', save_best_only=True)
    
    historial = modelo.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, 
                           callbacks=[early_stopping, checkpoint], verbose=1)
    
    loss, accuracy = modelo.evaluate(X_test, y_test, verbose=0)
    print(f'Precisión del modelo en conjunto de prueba: {accuracy:.2f}')
    
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(historial.history['loss'], label='Pérdida entrenamiento')
    plt.plot(historial.history['val_loss'], label='Pérdida validación')
    plt.title('Pérdida durante el entrenamiento')
    plt.xlabel('Épocas')
    plt.ylabel('Pérdida')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(historial.history['accuracy'], label='Precisión entrenamiento')
    plt.plot(historial.history['val_accuracy'], label='Precisión validación')
    plt.title('Precisión durante el entrenamiento')
    plt.xlabel('Épocas')
    plt.ylabel('Precisión')
    plt.legend()
    
    plt.savefig('entrenamiento_grafica_keras.png')
    print("La gráfica se ha guardado como 'entrenamiento_grafica_keras.png'")

if __name__ == '__main__':
    crear_modelo_keras()