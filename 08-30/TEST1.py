numero_di_parole = int(input("Quante parole vuoi inserire nella lista? "))

# Inizializza una lista vuota
parole = []

# Utilizzo un ciclo for per ripetere il loop il numero di volte desiderato
for i in range(numero_di_parole):
    parola = input("Inserisci la parola: ")
    parole.append(parola)

#stampo a schermo 
print("Hai inserito le parole:", parole)