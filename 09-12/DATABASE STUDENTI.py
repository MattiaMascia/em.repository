# creare un programma per la gestione degli studenti di una scuola,
# all'avvio se il db è presente legge i dati da db altrimenti lo crea, 
# l'utente puoi inserire studenti e voti all'interno del db

#Finita la prima parte aggiungete al programma 
#la possibilità di modificare voti e alunni

def lettura_file(nome_testo):
    with open(nome_testo,"r") as myfile:
        return myfile.read()

class Student():
  def __init__(self,id,nome,cognome,media_italiano,media_scienza,media_inglese):
     self.id=id
     self.nome=nome
     self.cognome=cognome
     self.media_ita=media_italiano
     self.media_sci=media_scienza
     self.media_ing=media_inglese
  def stringa_stud(self):
     stringa_studente="\n"+self.id+","+self.nome +","+self.cognome +","+self.media_ita +","+self.media_sci+","+self.media_ing
     return  stringa_studente
      
  
def riscrivi_database(database,matrice):
   riga=[]
   stringa=""
   for i in range(len(matrice)):
     riga.append(",".join(matrice[i]))
   for i in range(len(matrice)):
     stringa="\n".join(riga)
   with open(database,"w") as data:
       data.write("id, nome, cognome, media italiano,media scienze, media inglese"+"\n"+stringa)
 

def modifica(matrice,id,database):
   for index in range(len(matrice)):
      if id==matrice[index][0]:
         coordinata=index
   materia=int(input("Cosa vuoi cambiare? Ita(1),Sci(2),Ing(3)"))
   if materia==1:
      voto=input("Nuovo voto:")
      matrice[coordinata][3]=voto
      riscrivi_database(database,matrice)
   elif materia==2:
      voto=input("Nuovo voto:")
      matrice[coordinata][4]=voto
      riscrivi_database(database,matrice)
   elif materia==3:
      voto=input("Nuovo voto:")
      matrice[coordinata][5]=voto
      riscrivi_database(database,matrice)
   else:
      print("Scelta non valida")
def print_student(id,matrice):
  for index in range(len(matrice)):
      if id==matrice[index][0]:
         coordinata=index
  return matrice[coordinata]
   
      
   



scelta='True'
lista_id=[]
matrice=[]
while scelta=='True':
  try:
     contenuto=lettura_file("09-12/database.csv")
  except:
     with open("09-12/database.csv","a") as data:
       data.write("id, nome, cognome, media italiano,media scienze, media inglese")
       contenuto=lettura_file("09-12/database.csv")
  righe=contenuto.split("\n")
  for i in range(1,len(righe)):
    lista_id.append(righe[i].split(",")[0])
    matrice.append(righe[i].split(","))
  id=input("id")
  if id in lista_id:
     studente_conosciuto=print_student(id,matrice)
     choiche=input(f"Studente già presente,\n{studente_conosciuto}\nvuoi modificare i suoi dati? (y,n)") 
     if choiche=='y':
        modifica(matrice,id,"09-12/database.csv")
     else:
        break
  else:
     nome=input("Nome:")
     cognome=input("Cognome")
     media_it=input("Media-ita: ")
     media_sci=input("media scienze")
     media_ing=input("media inglese:")
     studente=Student(id,nome,cognome,media_it,media_sci,media_ing)
     stringa_input=studente.stringa_stud()
     with open("09-12/database.csv","a") as data:
       data.write(stringa_input)
  chc=input("Vuoi inserire altro studente? (y,n)")
  if chc=='n':
    scelta='False'