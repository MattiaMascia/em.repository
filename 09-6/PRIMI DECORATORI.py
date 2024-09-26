# Definizione del decoratore che accetta una funzione come argomento
def decoratore_con_argomenti(funzione):
    # Definizione della funzione wrapper che accetta argomenti e keyword arguments
    def wrapper(*args, **kwargs):
        # Stampa un messaggio prima dell'esecuzione della funzione
        print("Prima")
        # Esegue la funzione originale con gli argomenti e keyword arguments passati
        risultato = funzione(*args, **kwargs)
        # Stampa un messaggio dopo l'esecuzione della funzione
        print("Dopo")
        # Restituisce il risultato della funzione originale
        return risultato
    # Restituisce la funzione wrapper, che sostituisce la funzione originale
    return wrapper

# Applicazione del decoratore alla funzione somma
@decoratore_con_argomenti
def somma(a, b):
    # Restituisce la somma di due numeri
    return a + b

# Chiamata alla funzione decorata somma
print(somma(3, 4))