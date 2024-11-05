'''

2024.11.05 10.10
esercizio fabbrica

esercizio sulle classi

lo scopo di questo esercizio è creare un sistema di gestione
per una fabbrica che produce e vende vari tipi di prodotti
gli studenti dovranno creare una classe base 
chiamata prodotto e diverse classi derivate che rappresentano diversi tipi 
di prodotti
inoltre, dovranno creare un classe fabbrica che gestisce
l'inventario e le vendite dei prodotti

1 classe prodotto:
    attributi:
        nome
        costo_produzione
        prezzo_vendita
    metodi:
        calcola_profitto (restituisce differenza tra prezzo di vendita e costo di produzione)

3 classe fabbrica:
    attributi:
        inventario: dizionario che tiene traccia del numero di ogni tipo di prodotto
    metodi:
        aggiungi_prodotto
        vedni prodotto (diminuisce la quantità di un prodotto in inventario e stampa il profitto realizzato dalla vendita)
        resi_prodotto: aumenta la quantita di un prodotto restiuito in inventario

'''


class Prodotto:
    
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione
    

class Elettronica(Prodotto):

    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        Prodotto.__init__(nome, costo_produzione, prezzo_vendita, garanzia)
        self.garanzia = garanzia

    
class Abbigliamento(Prodotto):

    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        Prodotto.__init__(nome, costo_produzione, prezzo_vendita, materiale)
        self.materiale = materiale
        

class Fabbrica:

    inventario = {}

    def __init__(self):
        # dizionario che rappresenta inventario; keys:nomi, values:quantita
        self.inventario = {}
    
    def aggiungi_prodotto(self):
        print()
        print(f"Aggiungi prodotto")
        nome = input("Nome: ")
        

        if nome not in self.inventario.keys():
            tipologia = input("Tipologia prodotto (elettronica/abbigliamento): ")
            prezzo_vendita = float(input("Prezzo vendita: "))
            costo_produzione = float(input("Costo di produzione: "))
            quantita = int(input("Quantità da aggiungere: "))

            if tipologia == 'elettronica': 
               garanzia = input("Garanzia: ")    
               prodotto_da_aggiungere = Elettronica(nome, prezzo_vendita, costo_produzione, garanzia)
            if tipologia == 'abbigliamento': 
               garanzia = input("Materiale: ")    
               prodotto_da_aggiungere = Elettronica(nome, prezzo_vendita, costo_produzione, materiale)
            self.inventario[nome] = [prodotto_da_aggiungere, quantita]
        else:
            quantita = int(input("Quantità da aggiungere: "))
            self.inventario[nome][1] = self.inventario[nome][1] + quantita

        print()
        print(f"Prodotto {nome} inserito, quantità attuale {self.inventario[nome][1]}.")
        print()
    
    def vendi_prodotto(self):
        print()
        print("Vendita prodotto ")
        nome = input("Nome: ")
        if nome not in self.inventario.keys():
            print("Prodotto non presente in inventario. ")
        else:
            prodotto_da_vendere = self.inventario[nome][0]
            quantita_venduta = int(input("Quantità venduta: "))
            self.inventario[nome][1] = self.inventario[nome][1] - quantita_venduta 
            # calcolo il profitto ricavato
            profitto = prodotto_da_vendere.calcola_profitto()*quantita_venduta
            print(f"{quantita_venduta} unità di Prodotto {nome} venduta/e!")
            print(f"Profitto {profitto}.")
            print(f"Quantità attuale {self.inventario[nome][1]}.")
            print()

    def resi_prodotto(self):
        print()
        print("Reso prodotto ")
        nome = input("Nome: ")
        if nome not in self.inventario.keys():
            print("Prodotto non presente in inventario. ")
        else:
            quantita_resa = int(input("Quantità resa: "))
            self.inventario[nome][1] = self.inventario[nome][1] + quantita_resa 

    def info_prodotto(self):
        pass

fabbrica_de_alessio_dal_1972 = Fabbrica()

attivo = True
while attivo == True:
    print(f"Sistema Fabbrica",)
    print(f"Digita: ")
    print()
    print("add/a per aggiungere un prodotto all'inventario")
    print("sell/s per vendere un prodotto")
    print("ret/r per fare un reso")
    print("quit/q per uscire")
    risposta = input(": ").lower()
    if risposta == "add" or risposta == "a":
        fabbrica_de_alessio_dal_1972.aggiungi_prodotto()
    elif risposta == "sell" or risposta == "s":
        fabbrica_de_alessio_dal_1972.vendi_prodotto() 
    elif risposta == "q":
        attivo = False

