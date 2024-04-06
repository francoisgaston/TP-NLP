import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lee el archivo CSV
df = pd.read_csv("wiki_movie_plots_deduped.csv")

# Separa los géneros en una lista y convierte a minúsculas
df['Genre'] = df['Genre'].str.lower().str.split(', ')

# Filtra los datos para incluir solo los géneros especificados
selected_genres = ['drama', 'comedy', 'action', 'romance', 'horror', 'thriller', 'western']
filtered_df = df[df['Genre'].apply(lambda x: any(genre in selected_genres for genre in x))]

# Expande el DataFrame para tener una fila para cada combinación de película y género
expanded_df = filtered_df.explode('Genre')

# Calcula la cantidad de palabras por trama
expanded_df['Plot_word_count'] = expanded_df['Plot'].apply(lambda x: len(x.split()))

# Configura el estilo de seaborn
sns.set(style="whitegrid")

# Crea la función de densidad de probabilidad (PDF) para cada género
plt.figure(figsize=(12, 8))
for genre in selected_genres:
    sns.kdeplot(data=expanded_df[expanded_df['Genre'] == genre]['Plot_word_count'], label=genre.capitalize(), fill=True)

plt.title('Función de densidad de probabilidad de cantidad de palabras en el plot por género')
plt.xlabel('Cantidad de palabras en el plot')
plt.ylabel('Densidad de probabilidad')
plt.legend(title='Género')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Muestra la función de densidad de probabilidad por género
plt.tight_layout()
plt.show()
