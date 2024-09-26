numeri = []  # Inizializzo una lista

# Uso un ciclo for per chiedere 10 numeri
for i in range(10):
    numero = int(input(f"Inserisci il numero {i+1}: "))  # Chiedo all'utente di inserire un numero
    numeri.append(numero)  # Aggiungo il numero alla lista

print("I numeri inseriti sono:", numeri)  # Stampo la lista finale

massimo = numeri[0]  # Inizializza massimo come il primo numero
for numero in numeri:
    if numero > massimo:
        massimo = numero

minimo = numeri[0]  # Inizializza minimo come il primo numero
for numero in numeri:
    if numero < minimo:
        minimo = numero 

# Uso il ciclo while per ordinare la lista
n = len(numeri)
i = 0
while i < n: #Ogni passaggio "sposta" l'elemento più grande alla fine della lista
    j = 0
    while j < n - i - 1:  #confronta coppie di elementi adiacenti e li scambia se sono nell'ordine sbagliato.
        if numeri[j] > numeri[j + 1]:
            numeri[j], numeri[j + 1] = numeri[j + 1], numeri[j]
        j += 1
    i += 1

# Trovo i due numeri centrali
mid1 = numeri[(n // 2) - 1]
mid2 = numeri[n // 2]

# Calcolo della mediana come la media dei due numeri centrali
mediana = (mid1 + mid2) / 2
print("La tua lista ordinata è: ", numeri)
print("Il numero più grande è: ", massimo)
print("Il numero più piccolo è: ", minimo)
print("Il numero mediano è: ", mediana)

