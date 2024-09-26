#Esercizio 2
while True: ##inserisco un while per ripetere il loop all'infinito
    numero = int(input("Inserisci un numero: ")) #chiedo di inserire un numero in formato intero
    
    # Codice da eseguire se la variabile non è un intero
    #conto alla rovescia 
    for i in range (numero, -1, -1): # inserisco un for per ripeter in loop fino al verificarsi della condizione di arresto
        print(i)
        
    scelta=input("vuoi ripetere il test?(s/n)")
    if scelta=="n":
        break