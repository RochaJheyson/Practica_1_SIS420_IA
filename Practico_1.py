# Importar las librerías necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generar valores de altura y masa aleatorios y controlados
np.random.seed(123)  # Fijar una semilla para asegurar que los resultados sean reproducibles
alturas = np.random.uniform(1.4, 2.0, 100)  # Crear 100 alturas aleatorias entre 1.4m y 2.0m
masas = []  # Lista para almacenar las masas generadas

# Bucle para calcular masas controladas según la altura
for altura in alturas:
    # Calcular el rango de masa usando un IMC saludable (18.5 a 24.9)
    masa_min = 18.5 * (altura ** 2)  # Masa mínima según IMC de 18.5
    masa_max = 24.9 * (altura ** 2)  # Masa máxima según IMC de 24.9
    # Generar una masa aleatoria dentro del rango calculado
    masa = np.random.uniform(masa_min, masa_max)
    masas.append(masa)  # Agregar la masa a la lista de masas

# Crear un DataFrame con los datos de altura y masa
datos = pd.DataFrame({
    'Altura (m)': alturas,
    'Masa (kg)': masas
})

# Calcular la pendiente (m) y la intersección (b) de la línea de ajuste y = mx + b
x = datos['Altura (m)']
y = datos['Masa (kg)']
pendiente = np.sum((x - np.mean(x)) * (y - np.mean(y))) / np.sum((x - np.mean(x)) ** 2)
interseccion = np.mean(y) - pendiente * np.mean(x)

# Crear los valores de y basados en la ecuación de la línea
y_ajustada = pendiente * x + interseccion

# Visualizar los datos generados y la línea de ajuste
plt.scatter(datos['Altura (m)'], datos['Masa (kg)'], color='green', label='Datos Observados')
plt.plot(x, y_ajustada, color='orange', label='Línea de Ajuste')
plt.title('Relación entre Altura y Masa con Línea de Ajuste')
plt.xlabel('Altura (m)')
plt.ylabel('Masa (kg)')
plt.legend()
plt.show()
