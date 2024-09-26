import pandas as pd
import numpy as np

#1 Caricare i dati in un DataFrame autogenerandoli casualmente

# Lista preimpostata di nomi
nomi = ['Fabiana', 'Marco', 'Sara', 'Antonello', 'Maria', 'Paolo', 'Elena', 'Andrea', 'Giulia', 'Francesco', 'Valerio', 'Marta', 'Simone']
citta = ['Roma', 'Milano', 'Napoli', 'Campobasso', 'Bologna', 'Firenze', 'Palermo', 'Riccia', 'Verona', 'Venezia']

eta = np.random.randint(18, 100, size=10) 

salari = np.random.randint(1000, 5000, size=10)  

nomi_casuali = np.random.choice(nomi, size=10, replace=True)
citta_casuali = np.random.choice(citta, size=10, replace=True)

data = {
    'Nome': nomi_casuali,
    'Età': eta,
    'Città': citta,
    'Salario': salari
}

df = pd.DataFrame(data)

#2 Visualizzare le prime e le ultime cinque righe del DataFrame
print(df.head())
print(df.tail())

#3 Visualizzare il tipo di dati di ciascuna colonna
print(df.dtypes)

#4 Calcolare statistiche descrittive di base per le colonne numeriche
print(df.describe())

print("\nMedia Età:", df['Età'].mean())
print("Mediana Età:", df['Età'].median())
print("Deviazione Standard Età:", df['Età'].std())

print("\nMedia Salario:", df['Salario'].mean())
print("Mediana Salario:", df['Salario'].median())
print("Deviazione Standard Salario:", df['Salario'].std())

#5 Identificare e rimuovere eventuali duplicati
print("\nDuplicati:", df.duplicated().sum())
df = df.drop_duplicates() #per eliminare

#6 Gestire i valori mancanti sostituendoli con la mediana della rispettiva colonna
# Simuliamo alcuni valori mancanti (Thanks to GPT)
df.isna 
df.loc[1, 'Salario'] = np.nan 

df['Salario'].fillna(df['Salario'].median(), inplace=True)


#7 Aggiungere una nuova colonna chiamata "Categoria Età"
def categora_eta(eta):
    if eta <= 18:
        return 'Giovane'
    elif 19 <= eta <= 65:
        return 'Adulto'
    else:
        return 'Senior'

df['Categoria Età'] = df['Età'].apply(categora_eta)

#8 Salvare il DataFrame pulito in un nuovo file CSV
df.to_csv('09-17/dati_puliti_con_nomi.csv', index=False)

print("\nDataFrame finale con Categoria Età aggiunta:")
print(df)

##FARE ESERCIZIO 2 PAG 254
