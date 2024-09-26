class Automobile:  # dichiaro la classe
    numero_di_ruote = 4  # attributo di classe
    
    def __init__(self, marca, modello):  # metodo costruttore
        self.marca = marca  # attributo di istanza
        self.modello = modello  # attributo di istanza

    def stampa_info(self):  # metodo di istanza
        print("L'automobile è una", self.marca, self.modello)

# Crea oggetti di Automobile
Auto1 = Automobile("Fiat", "500")  # crea un oggetto di Automobile
Auto2 = Automobile("BMW", "X3")  # crea un altro oggetto di Automobile

# Stampa le informazioni delle automobili
Auto1.stampa_info()  # stampa "L'automobile è una Fiat 500"
Auto2.stampa_info()  # stampa "L'automobile è una BMW X3"