import pandas as pd

df=pd.read_csv("C://Users//Loredana//Desktop//Academy MM//PYTHON//PROGETTO//THE-MOVIES-DATASET//ratings_small.csv",low_memory=False)
df_ratings_clean=df
#togliamo eventuali duplicati e copie inutili
df_ratings_clean.drop_duplicates(inplace=True)
df_ratings_clean.drop(columns=['timestamp'],inplace=True)
print(df_ratings_clean.head())
print(df_ratings_clean.info())  # Vedi il tipo di dati
print(df_ratings_clean.describe())  # Statistiche di base

df_ratings_clean.to_csv("C://Users//Loredana//Desktop//Academy MM//PYTHON//PROGETTO//ratings_small_CLEAN.csv",index=False)