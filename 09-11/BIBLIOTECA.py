# Crea una classe biblioteca
# che permetta di creare un
# libro e stamparlo
# Extra: permetti di creare
# quanti libri vuole l’utente

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

class Biblioteca:
    def __init__(self):
        self.libri = []  # Inizializza la lista contenente i libri

    def aggiungi_libro(self, Titolo, Autore, Pagine):
        nuovo_libro = Libro(Titolo, Autore, Pagine)
        self.libri.append(nuovo_libro)

    def stampa_libri(self):
        if not self.libri:
            print("Non ci sono libri nella biblioteca.")
        else:
            for libro in self.libri:
                libro.stampa_info()

biblioteca = Biblioteca()

while True:
    scelta = input("Cosa vuoi fare? add/stampa/esc: ").lower()
    
    if scelta == "add":
        Titolo = input("Inserisci il titolo del libro: ")
        Autore = input("Inserisci l'autore del libro: ")
        Pagine = input("Inserisci il numero di pagine del libro: ")

        if not Pagine.isdigit():
            print("Il numero di pagine deve essere un intero!")
            continue 

        try:
            biblioteca.aggiungi_libro(Titolo, Autore, int(Pagine))
            print("Libro aggiunto!")
        except ValueError as error:
            print(error)

    elif scelta == "stampa":
        biblioteca.stampa_libri()

    elif scelta == "esc":
        print("Uscita dal programma.")
        break

    else:
        print("Comando non valido.")







