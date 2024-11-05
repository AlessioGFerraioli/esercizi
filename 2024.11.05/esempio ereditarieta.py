'''
2024.11.05 11.03
esempio di ereditarieta singola

'''

class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
    
    def mostra_informazioni(self):
        print(f"Veicolo marca {self.marca}, modello {self.modello}")


class DotazioniSpeciali:
    def __init__(self, dotazioni):
        self.dotazioni = dotazioni
    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")



# ereditarieta singola
class Quad(Veicolo):
    pass


class AutomobileSportiva(Veicolo, DotazioniSpeciali):
    def __init__(self, marca, modello, dotazioni, cavalli):
        # questo init lo definisco come l'init di Veciolo seguito da init di DotazioniSpeciali
        Veicolo.__init__(self, marca, modello)
        DotazioniSpeciali.__init__(self, dotazioni)
        # aggiungo un nuovo attributo proprio di questa classe figlio, non ereditato da niente
        self.cavalli = cavalli

    def mostra_informazioni(self):
        # super() serve per fare riferimento alla PRIMA classe padre (sempre e solo la prima, in questo caso "Veicolo"). sarebbe stato ugaule scrivere Veicolo.mostra_informazioni()
        super().mostra_informazioni()
        # i metodi di qualsaisi delle classi gnitori sono ereditati dal figlio
        # dunque possiamo chiamare metodi di qualsiasi delle classi genitori come se fossero della classe figlio
        # chiamiamo un metodo della prima classe padre
        print(f"potenza: {self.cavalli} CV")
        # chiamiamo un metodo della seconda classe padre
        self.mostra_dotazioni()




# esempio di come la classe Quad erediti le caratteristiche della classe Veicolo
marca = "special"
modello = "one"
il_mio_quad = Quad(marca, modello)
il_mio_quad.mostra_informazioni()