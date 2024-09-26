
while True:     #inizializzo il while 
    lista1 = []
    lista2 = []
    
    # Inserimento dei numeri per la lista1
    for x in range(5):
        while True:
            try:
                numeri1 = int(input(f"Inserisci il numero {x+1} per la lista 1: "))
                lista1.append(numeri1)
                break
            except ValueError:
                print("Per favore, inserisci un numero intero valido.")
    
    # Inserimento dei numeri per la lista2
    for y in range(5):
        while True:
            try:
                numeri2 = int(input(f"Inserisci il numero {y+1} per la lista 2: "))
                lista2.append(numeri2)
                break
            except ValueError:
                print("Per favore, inserisci un numero intero valido.")
    
    # Stampa delle liste
    print("La tua lista 1 è:", lista1)
    print("La tua lista 2 è:", lista2)
    
    # Calcolo della somma delle liste
    somma_liste = []
    for i in range(5):
        somma_liste.append(lista1[i] + lista2[i])
    
    print("La somma delle liste è:", somma_liste)
    
    # Richiesta di ripetizione
    ripetizione = input("Vuoi ripetere l'operazione? (si/no): ").strip().lower()
    if ripetizione == "no":
        break    #break del while al verificarsi della condizione in if

