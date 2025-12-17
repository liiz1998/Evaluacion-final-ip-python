# dl_simple.py
# Clasificación binaria usando una red neuronal simple con Keras

# 1. Importar librerías
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# 2. Cargar datos y seleccionar solo dos clases (setosa y versicolor)
iris = load_iris()
X = iris.data
y = iris.target

# Filtrar solo clases 0 y 1 para clasificación binaria
mask = y != 2
X = X[mask]
y = y[mask]

# Convertir etiquetas a 0 y 1 (binarias)
y = y.reshape(-1, 1)

# 3. Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Crear modelo secuencial simple
model = Sequential([
    Dense(8, input_shape=(4,), activation='relu'),  # Capa oculta con 8 neuronas
    Dense(1, activation='sigmoid')                  # Capa de salida para clasificación binaria
])

# 5. Compilar modelo
model.compile(optimizer=Adam(learning_rate=0.01),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# 6. Entrenar modelo
history = model.fit(X_train, y_train, epochs=50, batch_size=4, verbose=0)

# 7. Evaluar modelo
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Accuracy en test set: {accuracy:.2f}")

# 8. Hacer predicciones
y_pred = model.predict(X_test)
y_pred_labels = (y_pred > 0.5).astype(int)

print("Predicciones del test set:")
print(y_pred_labels.T)
print("Etiquetas reales del test set:")
print(y_test.T)

