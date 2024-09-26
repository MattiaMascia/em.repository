import numpy as np
#esercizio pagina 236
#1 CREARE UNA NUOVA MATRICE 2D DID DIMENSIONI SPECIFICATE CON NUMERI CASUALI
def crea_matrice():
    righe = int(input("Numero di righe: "))
    colonne = int(input("Numero di colonne: "))
    matrice = np.random.randint(0, 100, (righe, colonne))  
    print("La tua matricw è:", matrice)
    return matrice

#2 ESTRARRE E STAMPARE LA SOTTO MATRICE CENTRALE
def sottomatrice_centrale(matrice):
    righe, colonne = matrice.shape
    r_centrali = righe // 2
    c_centrali = colonne // 2

#inserisco un doppio if per controllare sia le righe che le colonne
    if righe % 2 == 0:  
        r_iniziali = r_centrali - 1
        r_finali = r_centrali + 1
    else:  
        r_iniziali = r_centrali
        r_finali = r_centrali + 1

    if colonne % 2 == 0:  
        c_iniziali = c_centrali - 1
        c_finali = c_centrali + 1
    else:  
        c_iniziali = c_centrali
        c_finali = c_centrali + 1

    sottomatrice = matrice[r_iniziali:r_finali, c_iniziali:c_finali]
    print("La sotto matrice è:", sottomatrice)

#3 TRASPORRE LA MATRICE E STAMPARLA
def trasposta(matrice):
    trasp=matrice.T
    print("La matrice trasposta è: ", trasp)

#4 CALCOLARE E STAMPARE LA SOMMA DI TUTTI GLI ELEMENTI
def somma(matrice):
    somma_elementi = np.sum(matrice)
    print("La somma degli elementi è:",somma_elementi)

#5 MENU
def menu():
    matrice = None
    while True:
        print("\nMenu:")
        print("1. Crea una matrice ")
        print("2. Estrai la sotto matrice")
        print("3. Stampa la trasposta")
        print("4. Stampa la somma")
        print("5. Esci!!")
        
        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            matrice = crea_matrice()
        elif scelta == "2":
            if matrice is not None:
                sottomatrice_centrale(matrice)
            else:
                print("Prima crea una matrice!!")
        elif scelta == "3":
            if matrice is not None:
                trasposta(matrice)
            else:
                print("Prima crea una matrice!!")
        elif scelta == "4":
            if matrice is not None:
                somma(matrice)
            else:
                print("Non hai creato una matrice!!")
        elif scelta == "5":
            print("Sei fuori dal programma!!")
            break
        else:
            print("Scelta non valida.")

menu()
    