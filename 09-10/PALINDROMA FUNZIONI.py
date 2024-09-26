# Scrivete un programma che utilizza una funzione che accetta
# come parametro una stringa passata dall’utente e restituisce in
# risposta se è palindroma o no.
# Esempio:
# ‘I topi non avevano nipoti’ è palindroma
# 'ciao' non è palindroma
def palindroma(stringa):
    stringa_pulita = ""
    
    for c in stringa:
        if c.isalpha():
            stringa_pulita += c.lower()
    
    return stringa_pulita == stringa_pulita[::-1]

def inserimento():
    stringa = input("Inserisci una stringa: ")
    
    if palindroma(stringa):
        print(f"'{stringa}' è palindroma.")
    else:
        print(f"'{stringa}' non è palindroma.")

inserimento()    

# stringa1 = "ciao a tutti"
# stringa2 = ""

# for i in range(len(stringa1)-1, -1, -1):
#     stringa2 += stringa1[i]
# print(stringa2 == stringa1)