
##QUI FACCIO QUALCHE ESEMPIO CON LA FUNZIONE len()
# Lunghezza di una stringa
stringa = "Python"
lunghezza_stringa = len(stringa)
print(lunghezza_stringa)  # Output: 6

# Lunghezza di una lista
lista = [1, 2, 3, 4, 5]
lunghezza_lista = len(lista)
print(lunghezza_lista)  # Output: 5

# Lunghezza di una tupla
tupla = (10, 20, 30)
lunghezza_tupla = len(tupla)
print(lunghezza_tupla)  # Output: 3

# Lunghezza di un dizionario (numero di coppie chiave-valore)
dizionario = {"nome": "Alice", "età": 25, "città": "Roma"}
lunghezza_dizionario = len(dizionario)
print(lunghezza_dizionario)  # Output: 3

# Lunghezza di un insieme (set)
insieme = {1, 2, 3, 4}
lunghezza_insieme = len(insieme)
print(lunghezza_insieme)  # Output: 4

# Lunghezza di una lista contenente altre liste
lista_nidificata = [[1, 2], [3, 4, 5], [6]]
lunghezza_lista_nidificata = len(lista_nidificata)
print(lunghezza_lista_nidificata)  # Output: 3


##QUI FACCIO QUALCHE ESEMPIO CON LA FUNIZONE split()
# Split di una stringa in base agli spazi
testo = "Python è un linguaggio dinamico"
parole = testo.split()
print(parole)

# Split di una stringa usando la virgola come delimitatore
testo = "mele,banane,ciliegie,arance"
frutti = testo.split(',')
print(frutti)

# Split con un numero massimo di divisioni
testo = "nome:età:città:paese"
dati = testo.split(":", 2)
print(dati)

# Split di una stringa con spazi multipli
testo = "Python   è    fantastico"
parole = testo.split()
print(parole)

##QUI FACCIO QUALCHE ESEMPIO CON replace()
# Sostituzione di una parola con un'altra
testo = "Mi piace Python"
nuovo_testo = testo.replace("Python", "Java")
print(nuovo_testo)

# Sostituzione di un carattere con un altro
testo = "Hello World!"
nuovo_testo = testo.replace("o", "0")
print(nuovo_testo)

# Sostituzione solo della prima occorrenza
testo = "banana, banana, banana"
nuovo_testo = testo.replace("banana", "mela", 1)
print(nuovo_testo)


#CONTROLLO CHAR E STRING
n = 'a'
concatenato = n+n
print(concatenato)
print(type(n))


