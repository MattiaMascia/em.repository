import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. GENERAZIONE DATI
date = pd.date_range(start="2023-01-01", periods=305)

mean = 1200  
std = 900

decremento_medio = 0.3   # aumento giornalmente il numero di visitatori
decremento_std = 0   # riduco giornalmente la deviazione standard

visitatori = []
for i in range(305):
    media_giorno = mean - (i) * decremento_medio   # trend crescente sulla media
    # std_giorno = std - i * decremento_std        # trend decrescente sulla deviazione standard
    
    # faccio sì che la media non diventi negativa
    media_giorno = max(media_giorno, 0)
    
    visitatori.append(int(np.random.normal(loc=media_giorno, scale=std)))


# 2. CREO IL DATAFRAME
patologie = ["ossa", "cuore", "testa"]
patologia_casuale = np.random.choice(patologie, size=305)

dati_visitatori = pd.DataFrame({
    "Data": date,
    "Visitatori": visitatori,
    "Patologia": patologia_casuale
})

# Imposto la colonna 'Data' come indice
dati_visitatori.set_index('Data', inplace=True)

print(dati_visitatori.head())

# 3. MEDIA E DEVIAZIONE STANDARD MENSILE
dati_visitatori['Mese'] = dati_visitatori.index.to_period('M')

media_mensile = dati_visitatori.groupby('Mese')['Visitatori'].mean()
std_mensile = dati_visitatori.groupby('Mese')['Visitatori'].std()
print(f"\nLa media per ogni mese è: {media_mensile}")
print(f"\nLa deviazione standard per ogni mese è: {std_mensile}")

# Totale visitatori per patologia
totale_per_patologia = dati_visitatori.groupby('Patologia')['Visitatori'].sum()
print(f"\nIl numero totale per ogni patologia è: {totale_per_patologia}")

totale_visitatori = dati_visitatori['Visitatori'].sum()
frequenze = totale_per_patologia / totale_visitatori
print(f"\nLa frequenza di ogni patologia è: {frequenze}")

print(f"\nLa frequenza maggiore è: {frequenze.max()}")
print(f"\nLa frequenza minore è: {frequenze.min()}")

#4 GRAFICI

# GRAFICO 1: NUMERO VISITATORI E MEDIA MOBILE
plt.figure(figsize=(14, 7))
plt.plot(dati_visitatori.index, dati_visitatori['Visitatori'], label='Visitatori Giornalieri', color='blue')
media_mobile_7gg = dati_visitatori['Visitatori'].rolling(window=7).mean()
plt.plot(dati_visitatori.index, media_mobile_7gg, label='Media Mobile a 7 Giorni', color='orange', linestyle='--')

plt.title('Numero di Visitatori Giornalieri e Media Mobile a 7 Giorni')
plt.xlabel('Data')
plt.ylabel('Numero di Visitatori')
plt.legend()
plt.grid(True)
plt.show()

# GRAFICO 2: FREQUENZA PATOLOGIE
patologie_frequenti = dati_visitatori['Patologia'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(patologie_frequenti, labels=patologie_frequenti.index, autopct='%1.1f%%')
plt.title('Distribuzione delle Patologie')
plt.show()

# GRAFICO MEDIA MENSILE
# media_mensile = dati_visitatori.resample('M').mean()

# plt.figure(figsize=(14, 7))
# plt.bar(media_mensile.index.astype(str), media_mensile['Visitatori'])
# plt.title('Media Mensile dei Visitatori')
# plt.xlabel('Data')
# plt.ylabel('Media dei Visitatori')
# plt.grid(True)
# plt.show()

# # ISTOGRAMMA PATOLOGIE
# patologie_frequenti = dati_visitatori['Patologia'].value_counts()
# plt.figure(figsize=(8, 6))
# plt.bar(patologie_frequenti.index, patologie_frequenti)
# plt.title('Distribuzione delle Patologie')
# plt.xlabel('Patologia')
# plt.ylabel('Numero di casi')
# plt.show()

