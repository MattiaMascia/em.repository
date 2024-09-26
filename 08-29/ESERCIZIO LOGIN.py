nome = "admin" #nome utente predefinito
password = "1234" #password predefinita

nome1 = input("inserisci il nome: ") #inseriamo qui il nome utente
password1 = input("inserisci la password: ") #inseriamo qui la password

if nome == nome1 and password ==password1:
    print("benvenuto nel tuo profilo")
    coloreanimale = input("vuoi inserire il tuo colore o il tuo animale preferito come domanda segreta? (colore/animale)") #inseriamo qui il colore preferito
    if coloreanimale == "animale":
        animale = input("inserisci il tuo animale preferito: ") #inseriamo qui l'animale preferito
    elif coloreanimale =="colore":
        colore = input("inserisci il tuo colore preferito: ") #inseriamo qui il tuo preferito
        
    cambiopassword = input("vuoi cambiare il nome utente o la password?(si/no) ")
    if cambiopassword =="si":
        nome = input("inserisci il tuo nuovo nome utente: ") #inseriamo il nuovo nome utente
        password = input("inserisci qui la tua nuova password: ") #inseriamo la nuova password
        print("benvenuto nel tuo profilo!") #entrati nel profilo
    elif cambiopassword == "no":
        print("benvenuto nel tuo profilo!") #entrati nel profilo
else:
    print("nome utente o password risultano errati!") #qui non siamo riusciti ad entrare nel profilo

