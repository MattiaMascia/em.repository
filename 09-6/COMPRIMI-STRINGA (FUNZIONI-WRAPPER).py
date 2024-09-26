def decoratore_compressione(funzione):
    def wrapper():
        # Chiede all'utente la stringa tramite l'altra funzione
        stringa = ottieni_stringa()
        
        # Chiama la funzione di compressione e ottiene il risultato
        risultato = funzione(stringa)
        
        print(f"Stringa compressa: {risultato}")
    return wrapper

#chiedo all'utente di inserise
def ottieni_stringa():
    return input("Inserisci una stringa da comprimere: ")

# Funzione per comprimere la stringa
def comprimi_stringa(stringa):
    if not stringa:
        return ""
    
    stringa_compressa = []
    count = 1  #inizializzo un count
    #vado a comprimere
    for i in range(1, len(stringa)):
        if stringa[i] == stringa[i - 1]:  #controllo due chr consecutivi
            count += 1
        else:
            stringa_compressa.append(stringa[i - 1] + str(count))#appendo il carattere e il conteggio alla stringa compressa
            count = 1 

    stringa_compressa.append(stringa[-1] + str(count))# unisco l'ultimo gruppo di caratteri

    stringa_finale = ''.join(stringa_compressa)# unisci la lista in una stringa

    if len(stringa_finale) < len(stringa):
        return stringa_finale
    else:
        return stringa

@decoratore_compressione
def esegui_compressione(stringa):
    return comprimi_stringa(stringa)

#eseguo il decoratore 
esegui_compressione()