# Decoratore che logga il risultato della funzione
def log_compression(func):
    def wrapper(stringa):
        risultato = func(stringa)
        print(f"Stringa originale: {stringa}")
        print(f"Stringa compressa: {risultato}")
        return risultato
    return wrapper

# Funzione per comprimere la stringa
@log_compression
def comprimi_stringa(stringa):
    compressa = []
    contatore = 1
    
    # Iteriamo sulla stringa e controlliamo i caratteri consecutivi
    for i in range(1, len(stringa)):
        if stringa[i] == stringa[i - 1]:
            contatore += 1
        else:
            compressa.append(stringa[i - 1] + str(contatore))
            contatore = 1
    compressa.append(stringa[-1] + str(contatore))  # Aggiunge l'ultimo gruppo

    stringa_compressa = ''.join(compressa)
    
    # Se la stringa compressa non è più corta, restituisci l'originale
    return stringa_compressa if len(stringa_compressa) < len(stringa) else stringa

# Test della funzione
stringa_test = "aaaabbccccc"
comprimi_stringa(stringa_test)




