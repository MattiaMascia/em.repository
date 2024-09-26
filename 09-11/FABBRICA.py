# Lo scopo di questo esercizio è creare un sistema di gestione per una fabbrica che produce e vende vari
# tipi di prodotti. Gli studenti dovranno creare una classe base chiamata Prodotto e diverse classi
# derivate che rappresentano diversi tipi di prodotti. Inoltre, dovranno creare una classe Fabbrica che
# gestisce l'inventario e le vendite dei prodotti.
# 1.Classe Prodotto:
# Attributi:
# nome (stringa che descrive il nome del prodotto)
# costo_produzione (costo per produrre il prodotto)
# prezzo_vendita (prezzo a cui il prodotto viene venduto al pubblico)
# Metodi:
# calcola_profitto: restituisce la differenza tra il prezzo di vendita e il costo di produzione.
# 2.Classi Derivate:
# Creare almeno due classi derivate da Prodotto, per esempio Elettronica e Abbigliamento.
# Aggiungere attributi specifici per ciascun tipo di prodotto, come materiale per Abbigliamento e
# garanzia per Elettronica.
# 3.Classe Fabbrica:
# Attributi:
# inventario: un dizionario che tiene traccia del numero di ogni tipo di prodotto in magazzino.
# Metodi:
# aggiungi_prodotto: aggiunge prodotti all'inventario.
# vendi_prodotto: diminuisce la quantità di un prodotto in inventario e stampa il profitto
# realizzato dalla vendita.
# resi_prodotto: aumenta la quantità di un prodotto restituito in inventario.



"""""# cucina1 = Cucina("Cucina Moderna", 2000, 3500)
# cucina1.stampa_info()
# print(f"Profitto dalla cucina: {cucina1.calcola_profitto_cucina()}€")

# mobili1 = Mobili("Bianco", "Legno")
# mobili1.stampa_info_mobili()

# elettrodomestico1 = Elettrodomestici("A++", "150 kWh/anno")
# elettrodomestico1.stampa_info_elettrodomestico()

# macchina = Macchina("Panda", 1000, 1500)
# macchina.stampa_info()
# print(f"Profitto Macchina: {macchina.calcola_profitto_macchina()}")

# interni = Interni("Pelle", "Rosso")
# interni.stampa_info_interni()

# motore = Motore("Diesel", 2000)
# motore.stampa_info_motore()"""""



# Definizione delle classi
class Macchina:
    def __init__(self, descrizione, costo_produzione, prezzo_vendita):
        self.descrizione = descrizione
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto_macchina(self):
        return self.prezzo_vendita - self.costo_produzione

    def stampa_info(self):
        print(f"Descrizione: {self.descrizione}, Costo Produzione: {self.costo_produzione}, Prezzo Vendita: {self.prezzo_vendita}")


#sottoclasse interni
class Interni:
    def __init__(self, materiale, colore):
        self.materiale = materiale
        self.colore = colore

    def stampa_info_interni(self):
        print(f"Materiale interni: {self.materiale}, Colore: {self.colore}")

#sottoclasse motore
class Motore:
    def __init__(self, tipo_motore, cilindrata):
        self.tipo_motore = tipo_motore
        self.cilindrata = cilindrata
    
    def stampa_info_motore(self):
        print(f"Tipo di Motore: {self.tipo_motore}, Cilindrata: {self.cilindrata}cc")



#Classe cucina
class Cucina:
    def __init__(self, descrizione, costo_produzione, prezzo_vendita):
        self.descrizione = descrizione
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto_cucina(self):
        return self.prezzo_vendita - self.costo_produzione

    def stampa_info(self):
        print(f"Descrizione: {self.descrizione}, Costo Produzione: {self.costo_produzione}€, Prezzo Vendita: {self.prezzo_vendita}€")


#sottoclasse mobili
class Mobili:
    def __init__(self, colore , materiale):
        self.colore = colore
        self.materiale = materiale

    def stampa_info_mobili(self):
        print(f"Colore: {self.colore}, Materiale: {self.materiale}")


#sottoclasse elettrodomestici
class Elettrodomestici:
    def __init__(self, classe_elettrodomestico, consumo):
        self.classe_elettrodomestico = classe_elettrodomestico
        self.consumo = consumo


    def stampa_info_elettrodomestico(self):
        print(f"Tipo di Elettrodomestico: {self.classe_elettrodomestico}, Consumo: {self.consumo}")



#classe fabbrica
class Fabbrica:
    def __init__(self):
        self.inventario = {}#inizializzo un dizionario
    
    def aggiungi_prodotto(self, prodotto, quantita):
        if prodotto in self.inventario:
            self.inventario[prodotto] += quantita
        else:
            self.inventario[prodotto] = quantita
    
    def vendi_prodotto(self, prodotto, quantita):
        if prodotto in self.inventario and self.inventario[prodotto] >= quantita:
            self.inventario[prodotto] -= quantita
            profitto = prodotto.calcola_profitto_cucina() if isinstance(prodotto, Cucina) else prodotto.calcola_profitto_macchina()
            print(f"Venduti {quantita} {prodotto.descrizione}. Profitto: {profitto * quantita}€")
        else:
            print("Prodotto non disponibile o quantità insufficiente.")
    
    def resi_prodotto(self, prodotto, quantita):
        if prodotto in self.inventario:
            self.inventario[prodotto] += quantita
        else:
            self.inventario[prodotto] = quantita
    
    def stampa_inventario(self):
        for prodotto, quantita in self.inventario.items():
            print(f"{prodotto.descrizione}: {quantita} pezzi")

"""# Creazione di oggetti di prodotto

#CREO UNA MACCHINA
macchina1 = Macchina("Motore V8", 10000, 15000)
#CREO INTERNI
interni1 = Interni("Pelle", "Nero")
#CREO MOTORE
motore1 = Motore("Diesel", 3000)
#CREO UNA CUCINA
cucina1 = Cucina("Cucina Moderna", 5000, 7000)
#MOBILI
mobili1 = Mobili("Bianco", "Legno Massello")
#ELETTRODOMESTICI
elettrodomestico1 = Elettrodomestici("A++", "150 kWh/anno")

fabbrica = Fabbrica()

fabbrica.aggiungi_prodotto(macchina1, 10)  
fabbrica.aggiungi_prodotto(cucina1, 5)     
fabbrica.aggiungi_prodotto(mobili1, 15)    


fabbrica.vendi_prodotto(macchina1, 2)  # Vende 2 motori V8 e calcola il profitto
# Reso di un prodotto
fabbrica.resi_prodotto(cucina1, 2)  # Restituisce 2 cucine moderne all'inventario

fabbrica.stampa_inventario()  # Mostra il numero di pezzi per ciascun tipo di prodotto in inventario
"""


