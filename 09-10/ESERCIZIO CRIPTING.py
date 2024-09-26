# Il Cifrario di Cesare è un algoritmo di crittografia che consiste nello spostare
# ciascuna lettera di una certa quantità di posti nell'alfabeto. Per utilizzarlo, si
# sceglie una chiave (scelta dall’utente) che rappresenta il numero di posti
# di cui ogni lettera dell'alfabeto verrà spostata: ad esempio, se si sceglie
# una chiave di 3, la lettera A diventerà D, la lettera B diventerà E e così via.
# Per decifrare un messaggio cifrato con il cifrario di Cesare bisogna
# conoscere la chiave utilizzata e spostare ogni lettera indietro di un numero
# di posti corrispondente alla chiave.

def cripting(frase, alfabeto="abcdefghilmnopqrstuvz", caratteri_speciali = ".,;:-_ ><)(/?!)"):
    frase_criptata = ""
    
    for c in frase:
        if c in alfabeto:
            posizione_corrente = alfabeto.index(c)
            nuova_posizione = (posizione_corrente + 2) % len(alfabeto)
            frase_criptata += alfabeto[nuova_posizione]
        elif c in caratteri_speciali:
            frase_criptata += c
        else:
            return "La frase non può essere criptata!"
    return frase_criptata


frase = input("Inserisci una frase: ")
risultato = cripting(frase)
print(f"Frase criptata: {risultato}")