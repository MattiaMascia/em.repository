# Create un gestionale scolastico in cui l'utente può inserire,
# modificare o eliminare, alunni voti e medie e naturalmente anche 
# solo visualizzare i dati in database, questo programma utilizzerà un db sql come archivio

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=8889,
    database="DataBase_Studenti"
)

mycursor = mydb.cursor()# Creazione del cursore per eseguire le query

#funzione inserisci studente
def inserire_studente():
    nome = input("Inserisci il nome dello studente: ")
    cognome = input("Inserisci il cognome dello studente: ")
    voto_italiano = int(input("Inserisci il voto di italiano: "))
    voto_matematica = int(input("Inserisci il voto di matematica: "))
    voto_inglese = int(input("Inserisci il voto di inglese: "))
    
    sql = "INSERT INTO studenti (nome, cognome, voto_italiano, voto_matematica, voto_inglese, media) VALUES (%s, %s, %s, %s, %s, %s)"
    nuovo_studente = (nome, cognome, voto_italiano, voto_matematica, voto_inglese, (voto_italiano + voto_matematica + voto_inglese) / 3)
    mycursor.execute(sql, nuovo_studente)
    mydb.commit()
    print(f"Studente {nome} {cognome} aggiunto correttamente.")

#funzione modifica voti
def modifica_voti():
    id_studente = int(input("Inserisci l'ID dello studente: "))
    print("Quale voto vuoi modificare?")
    print("1. Italiano")
    print("2. Matematica")
    print("3. Inglese")
    scelta = int(input("Inserisci la tua scelta: "))
    
    if scelta == 1:
        nuovo_voto = int(input("Inserisci il nuovo voto di italiano: "))
        sql = "UPDATE studenti SET voto_italiano=%s WHERE id=%s"
        val = (nuovo_voto, id_studente)
    elif scelta == 2:
        nuovo_voto = int(input("Inserisci il nuovo voto di matematica: "))
        sql = "UPDATE studenti SET voto_matematica=%s WHERE id=%s"
        val = (nuovo_voto, id_studente)
    elif scelta == 3:
        nuovo_voto = int(input("Inserisci il nuovo voto di inglese: "))
        sql = "UPDATE studenti SET voto_inglese=%s WHERE id=%s"
        val = (nuovo_voto, id_studente)
    else:
        print("Scelta non valida!")
        return

    mycursor.execute(sql, val)
    mydb.commit()
    print("Voto aggiornato correttamente.")
    aggiorna_media(id_studente)

#funzione per aggiornare la media
def aggiorna_media(id_studente):
    sql = "SELECT voto_italiano, voto_matematica, voto_inglese FROM studenti WHERE id=%s"
    mycursor.execute(sql, (id_studente,))
    voti = mycursor.fetchall()
    
    media = (voti[0][0] + voti[0][1] + voti[0][2]) / 3
    sql = "UPDATE studenti SET media=%s WHERE id=%s"
    val = (media, id_studente)
    mycursor.execute(sql, val)
    mydb.commit()
    print(f"Media aggiornata a {media:.2f} per lo studente con ID {id_studente}.")

#funzione per visualizzare la tabella
def visualizza_tabella():
    mycursor.execute("SELECT * FROM studenti")
    risultati = mycursor.fetchall()
    print("\nTabella Studenti:")
    print("ID | Nome | Cognome | Italiano | Matematica | Inglese | Media")
    for studente in risultati:
        print(f"{studente[0]} | {studente[1]} | {studente[2]} | {studente[3]} | {studente[4]} | {studente[5]} | {studente[6]:.2f}")
    print("")

#funzione per eliminare 
def elimina_studente():
    id_studente = int(input("Inserisci l'ID dello studente da eliminare: "))
    sql = "DELETE FROM studenti WHERE id=%s"
    mycursor.execute(sql, (id_studente,))
    mydb.commit()
    print(f"Studente con ID {id_studente} eliminato.")

# Menu principale
def menu():
    while True:
        print("\nGestione Studenti - Menu:")
        print("1. Aggiungi studente")
        print("2. Modifica voti studente")
        print("3. Visualizza tabella studenti")
        print("4. Elimina studente")
        print("5. Esci")
        
        scelta = input("Scegli un'opzione: ")
        
        if scelta == '1':
            inserire_studente()
        elif scelta == '2':
            modifica_voti()
        elif scelta == '3':
            visualizza_tabella()
        elif scelta == '4':
            elimina_studente()
        elif scelta == '5':
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida, riprova.")

#menu user/amministratore
def user():
    scelta1= int(input("Amministratore(1)/Utente(2)"))
    if scelta1 == 1:
        password = input("Inserisci password:")
        if password == "1234":
            menu()
        else:
            print("password sbagliata")
            visualizza_tabella()
    elif scelta1 ==2:
        visualizza_tabella()
    else:
        print("scelta non valida.")

# Avvio del programma
user()