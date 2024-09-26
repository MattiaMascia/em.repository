# chiedo all'utente di inserire una frase
frase = input("Inserisci una frase: ")

vocali = "aeiouAEIOU"

# variabile di controllo per verificare se ci sono vocali
vocale_trovata = False
indice = 0
for carattere in frase:
    if carattere in vocali:
        print(f"Vocale '{carattere}' trovata all'indice {indice}")
        vocale_trovata = True
    indice += 1
if not vocale_trovata:
    print("Non ci sono vocali")