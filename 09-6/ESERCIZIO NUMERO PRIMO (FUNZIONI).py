def decoratore(funzione): # definisco il decoratore
    def wrapper():
        nome = input("Inserisci il tuo nome: ") #chiedo all'utente di inserire nome e numero
        numero = int(input("Inserisci un numero: "))
        
        divisori = funzione(numero, nome) #eseguo la funzione e ottengo la lista dei divisori

        if divisori:# stampo la lista
            print(f"{nome} la lista dei divisori di {numero} è: {divisori}")
        else:
            print(f"{nome}, il numero {numero} è un numero primo.")
    
    return wrapper


@decoratore
def primo_o_no(numero, nome):
    divisori = [] #inizializzo la lista
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:  # ae trova un divisore
            divisori.append(i)  # aggiungo il divisore alla lista
            print(f"Il numero non è primo! {i} è un divisore.")
    
    if len(divisori) == 0: # se non trovo nessun divisore, il numero è primo
        print(f"{nome}, il numero {numero} è primo!")
    
    return divisori

primo_o_no() #chiamo la funzione


