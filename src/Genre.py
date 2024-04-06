import pandas as pd
import matplotlib.pyplot as plt

# Lee el archivo CSV
df = pd.read_csv("wiki_movie_plots_deduped.csv")

# Separa los géneros en una lista
genres = df['Genre'].str.split(', ')

# Cuenta las ocurrencias de cada género
genre_counts = pd.Series([genre for sublist in genres for genre in sublist]).value_counts()

# Filtra los géneros para excluir "Unknown" y toma los primeros 7
top_genres = genre_counts[genre_counts.index != 'unknown'].head(10)

# Crea el gráfico
plt.figure(figsize=(12, 6))
top_genres.plot(kind='bar', color='skyblue')
plt.title('Top 7 Géneros de Películas (sin "Unknown")')
plt.xlabel('Género')
plt.ylabel('Cantidad de Películas')
plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para una mejor visualización

# Muestra el gráfico
plt.tight_layout()
plt.show()