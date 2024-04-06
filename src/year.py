import pandas as pd
import matplotlib.pyplot as plt

# Lee el archivo CSV
df = pd.read_csv("wiki_movie_plots_deduped.csv")

# Cuenta la cantidad de películas por año
movies_per_year = df.groupby('Release Year').size()

# Crea el gráfico
plt.figure(figsize=(10, 6))
movies_per_year.plot(kind='bar', color='skyblue')
plt.title('Cantidad de películas por año')
plt.xlabel('Año de lanzamiento')
plt.ylabel('Cantidad de películas')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Ajusta la leyenda de los años
plt.xticks(range(0, len(movies_per_year), 10), movies_per_year.index[::10])

# Muestra el gráfico
plt.tight_layout()
plt.show()
