from tensorflow import keras
model = keras.models.load_model('mejor_modelo_keras.keras')
model.summary()
