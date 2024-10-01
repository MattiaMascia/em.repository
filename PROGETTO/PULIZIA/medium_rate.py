import pandas as pd
df=pd.read_csv("C://Users//Loredana//Desktop//Academy MM//PYTHON//PROGETTO//THE-MOVIES-DATASET//ratings_small.csv",low_memory=False)

import pandas as pd

# Raggruppo i dati per 'movieId', calcolo la media delle valutazioni e conto il numero di recensioni
df_grouped = df.groupby('movieId').agg(
    average_rating=('rating', 'mean'),   # Media delle valutazioni
    review_count=('rating', 'count')     # Conteggio delle recensioni
).reset_index()

# Visualizzo il risultato
print(df_grouped)

# Filtro per estrarre il film con movieId voluto
#film_862 = df_grouped.loc[df_grouped['movieId'] == 862]
#film_8844= df_grouped.loc[df_grouped['movieId'] == 8844]
#film_0114709 = df_grouped.loc[df_grouped['movieId'] == 0114709]

# Stampa il risultato
#print(film_862)
#print(film_0114709)