# Crea una classe chiamata Libro. Questa classe dovrebbe avere:
# Tre attributi: titolo, autore e pagine.
# Un metodo descrizione che restituisca una stringa del tipo "Il libro 'titolo' è stato scritto
# da 'autore' e ha 'pagine' pagine.".

class Libro:
    def __init__(self, Titolo, Autore, Pagine):
        if isinstance(Titolo, str) and isinstance(Autore, str):
            self.Titolo = Titolo
            self.Autore = Autore
        else:
            raise ValueError("Il titolo e l'autore devono essere stringhe.")
        
        if isinstance(Pagine, int):
            self.Pagine = Pagine
        else:
            raise ValueError("Il numero di pagine deve essere un intero.")

    def stampa_info(self):
        print(f"Il titolo del libro è '{self.Titolo}', l'autore è {self.Autore}, e il numero di pagine è {self.Pagine}.")

Libro1 = Libro("iii", "Me", 60)  
Libro1.stampa_info()  