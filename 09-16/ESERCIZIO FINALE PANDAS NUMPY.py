import numpy as np
import pandas as pd


##PUNTO NUMERO 1
date = pd.date_range(start="2023-01-01", periods=365)

mean = 2000  
std = 500

incremento_media = 2   # aumento giornalmente il numero di visitatori
decremento_std = 0.5   # riduco giornalmente la deviazione standard

visitatori = []
for i in range(365):
    media_giorno = mean + i * incremento_media   # trend crescente sulla media
    std_giorno = std - i * decremento_std        # trend decrescente sulla deviazione standard
    
    # faccio si che la deviazione standard non diventi negativa
    std_giorno = max(std_giorno, 0)
    
    visitatori.append(int(np.random.normal(loc=media_giorno, scale=std_giorno)))


dati_visitatori = {"Data": date, "Visitatori": visitatori}
#print(dati_visitatori)

#PUNTO NUMERO 2
dataframe_visitatori = pd.DataFrame(dati_visitatori)
#print(dataframe_visitatori.head())
#print(data_clienti)


#PUNTO NUMERO 3
media_mensile = dataframe_visitatori.resample('M', on='Data').mean() #utilizzo reample per scegliere i dati mensili
std_mensile = dataframe_visitatori.resample('M', on='Data').std()

print(media_mensile)
print(std_mensile)




