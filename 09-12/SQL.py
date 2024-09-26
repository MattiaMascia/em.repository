import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user="root",
    password="root",
    port=8889,
    database = "esercitazionepython"
)

#print(mydb) per controllare se funziona

#mycursor = mydb.cursor()#questo è il cursore per interagire

#sql = "CREATE DATABASE esercitazionepython" ##per creare un database

#sql = "create table Utenti(id int auto_increment primary key, nome varchar(255), cognome varchar(255))"

# il cursore ci permette di interagire con il database
#execute e executemany ci fanno esegure 
#commit ci permette di inserire
#mycursor.execute(sql, val)#serve ogni volta per eseguire---#val serve per inserire i valori
#print(mycursor.lastrowid)##stampa l'ultimo id
mycursor = mydb.cursor()
def selezione():
    sql = "select * from utenti where id >  3"
    mycursor.execute(sql)

dati = mycursor.fetchall()##per catturarne solo uno utilizziamo fetchone
    
def inserisciDati():
    sql = "insert into utenti (nome, cognome) values (%s,%s)"
    val = [("tommaso", "muraca"),("giovanni", "rossi"),("marco","verdi"),("luca", "gialli")]
    mycursor.executemany(sql, val)#per inserire tanti valori
    
    mydb.commit()##serve per il commit
    
    print(mycursor.rowcount, "record inseriti")

# sql = "select * from utenti where id >  3"
# mycursor.execute(sql)

def delete():
    sql="delete from utenti where id =7 "
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record eliminate")

dati = mycursor.fetchall()##tutti i risultati

#dati = mycursor.fetchone()##solo un dato

for dato in dati:
    print(dato)

# for tb in mycursor:
#     print(f"Tabella: {tb}")


