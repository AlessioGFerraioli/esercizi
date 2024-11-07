

from abc import ABC, abstractmethod

class Operaio:
    
    def __init__(self, nome, eta, specializzazione):
        self.nome = nome
        self.eta = eta
        self.specializzazione = specializzazione
    
    def info(self):
        print(f"Nome: {self.nome}, eta: {self.eta}, specializzazione: {self.specializzazione} ")

class Cazzuola(ABC):
    @abstractmethod
    def stendi_calce(self):
        return "steso calce con cazzuola"

class Sega(ABC):
    @abstractmethod
    def taglia_legno(self):
        return "tagliato legno con sega"

class Muratore(Operaio, Cazzuola):
    def stendi_calce(self):
        print(f"{self.nome} ha {Cazzuola.stendi_calce(self)}")

class Falegname(Operaio, Sega):
    def taglia_legno(self):
        print(f"{self.nome} ha {Sega.taglia_legno(self)}")

              


alessio = Falegname("alessio",30,"falegnameria")
alessio.taglia_legno()