# Obiettivo: Creare una classe Ristorante che permetta di gestire alcune funzionalità di base .
# Requisiti:
# 1.Definizione della Classe:
# Creare una classe chiamata Ristorante.
# La classe dovrebbe avere un costruttore __init__ che accetta due parametri: nome (nome del ristorante) e
# tipo_cucina (tipo di cucina offerta).
# Definire un attributo aperto che indica se il ristorante è aperto o chiuso. Questo attributo deve essere
# impostato su False di default (cioè, il ristorante è chiuso).
# Un dizionario menu dove dentro ci sono i piatti e prezzi che ha il ristorante
# 2.Metodi della Classe:
# descrivi_ristorante(): Un metodo che stampa una frase descrivendo il ristorante, includendo il nome e il
# tipo di cucina.
# stato_apertura(): Un metodo che stampa se il ristorante è aperto o chiuso.
# apri_ristorante(): Un metodo che imposta l'attributo aperto su True e stampa un messaggio che indica che
# il ristorante è ora aperto.
# chiudi_ristorante(): Un metodo che imposta l'attributo aperto su False e stampa un messaggio che indica
# che il ristorante è ora chiuso.
# aggiungi_al_menu(): Un metodo per aggiungere piatti al menu
# togli_dal_menu(): Un metodo per togliere piatti al menu
# stampa_menu(): Un metodo per stampare il menu
# 3.Testare la Classe:
# Creare un'istanza della classe Ristorante, passando i valori appropriati al costruttore.
# Testare tutti i metodi creati per assicurarsi che funzionino come previsto.

class Ristorante:
    def __init__(self, nome, tipo_cucina):
        self.nome = nome                  #primo parametro
        self.tipo_cucina = tipo_cucina    #secondo parametro
        self.aperto = False               #attributo di classe
        self.menu= {} 
    def descrivi_ristorante(self):
        print(f"Il ristorante {self.nome} offre la cucina {self.tipo_cucina}")
    
    def stato_apertura(self):
        if self.aperto:
            print(f"Il ristorante {self.nome} è aperto.")
        else:
            print(f"Il ristorante {self.nome} è chiuso.")
    def apri_ristorante(self):
        self.aperto=True 
        print(f"Il ristorante {self.nome} è aperto.")
    def chiudi_ristorante(self):
        print(f"Il ristorante {self.nome} è chiuso.")
    def aggiungi_al_menu(self, nome_piatto, prezzo):
        if nome_piatto not in self.menu:
            self.menu[nome_piatto]=prezzo
            #piatto che viene aggiunto al menu
        else:
            print(f"Il piatto {nome_piatto} è già presente nel menu")
    def togli_dal_menu(self, nome_piatto):
        if nome_piatto in self.menu:
            del self.menu[nome_piatto]
        else:
            print(f"Il piatto {nome_piatto} non è presente nel menu.")
    def stampa_menu(self):
        if self.menu:
            print(f"Menu del ristorante '{self.nome}':")
            for nome_piatto, prezzo in self.menu.items():
                print(f"{nome_piatto}:{prezzo} ")
        else:
            print(f"Il menu del ristorante '{self.nome}' è vuoto.")


ristorante = Ristorante("Ciocca", "Cinese")

ristorante.descrivi_ristorante()

ristorante.stato_apertura()

ristorante.apri_ristorante()

ristorante.aggiungi_al_menu("Ravioli", 15)

ristorante.stampa_menu()

ristorante.togli_dal_menu("Ravioli")

ristorante.stampa_menu()




        
    