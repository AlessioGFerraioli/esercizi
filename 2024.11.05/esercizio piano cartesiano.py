'''

2024.11.05 14.26
esercizio piano cartesiano

'''


class Punto: 
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def muovi_punto(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy


class PianoCartesiano:

    def __init__(self, punti):
        if len(punti) < 2: 
            print("Servono almeno 2 punti per creare un piano cartesiano. \n")
        else:
            self.punti = punti

    def stampa_piano(self):
        print("------------")
        print("\nPiano Cartesiano")
        print("------------")
        for punto in self.punti:
            print(f"({punto.x},{punto.y})")


lista_punti = []
numero_punti = 2

for i in range(numero_punti):
    print(f"Punto {i}")
    x = float(input("Inserisci coordinata x: "))
    y = float(input("Inserisci coordinata y: "))
    print()
    lista_punti.append(Punto(x,y))
                
piano = PianoCartesiano(lista_punti)

piano.stampa_piano()
        
