numeri = []
while True:
    scelti = int(input("scegli un numero: "))
    numeri.append(scelti)
    altro = str(input("vuoi aggiungere un altro numero?(s/n)"))
    if altro == "n":
        break
for x in numeri:
    print(x**2)
