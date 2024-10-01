import pandas as pd

# Caricamento dei file CSV
df_rat = pd.read_csv("C://Users//Loredana//Desktop//Academy MM//PYTHON//PROGETTO//ratings_small_CLEAN.csv", low_memory=False)
df_movie = pd.read_csv("C://Users//Loredana//Desktop//Academy MM//PYTHON\PROGETTO//movies_metadata_50_perc.csv", low_memory=False)

# Trova gli ID comuni tra i due dataset
unici_df_rat = pd.Series(df_rat['movieId'].unique())
comuni = df_movie['movieId'].isin(unici_df_rat)  # Film presenti in entrambi i dataset

# Filtra i film comuni in df_movie
df_movie_comuni = df_movie[comuni]

# Filtra le recensioni comuni in df_rat
presenti_rec = df_rat['movieId'].isin(df_movie_comuni['movieId'])
df_rat_comuni = df_rat[presenti_rec]

# Salva i nuovi dataset filtrati
df_movie_comuni.to_csv("C://Users//Loredana//Desktop//Academy MM//PYTHON//PROGETTO//CSV_PULITI//movies_metadata_comuni_small.csv", index=False)
df_rat_comuni.to_csv("C://Users//Loredana//Desktop//Academy MM//PYTHON//PROGETTO//CSV_PULITI//ratings_comuni_small.csv", index=False)

# Conteggi per verificare
print(f"Numero di film comuni nel dataset movies: {len(df_movie_comuni)}")
print(f"Numero di recensioni comuni nel dataset ratings: {len(df_rat_comuni)}")
