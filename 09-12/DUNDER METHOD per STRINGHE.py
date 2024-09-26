class gatto:
    def __init__(self, nome, razza):
        self.nome=nome
        self.razza=razza
    def __str__(self):
        return f"nome:{self.nome}, razza:{self.razza}"

gattino = gatto("gigio","randagio")

print(gattino)