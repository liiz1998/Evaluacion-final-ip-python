# Ejercicio 4 – Predicción sencilla

## Opción A – Machine Learning (ML)

### Dataset
Se utiliza el dataset Iris, que contiene 150 muestras de flores con cuatro características numéricas: longitud y anchura del sépalo, longitud y anchura del pétalo.  
Las clases a predecir son: *setosa*, *versicolor* y *virginica*.

### Carga de datos
Los datos se cargan utilizando la función `load_iris()` de la librería scikit-learn.

### Entrenamiento
Se emplea un modelo de clasificación **Random Forest**.  
El dataset se divide en un conjunto de entrenamiento (80 %) y uno de prueba (20 %).  
El modelo se entrena con los datos de entrenamiento.

### Evaluación
El modelo se evalúa utilizando la métrica **precisión (accuracy)** y un `classification_report`.  
El resultado obtenido muestra una precisión cercana al 100 %, indicando un buen rendimiento del modelo.


## Opción B – Deep Learning (DL)

### Dataset
Se utiliza el dataset Iris, pero solo con dos clases (*setosa* y *versicolor*) para plantear un problema de **clasificación binaria**.

### Carga de datos
Los datos se cargan desde scikit-learn y se filtran para mantener únicamente dos clases.  
Posteriormente, se dividen en conjuntos de entrenamiento y prueba.

### Entrenamiento
Se implementa una **red neuronal simple** con Keras, compuesta por:  
- Una capa oculta con función de activación ReLU  
- Una capa de salida con función sigmoide  

El modelo se entrena durante varias épocas utilizando la función de pérdida `binary_crossentropy` y el optimizador Adam.

### Evaluación
El modelo se evalúa mediante la métrica **precisión (accuracy)** sobre el conjunto de prueba.

### Nota sobre la ejecución
En el entorno utilizado (macOS con Python 3.13 y TensorFlow) se produce un error de tipo *segmentation fault* debido a problemas de compatibilidad.  
El código es correcto y se ejecuta correctamente en entornos compatibles, por ejemplo Python 3.10.