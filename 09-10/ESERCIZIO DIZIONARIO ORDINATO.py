dizionario = {"a":1, "b":12, "c":11, "d":5}
lista_valori = list(dizionario.values())
lista_chiavi = list(dizionario.keys())
dizionario2= dict(zip(lista_valori, lista_chiavi))

dizionario3 = {}
for element in sorted(dizionario2, reverse=True):
    dizionario3[dizionario2[element]] =element

print(dizionario3)
    