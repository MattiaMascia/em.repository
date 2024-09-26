import pandas as pd
import numpy as np

date_range = pd.date_range(start="2023-01-01", periods=10)
città = ['Milano', 'Roma', 'Napoli']
prodotti = ['Cellulare', 'Computer', 'Aspirapolvere']

dati = {
    'Data': np.random.choice(date_range, 50),
    'Città': np.random.choice(città, 50),
    'Prodotto': np.random.choice(prodotti, 50),
    'Vendite': np.random.randint(100, 1000, 50)
}

#DATAFRAME
df_vendite = pd.DataFrame(dati)

("Dataframe")
print(df_vendite.head())

#PIVOT
pivot_df = df_vendite.pivot_table(values='Vendite', index='Città', columns='Prodotto', aggfunc='mean')

("DataFrame con PIVOT")
print(pivot_df)

#GROUPBY
grouped_df = df_vendite.groupby("Prodotto")["Vendite"].sum()

print("DataFrame con GOUPBY")
print(grouped_df)