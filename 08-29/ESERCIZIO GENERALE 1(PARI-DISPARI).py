##Esercizio 1
while True: #uso il ciclo while per ripetere il loop all'infinito
    numero = int(input("Inserisci un numero per controllare che sia pari o dispari: "))
    q = 2
    controllo = numero % q
    if controllo == 0: ##se il numero diviso per 2 restituisce resto 0 vuol dire che è pari
        print("il tuo numero è pari")
    else:
        print("il tuo numero è dispari")
    
    scelta=input("vuoi ripetere il test?(s/n)") ##chiedo se si ha voglia di ripetere il test
    if scelta=="n": ##se la scelta è n=no c'è un break e viene rotto il loop
        break
