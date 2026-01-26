# OSINT: Detector de Brechas de Seguridad con IA

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)
![Model](https://img.shields.io/badge/Model-CatBoost-orange.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

Esta herramienta es una aplicación web interactiva que predice la probabilidad de que un perfil de usuario sufra una **filtración de datos (Data Breach)** basándose en patrones de seguridad y datos OSINT (Open Source Intelligence).

---

## Características

* **Predicción con CatBoost:** Utiliza uno de los algoritmos más potentes del mercado para datos tabulares, optimizado para detectar patrones complejos.
* **Análisis Geográfico Inteligente:** El modelo ha sido entrenado agrupando localizaciones por **País**, permitiendo una generalización más robusta que por ciudades individuales.
* **Factores de Riesgo:** Analiza variables críticas como:
    * Cargo laboral (*Job Title*).
    * Fortaleza de la contraseña (calculada algorítmicamente).
    * Exposición en **Pastebin** (el factor de riesgo más crítico).
    * Ubicación geográfica.
* **Interfaz Amigable:** Construida con Streamlit para una experiencia de usuario fluida y visual.

---

## Cómo funciona el Modelo (Data Science)

El núcleo del proyecto es un flujo de trabajo de Machine Learning que incluye:

### 1. Preprocesamiento de Datos
* **Limpieza de Localización:** Se transformó la columna original `Location` (ej: "Madrid, Spain") para extraer únicamente el **País**. Esto redujo la dimensionalidad y mejoró la capacidad del modelo para encontrar patrones regionales.
* **Codificación:** Uso de `OneHotEncoder` para transformar variables categóricas (Trabajo, País) en vectores numéricos.
* **Ingeniería de Características:** Cálculo automático de la fortaleza de la contraseña basada en longitud y complejidad.

### 2. El Modelo
Se probaron varios algoritmos (Decision Trees, Random Forest, Logistic Regression Balanceado) y finalmente se implementó un modelo capaz de manejar el desbalanceo de clases (pocos usuarios hackeados vs. muchos seguros), optimizando la métrica de **Recall** para no ignorar las amenazas reales.

* **Dataset utilizado:** [OSINT Public Profiles](https://www.kaggle.com/datasets/alliot032/osint-public-profiles-dataset).
* **Factor más determinante:** La presencia del correo en *Pastebin* demostró ser el predictor más fuerte de una brecha de seguridad.

---

## Acceso y Ejecución

Tienes dos formas de utilizar esta herramienta: acceder a la versión desplegada en la nube o ejecutar el código en tu propio ordenador.

### Opción A: Versión Online (Recomendada)
¡La aplicación está desplegada y lista para usar! No necesitas instalar nada.

**[Haz clic aquí para abrir el Detector de Brechas](https://assignmentbrief-appliedmachinelearning.streamlit.app/)**

*(Nota: Si la aplicación se ha "dormido" por inactividad, dale unos segundos para que arranque de nuevo).*

---
### Opción B: Instalación Local
Si prefieres examinar el código, modificarlo o ejecutarlo en tu máquina, sigue estos pasos:

#### 1. Clonar el repositorio
Descarga el código fuente a tu ordenador:
```bash
git clone [https://github.com/JorgeMV-MSMK/Assignment_Brief-Applied_Machine_Learning.git](https://github.com/JorgeMV-MSMK/Assignment_Brief-Applied_Machine_Learning.git)
cd Assignment_Brief-Applied_Machine_Learning
```
#### 2. Instalar dependencias
Asegúrate de tener Python instalado. Navega a la carpeta del proyecto y ejecuta el siguiente comando para instalar las librerías necesarias:

```bash
pip install -r requirements.txt
```

#### 3. Ejecutar la aplicación
Una vez instaladas las dependencias, inicia la interfaz web con el comando:
```bash
streamlit run app.py
```
Automáticamente se abrirá una pestaña en tu navegador predeterminado (normalmente en `http://localhost:8501`) mostrando la herramienta.

---

## Nota Legal y Ética
Esta herramienta ha sido creada con fines educativos y de concienciación sobre ciberseguridad. Los datos utilizados para el entrenamiento provienen de un dataset público ficticio. La predicción es una estimación estadística y no una auditoría de seguridad real. No introduzca credenciales reales sensibles en la aplicación.
