lista =[]
def area_triangolo(base, altezza):
    area = (base * altezza) / 2
    lista.append(area)
    print(f"L'area del triangolo è: {area}")

def area_quadrato(base_q):
    area_q = base_q * base_q
    lista.append(area_q)
    print(f"L'area del quadrato è: {area_q}")

def area_rettangolo(base_r, altezza_r):
    area_r = base_r * altezza_r
    lista.append(area_r)
    print(f"L'area del rettangolo è: {area_r}")

while True:
    # Chiedi all'utente quale operazione vuole effettuare
    scelta = input("Vuoi calcolare l'area di un triangolo, quadrato o rettangolo? (t/q/r) oppure 'esci' per uscire: ")
    
    if scelta == 'esci':
        print("Uscita dal programma.")
        break
    
    elif scelta == 't':
        base_t = int(input("Qual'è la base del tuo triangolo? "))
        altezza_t = int(input("Qual'è l'altezza del tuo triangolo? "))
        print(lista)
        area_triangolo(base_t, altezza_t)
        
    elif scelta == 'q':
        base_q = int(input("Qual'è il lato del tuo quadrato? "))
        area_quadrato(base_q)
        
    elif scelta == 'r':
        base_r = int(input("Qual'è la base del tuo rettangolo? "))
        altezza_r = int(input("Qual'è l'altezza del tuo rettangolo? "))
        area_rettangolo(base_r, altezza_r)
        
    else:
        print("Scelta non valida. Per favore scegli tra 't', 'q', 'r' o 'esci'.")
        

        
