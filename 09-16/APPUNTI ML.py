import pandas as pd

#L'ERRORE PIU COMUNE CHE SI PIO FARE NEL ML 
#1 CONFONDERE L'ML CON TUTTA L'AI 
#2 PENSARE CHE UN SOLO TIPO DI APPRENDIMENTO PUO FAR COMPRENDERE ALLA MACCHINA TUTTE LE RELAZIONI

#DIVERSI TIPI DI APPRENDIMENTO
#1 SUPERVISIONATO: SIA INPUT CHE OUTPUT VENGONO VISUALIZZATI (ESEMPIO IMMAGINE CANE E GATTO)
#2 NON SUPERVISIONATO: NON ABBIAMO OUTPUT: SI CERCA DI TROVARE UNA RELAZIONE TRA I DATI
#3 PER RINFORZO: SI BASA SULLA CONCEZIONE DI PUNIZIONE OPPURE PREMIO

#UNA RETE NEURALE FA PARTE DEI MODELLI DI APPRENDIMENTO
#AVVIENE UN PROCESSO INVISIBILE IN CUI SI PARTE DAI DATI DI INPUT CHE VENGONO POI OUTPUTTATI
#POSSIAMO AVERE UN SOLO STRATO INTERNO, UN PUNTO SOLO DI USCITA

#c'è un solo output perchè viene restituito come parte di una clase OOP

#DEEP LEARNING è DIVERSO DAL MACHINE LEARNING, CERCA IL MOTIVO DI ALCUNE RISPOSTE, NON RESTITUISCE SOLO UNA RISPOSTA

####NUMPY####DALLA 202 IN POI
#SUPPORTO PER ARRAY MULTIDIMENSIONALI
#ESEMPIO 1
"""import numpy as np

# Creazione di un array unidimensionale
arr = np.array([1, 2, 3, 4, 5])

# Creazione di un array bidimensionale
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

#ESEMPIO 2
import numpy as np

# Creazione di un array
arr = np.array([1, 2, 3, 4, 5])

# Utilizzo di alcuni metodi
print("Forma dell'array:",arr.shape) # Output: (5,)
print("Dimensioni dell'array:",arr.ndim) # Output: 1
print("Tipo di dati:", arr.dtype) # Output: int64 (varia a seconda della piattaforma)
print("Numero di elementi:", arr.size) # Output: 5
print("Somma degli elementi:", arr.sum()) # Output: 15
print("Media degli elementi:", arr.mean()) # Output: 3.0
print("Valore massimo:", arr.max()) # Output: 5
print("Indice del valore massimo:", arr.argmax()) # Output: 4

arr = np.array([1, 2, 3], dtype='int32')
print(arr.dtype) # Output: int32

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape) # Output: (2, 3)"""

