while True: #while per ripetere il loop infinite volte
    numero = int(input("Inserisci un numero: "))

    #conto alla rovescia 
    for i in range (numero, -1, -1): #imposto -1 per arrivare fino a zero
        print(i)

    ripetere = input("vuoi inserire un altro numero?(si/no)")

    if ripetere == "no":
        print("programma finito")
        break