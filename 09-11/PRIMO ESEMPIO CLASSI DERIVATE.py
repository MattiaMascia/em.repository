#classe padre Prodotto
class Prodotto:
    def __init__(self, descrizione, costo_produzione, prezzo_vendita):
        self.descrizione = descrizione
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

    def stampa_info(self):
        print(f"Descrizione: {self.descrizione}, Costo Produzione: {self.costo_produzione}€, Prezzo Vendita: {self.prezzo_vendita}€")


# classe derivata macchina
class Macchina(Prodotto):
    def __init__(self, descrizione, costo_produzione, prezzo_vendita):
        super().__init__(descrizione, costo_produzione, prezzo_vendita)#richiamo il costruttore della superclasse

    def calcola_profitto_macchina(self):
        return self.calcola_profitto() 

    def stampa_info(self):
        super().stampa_info() 
        print(f"Tipo di Macchina: {self.descrizione}")


#classe derivata cucina
class Cucina(Prodotto):
    def __init__(self, descrizione, costo_produzione, prezzo_vendita):
        super().__init__(descrizione, costo_produzione, prezzo_vendita)

    def calcola_profitto_cucina(self):
        return self.calcola_profitto() 

    def stampa_info(self):
        super().stampa_info() 
        print(f"Tipo di Cucina: {self.descrizione}")