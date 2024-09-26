# Create un gestionale scolastico in cui l'utente può inserire,
# modificare o eliminare, alunni voti e medie e naturalmente anche 
# solo visualizzare i dati in database, questo programma utilizzerà un db sql come archivio
import mysql.connector

# Creazione della connessione al server MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=8889,
    database = "DataBase_Studenti"
)

# Creazione del cursore per eseguire le query
mycursor = mydb.cursor()

#Creazione DataBase_Studenti
#sql = "CREATE DATABASE DataBase_Studenti"

#drop Table
#sql = "drop table Studenti"

#Creazione Tabella Studenti
#sql = "create table Studenti(id int auto_increment primary key, nome varchar(255), cognome varchar(255), voto_italiano int, voto_matematica int, voto_inglese int,  media float)"
#mycursor.execute(sql)

def inserire_studente(nome,cognome,voto_italiano,voto_matematica,voto_inglese):
    sql = "insert into studenti(nome,cognome,voto_italiano,voto_matematica,voto_inglese, media) values(%s,%s,%s,%s,%s,%s)"
    nuovo_studente=(nome, cognome, voto_italiano,voto_matematica,voto_inglese, (voto_italiano+voto_matematica+voto_inglese)/3)
    mycursor.execute(sql,nuovo_studente)
    mydb.commit()
   
# inserire_studente("Mattia","Mascia",7,8,9)
# inserire_studente("Martina","Curcio",5,7,9)
# inserire_studente("Mattia","Rossi",10,8,2)
# inserire_studente("Cosimo","Rossi",4,7,2)


def modificare_votoitaliano(id_studente,nuovo_voto_italiano):
    sql="UPDATE studenti SET voto_italiano=%s WHERE id=%s"
    val=(nuovo_voto_italiano,id_studente)
    mycursor.execute(sql,val)
    mydb.commit()



def modificare_votomatematica(id_studente,nuovo_voto_matematica):
    sql="UPDATE studenti SET voto_matematica=%s WHERE id=%s"
    val=(nuovo_voto_matematica,id_studente)
    mycursor.execute(sql,val)
    mydb.commit()


def modificare_votoinglese(id_studente,nuovo_voto_inglese):
    sql="UPDATE studenti SET voto_inglese=%s WHERE id=%s"
    val=(nuovo_voto_inglese,id_studente)
    mycursor.execute(sql,val)
    mydb.commit()


#modificare_votoitaliano(1,9)
#modificare_votomatematica(3,8)
#modificare_votoinglese(2,8)


def aggiorna_media(id_studente):
    sql = "select voto_italiano,voto_matematica,voto_inglese from studenti where id=%s"
    mycursor.execute(sql,(id_studente,))
    voti = mycursor.fetchall()
    print(voti)
    sql="UPDATE studenti SET media=%s WHERE id=%s"
    media=(voti[0][0]+voti[0][1]+voti[0][2])/3
    val=(media,id_studente)
    mycursor.execute(sql,val)
    mydb.commit()

#aggiorna_media(1)

def elimina_studente(id_studente):
    sql="delete from studenti where id=%s"
    mycursor.execute(sql,(id_studente,))
    mydb.commit()


# print(mycursor.rowcount, "record inseriti") # Esecuzione della query


