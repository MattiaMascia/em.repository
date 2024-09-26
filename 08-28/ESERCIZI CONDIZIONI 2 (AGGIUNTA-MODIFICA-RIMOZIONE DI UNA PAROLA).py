frase = input("Inserisci una frase: ") #inserimento della frase
scelta = input("Cosa vuoi fare con questa frase? 1: Aggiungi una parola, 2: Rimuovi una parola, 3:Modifica una parola")
#scelta dell'operazione da svolgere
if scelta == "1": #aggiunta di una parola
    aggiunta=input("Quale parola vuoi aggiungere?")
    frase1 = frase + " " + aggiunta
    print("La tua nuova frase è:", frase1)
elif scelta == "2": #rimozione di una parola
    rimozione = input("Quale parola vuoi rimuovere?")
    if rimozione in frase:
        frase2 = frase.replace(rimozione, "")
        print("La tua nuova frase è:", frase2, ".")
    else:  
        print("La parola non è esistente")
elif scelta == "3": #modifica din una parola nella frase
    modifica = input("Quale parola vuoi modificare?")
    modifica1 = input("Con quale parola vuoi sostituirla?")
    if modifica in frase:
        frase3 = frase.replace(modifica, modifica1)
        print("La tua nuova frase è ", frase3)
    else: #caso in cui la parola che si è scelta non è all'interno della frase
        print("La parola che hai scelto non è all'interno della frase")
else:
    print("L'opzione che hai scelto non esiste.")
    
    


        