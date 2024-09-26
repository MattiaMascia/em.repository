##ELIF
x=input("scegli il primo valore:")
if x == "5":
    y=input("scegli il secondo valore:")
    if y=="7":
        z=input("scegli il terzo valore:")
        if z=="10":
            print("hai completato tutti i livelli")
        else:
            print("l'ultimo livello non è stato rispettato")
    else:
        print("il secondo livello non è stato rispettato")
else:
    print("il primo livello non è stato rispettato")