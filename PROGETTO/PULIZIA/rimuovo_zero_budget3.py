import pandas as pd
df = pd.read_csv("C://Users//Loredana//Desktop//Academy MM//PYTHON//PROGETTO//movies_metadata_CLEAN_ID.csv", low_memory=False)

# Esplorazione iniziale
print(df.head())
print(df.info())
print(df.describe())

#Rimuovo righe con budget = 0 o revenue = 0
df['budget'] = pd.to_numeric(df['budget'], errors='coerce')  # Conversione in numerico
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')  # Conversione in numerico

#Rimuovi righe dove "budget == 0" o "revenue == 0"
df_cleaned_budget_revenue = df[(df['budget'] != 0) & (df['revenue'] != 0)]

#Salva il risultato parziale
df_cleaned_budget_revenue.to_csv('C://Users//Loredana//Desktop//Academy MM//PYTHON//PROGETTO//movies_metadata_CLEAN_budget_revenue.csv', index=False)

#Visualizza il risultato dopo la prima operazione
print("\nDopo la rimozione di budget = 0 o revenue = 0:")
print(df_cleaned_budget_revenue.head())
print(df_cleaned_budget_revenue.info())
print(df_cleaned_budget_revenue.describe())

#Rimuovo i titoli contenenti numeri
titoli_giu = df_cleaned_budget_revenue['title'].str.isalpha()  # Mantieni solo titoli senza numeri
df_cleaned_titles = df_cleaned_budget_revenue[titoli_giu]

#Salva il risultato
df_cleaned_titles.to_csv('C://Users//Loredana//Desktop//Academy MM//PYTHON//PROGETTO//movies_metadata_CLEAN_title.csv', index=False)

#Visualizza il risultato
print("\nDopo la rimozione dei titoli con numeri:")
print(df_cleaned_titles.head())
print(df_cleaned_titles.info())
print(df_cleaned_titles.describe())
