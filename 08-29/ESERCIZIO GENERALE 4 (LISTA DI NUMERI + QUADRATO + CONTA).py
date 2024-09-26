# Inizializzo una lista vuota
numeri = []

# Chiedo all'utente di inserire numeri uno alla volta
while True:
    numero_input = input("Inserisci un numero (o scrivi s per terminare): ")

    if numero_input == 's':
        break  # Interrompi il ciclo se l'utente inserisced 'stop'
    try:
        # Aggiungi il numero alla lista se l'input è valido
        numeri.append(int(numero_input))
    except ValueError:
        print("Per favore, inserisci un numero valido o s per terminare.")

# Utilizzo if per controllare se la lista è vuota
if len(numeri) == 0:
    print("Lista Vuota")
else:
    # Ciclo for per trovare il numero massimo
    massimo = numeri[0]  # Inizializza massimo come il primo numero
    for numero in numeri:
        if numero > massimo:
            massimo = numero

    # Ciclo while per contare il numero di elementi nella lista
    if len(numeri) == 0:
        print("Lista Vuota")
    else:
        massimo = numeri[0]  # Inizializza massimo come il primo numero
    for numero in numeri:
        if numero > massimo:
            massimo = numero
# Usa len() per contare il numero di elementi nella lista
    conta_elementi = len(numeri)

    # Stampa il numero massimo e il numero di elementi
    print("Il numero massimo nella lista è: ", massimo)
    print("Il numero di elementi nella lista è: ", conta_elementi)