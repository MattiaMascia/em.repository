import pandas as pd
# Dati di esempio
data = {'Data': ['2021-01-01','2021-01-01','2021-01-01','2021-01-02','2021-01-02'],
        'Città': ['Roma','Milano','Napoli','Roma','Milano'],'Prodotto': ['Mouse','Tastiera','Mouse','Tastiera','Mouse'],
        'Vendite': [100, 200, 150, 300, 250]}

df = pd.DataFrame(data)
print(df)
# Creazione della tabella pivot
pivot_df = df.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')

#raggruppa per città e prodotto aggiungendo la funzione alla fine
print("\nTabella con Pivot")
print(pivot_df)