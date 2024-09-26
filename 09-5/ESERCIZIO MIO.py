frase = str(input("inserisci una frase: "))

frase_seraparata = list(frase)
print(frase_seraparata)

carattere = input("quale carattere vuoi trovare: ")

print(f"Il carattere si trova nella posizione {frase_seraparata.index(carattere)}")
