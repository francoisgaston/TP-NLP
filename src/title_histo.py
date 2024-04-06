import pandas as pd
import matplotlib.pyplot as plt

# Lee el archivo CSV
df = pd.read_csv("wiki_movie_plots_deduped.csv")

# Calcula la cantidad de palabras por título
df['Title_word_count'] = df['Title'].apply(lambda x: len(x.split()))

# Crea el histograma
plt.figure(figsize=(10, 6))
plt.hist(df['Title_word_count'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histograma de cantidad de palabras por título de película')
plt.xlabel('Cantidad de palabras')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Muestra el histograma
plt.tight_layout()
plt.show()