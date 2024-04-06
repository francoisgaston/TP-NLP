import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Lee el archivo CSV
df = pd.read_csv("wiki_movie_plots_deduped.csv")

# Calcula la cantidad de palabras por trama
df['Plot_word_count'] = df['Plot'].apply(lambda x: len(x.split()))

# Calcula la función de distribución acumulada (CDF)
cdf = np.arange(1, len(df['Plot_word_count']) + 1) / len(df['Plot_word_count'])

# Crea la curva de distribución acumulada
plt.figure(figsize=(10, 6))
plt.plot(np.sort(df['Plot_word_count']), cdf, color='skyblue')
plt.title('Curva de distribución acumulada de cantidad de palabras por trama de película')
plt.xlabel('Cantidad de palabras')
plt.ylabel('Probabilidad acumulada')
plt.grid(axis='both', linestyle='--', alpha=0.7)

# Muestra la curva de distribución acumulada
plt.tight_layout()
plt.show()