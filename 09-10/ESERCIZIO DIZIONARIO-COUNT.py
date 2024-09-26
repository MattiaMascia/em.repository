stringa = input("Inserisci una stringa per ottenere in output il numero di ogni carattere: ")
numero = {}  # dizionario per memorizzare il conteggio dei caratteri

for char in stringa:  
    conteggio = stringa.count(char)  #conto i caratteri con la funzione count
    numero[char] = conteggio  

print(numero)



