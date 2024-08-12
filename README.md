# Practica_1_SIS420_IA
Propósito del Código
El código tiene como objetivo simular datos de altura y masa (peso) para 100 individuos y analizar la relación entre estas dos variables utilizando regresión lineal. El análisis culmina en la creación de un gráfico que muestra tanto los datos generados como la línea de ajuste que mejor representa la relación entre altura y masa.

Importación de Librerías:

Se importan las librerías numpy, pandas, y matplotlib.pyplot que se utilizarán para la generación de datos, su manipulación y su visualización.
Generación de Datos Aleatorios:

Alturas: Se generan 100 valores aleatorios de alturas entre 1.4 m y 2.0 m utilizando la función np.random.uniform.
Masas (Pesos):
Para cada altura generada, se calcula un rango de masas utilizando un IMC saludable, con valores de 18.5 y 24.9.
Se genera una masa aleatoria dentro de este rango para cada altura utilizando nuevamente np.random.uniform.
Los datos de altura y masa se almacenan en listas separadas.
Creación de un DataFrame:

Las listas de alturas y masas se combinan en un DataFrame de Pandas, que facilita la manipulación y análisis de los datos.
Cálculo de la Línea de Ajuste (Regresión Lineal):

Se calcula la pendiente (m) y la intersección (b) de la línea de regresión lineal que mejor se ajusta a los datos. Esto se hace utilizando fórmulas estadísticas que comparan la relación entre los valores de altura y masa.
La fórmula y = mx + b se usa para calcular los valores ajustados (esperados) de masa en función de las alturas.
Visualización de los Resultados:

Se genera un gráfico de dispersión que muestra los pares de datos de altura y masa.
Sobre el gráfico de dispersión, se traza la línea de ajuste calculada, que representa la relación lineal entre altura y masa.
El gráfico incluye etiquetas en los ejes, un título, y una leyenda que identifica los datos y la línea de ajuste.
Resultado Final
El código produce un gráfico que visualiza la relación entre la altura y la masa de 100 individuos simulados. En este gráfico:

Los puntos azules representan las alturas y masas generadas aleatoriamente.
La línea roja muestra la tendencia general (línea de regresión) que indica cómo cambia la masa en función de la altura.
Este gráfico es una herramienta útil para entender la relación entre las dos variables y cómo se distribuyen los datos alrededor de esta relación lineal.
