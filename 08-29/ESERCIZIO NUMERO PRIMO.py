while True: 
    numero = int(input("inserisci un numero per controllare che sia primo: "))
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:  # Se trova un divisore, il numero non è primo
            print("il numero non è primo")