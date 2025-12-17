# 📘 Evaluación Final – Curso IP_IAPython_1

## 📝 Descripción
Repositorio correspondiente a la evaluación final del curso **Introducción a Python / IA Python**.  
El proyecto incluye ejercicios de Python base, Machine Learning, Deep Learning, desarrollo web frontend y planificación Scrum.

## 🛠 Tecnologías utilizadas
- Python 3.x
- scikit-learn
- TensorFlow / Keras
- HTML
- CSS
- JavaScript
- Git y GitHub

## 📂 Estructura del proyecto

```text
evaluacion-final-ip-python/
│
├─ README.md
├─ requirements.txt
├─ explicacion.md
├─ scrum.md
├─ index.html
├─ style.css
├─ script.js
└─ src/
   ├─ ml_simple.py
   ├─ dl_simple.py
   ├─ procesador.py
   ├─ usuarios.txt
   └─ usuarios_limpios.csv
```

## Cómo ejecutar el proyecto

### Scripts Python (Ejercicios 2 y 4)
Abrir una terminal en la carpeta `src` y ejecutar:

```bash
pip install -r ../requirements.txt
python ml_simple.py
python dl_simple.py
python procesador.py
```

###  Interfaz web (Ejercicio 5)
Abrir una terminal en la raíz del proyecto y ejecutar:

```bash
python3 -m http.server 8000
```

Luego abrir el navegador y acceder a:

```
http://localhost:8000/index.html
```

## 🗒 Notas
- El ejercicio de Machine Learning y Deep Learning incluye una explicación adicional en el archivo `explicacion.md`.  
- La planificación del ejercicio Scrum se encuentra documentada en `scrum.md`.  
- Los archivos generados automáticamente (como `usuarios_limpios.csv` o la base de datos `db.sqlite3`) **no se deben subir al repositorio**; se pueden regenerar al ejecutar los scripts.