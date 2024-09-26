##CONTROLLO DEL FLUSSO
##IF
numero = -10
if numero > 0: 
    print("Il numero è positivo")
if numero < 0: 
    print("Il numero è negativo")

##ELSE
numero = 10
if numero > 0: 
    print("Il numero è positivo") 
else: 
    print("Blocco Else")

##ELIF
numero = 10
if numero > 0:
    print("Il numero è positivo")
    if numero == 100:
        print("wow")
elif numero < 0:
    print("Il numero è negativo")
else:
    print("Il numero è zero")

