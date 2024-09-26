import random

numero_random = random.randint(1, 100)  # funzione che genera un numero casuale tra 1 e 100

#definisco la funzione
def indovina_numero():
    
    while True:
        scelta = input("Indovina un numero tra 1 e 100 (o digita esc per terminare): ")

        if scelta == 'esc':  
            print("Sei fuori dal gioco!")
            break
        
        elif not scelta.isdigit():  # inserisco isdigit per verficare che sia un numero
            print("Inserisci un nimero valido:")
            continue
        
        if scelta < numero_random:
            print("Il numero è più alto!")
        elif scelta > numero_random:
            print("Il numero è più basso!")
        else:
            print("Hai indovinato!")
            break

#avvio il gioco
indovina_numero()

