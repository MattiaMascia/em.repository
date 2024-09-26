# Scrivete un programma che prenda i nomi degli alunni di una
# classe e i loro voti, quando l’utente scrive media il programma
# andrà a stampare i nomi di tutti gli alunni e per ogni alunno la
# media dei voti.
# Esempio:
# Nome: Giovanni , Media: 7.5
# Nome: Alfredo , Media: 9
# Nome: Michela, Media 10
alunni = {}

while True:
    nome = input("Inserisci il nome dell'alunno o scrivi 'media' per calcolare le medie: ")
    
    if nome.lower() == 'media':  
        if not alunni:  
            print("Nessun dato disponibile.")
        else:
            for alunno, voti in alunni.items():
                media = sum(voti) / len(voti)
                alunni_media = {alunno, media}
                print(f"Nome: {alunno}, Media: {media:2f}")
                #print(alunni_media)
        break
    
    else:
        voti = input(f"Inserisci i voti di {nome}, separati da uno spazio: ")
        voti_lista = []
        for v in voti.split():
            voti_lista.append(int(v))  
        alunni[nome] = voti_lista
