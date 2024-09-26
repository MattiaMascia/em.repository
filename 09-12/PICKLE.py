import pickle 

# dizionario = {1:"Tommaso", 2:"Mirko"}

# dizB =pickle.dumps(dizionario)

# with open("09-12/binario.bin", "wb") as myfile:
#     myfile.write(dizB)

with open("09-12/binario.bin","rb") as myfile:
    contenuto = myfile.read()

contenuto = pickle.loads(contenuto)
print(contenuto)
