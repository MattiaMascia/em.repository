numero_di_numeri = int(input("Quanti numeri vuoi inserire? "))
lista = []

for i in range(numero_di_numeri):
    numeri = int(input("Inserisci numero: "))
    lista.append(numeri)

for i in lista:
    string= ""
    for elemento in range(i):
        string += "*"
    print(string)

# lista  = [1, 2, 3, 4, 5]
# for i in lista:
#     print(i * "*")


