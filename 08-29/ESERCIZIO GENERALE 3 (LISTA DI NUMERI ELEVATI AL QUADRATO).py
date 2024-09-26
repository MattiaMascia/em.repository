#chiedo di inserire i numeri
numeri = [int(x) for x in input("Inserisci i numeri separati da uno spazio: ").split()]
#stampo i numeri a schermo 
print("La tua lista di numeri è: ", numeri)
#chiedo se si voglio elevare i numeri al quadrato
scelta = str(input("Vuoi elevare i tuoi numeri al quadrato?(s/n)"))
if scelta == "s": #se la risposta è s restituisco in output i numeri al quadrato
    numeri_al_quadrato = [x**2 for x in numeri]
    risultato = " ".join(str(x) for x in numeri_al_quadrato)
    print("I numeri elevati al quadrato sono: ", risultato)
else:
    print("Hai scelto di non ricevere gli esercizi al quadrato!")


    