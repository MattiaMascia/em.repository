def calcola_parole(file_path):
    with open(file_path, "r") as file : 
        contenuto = file.read()
        contenuto1 = contenuto.replace("\n", " ")#rimpiazzo \n con lo spazio
        contenuto2 = contenuto1.replace("'", " ")#rimpiazzo ' con lo spazio
        numero_caratteri = len(contenuto1)#conta i caratteri
        numero_righe = len(contenuto.splitlines())#conta le righe con slitlines 
        numero_parole = len(contenuto2.split())

        print(f"Il numero di caratteri è {numero_caratteri}")
        print(f"Il numero di righe è {numero_righe}")
        print(f"Il numero di parole è {numero_parole}")
        

calcola_parole("09-12/testo.txt")


