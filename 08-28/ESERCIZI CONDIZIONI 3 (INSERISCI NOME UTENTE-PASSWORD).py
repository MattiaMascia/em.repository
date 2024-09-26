nome = "Mattia" #nome utente predefinito
password = "aiuto" #password predefinita

nome1 = input("inserisci il nome: ") #inseriamo qui il nome utente
password1 = input("inserisci la password: ") #inseriamo qui la password


if nome != nome1 and password1 != password: #caso in cui sbagliamo nome e password
    scelta1 = input("Il tuo account non esiste, vuoi creare un account? (si/no)")
    if scelta1 == "si":
        nome2 = input("inserisci il nome: ")
        password2 = input("inserisci la password: ")

elif nome != nome1 or password1 != password: #caso in cui sbagliamo nome o password
    scelta2 = input("Hai sbagliato password o nome utente, vuoi reimpostarli? (si/no)")
    if scelta2 == "si":
        nome3 = input("inserisci il nome: ")
        password3 = input("inserisci la password: ")
    
    
else: #caso in cui abbiamo password e nome utente giusti
    scelta = input("Sei dentro il tuo account, vuoi modificare nome utente o password? (digita si oppure no)")
    if scelta == "si":
        nome1 = input("inserisci il nuovo nome: ")
        password1 = input("inserisci la nuova password: ")



