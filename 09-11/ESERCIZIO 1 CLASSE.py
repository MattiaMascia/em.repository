# Crea una classe chiamata Punto. Questa classe dovrebbe avere:
# Due attributi: x e y, per rappresentare le coordinate del punto nel piano.
# Un metodo muovi che prenda in input un valore per dx e un valore per dy e modifichi le
# coordinate del punto di questi valori.
# Un metodo distanza_da_origine che restituisca la distanza del punto dall'origine (0,0) del
# piano.

class Punto:
    
    def __init__(self,x,y):
        try:
            if isinstance(x, int) and isinstance(y, int):
                self.x = x
                self.y = y
        except:
            print("Inserisci valori interi")
            
        
    def muovi(self, dx , dy):
        try:
            if type (dx == int) and type(dy == int):
                self.x += dx
                self.y += dy
        except:
            print("Inserisci valori interi")
       
    
    def distanza_origine(self):
        return self.x , self.y

punto = Punto(5,4)

punto.muovi("a",1)

print(punto.distanza_origine())
