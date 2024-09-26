import pandas as pd
from datetime import datetime

print("Inserisci i dati per il cliente:")
numero_cliente = int(input("Id Cliente: "))
nome = input("Nome: ")
cognome = input("Cognome: ")
data_nascita = input("Data di Nascita (formato YYYY-MM-DD): ")
regione_residenza = input("Regione di Residenza: ")

clienti = []  
for i in range(10):
    clienti.append({
        "id": numero_cliente + i,
        "Nome": nome,
        "Cognome": cognome,
        "Data di Nascita": data_nascita,
        "Regione di Residenza": regione_residenza
    })

df_clienti = pd.DataFrame(clienti)

df_clienti.to_csv("09-13/clienti.csv", index = False)

print(df_clienti)

def calcola_eta(data_nascita):
    data_nascita = datetime.strptime(data_nascita, "%Y-%m-%d")
    oggi = datetime.today()
    eta = oggi.year - data_nascita.year - ((oggi.month, oggi.day) < (data_nascita.month, data_nascita.day))
    return eta

def verifica_minore_18(data_nascita):
    eta = calcola_eta(data_nascita)
    return "x" if eta < 18 else " "

def verifica_maggiore_17(data_nascita):
    eta = calcola_eta(data_nascita)
    return "x" if eta >= 18 else " "

def verifica_maggiore_20(data_nascita):
    eta = calcola_eta(data_nascita)
    return "x" if eta >= 20 else " "

df_clienti['<18'] = df_clienti['Data di Nascita'].apply(verifica_minore_18)
df_clienti['>=18'] = df_clienti['Data di Nascita'].apply(verifica_maggiore_17)
df_clienti['>=20'] = df_clienti['Data di Nascita'].apply(verifica_maggiore_20)

print(df_clienti)

df_clienti.to_csv("09-13/clienti_con_verifica_eta.csv", index=False)