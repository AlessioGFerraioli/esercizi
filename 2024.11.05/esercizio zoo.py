'''
2024.11.05 11.22

esercizio ereditarieta 
(esercizio zoo)

classe base Animale
    attributi
        nome
        eta
    metodi
        fai_suono(): print suono generico dell'animale

tre classi figlie
    esempio leone, giraffa, pinguino
        ognuna con metodi specifici

'''

class Animale:

    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
    
    def fai_suono(self):
        print("VERSO DI ANIMALE!!")


class Cavallo(Animale):
    
    def __init__(self, nome, eta, manto):
        Animale.__init__(self, nome, eta)
        self.manto = manto

    def fai_suono(self):
        print("hiiiiihiiiii!!")
    
    def galoppa(self):
        print(f"Il Cavallo {self.nome} galoppa!")


class Ciuco(Animale):
    
    def __init__(self, nome, eta, manto):
        Animale.__init__(self, nome, eta)
        self.manto = manto

    def fai_suono(self):
        print("hii hooo!!")
    
    def trotta(self):
        print(f"Il Ciuco {self.nome} trotta!")



class Mulo(Cavallo, Ciuco):
    
    def __init__(self, nome, eta, manto):
        Cavallo.__init__(self, nome, eta, manto)
        Ciuco.__init__(self, nome, eta, manto)

    def fai_suono(self):
        print("hiihiiii hooo!!")
    
    def trotterella(self):
        print(f"Il Mulo {self.nome} trotterella!")


class CiucoParlante(Ciuco):

    def __init__(self, nome, eta, manto, lingua):
        Ciuco.__init__(self, nome, eta, manto)
        self.lingua = lingua

    def fai_suono(self):
        print(f"Hey! Io parlo {self.lingua}")

class Volante:
    def __init__(self, n_ali):
        self.n_ali = n_ali
    
    def vola(self):
        print("Hey! Vola!")
    
class CiucoParlanteVolante(CiucoParlante, Volante):

    def __init__(self, nome, eta, manto, lingua):
        CiucoParlante.__init__(self, nome, eta, manto, lingua)
        Volante.__init__(self,n_ali=0)
    
    def fai_suono(self):
        print("Proprio così, idiota, ora sono un ciuco parlante e volante!")
        print("Avrai visto un tappeto volante, magari anche un disco volante,")
        print("ma scommetto che non hai mai visto un ciuco volante!")

ciuchino = CiucoParlanteVolante("Ciuchino",24,"bruno","italiano")

ciuchino.fai_suono()




class Zoo:

    inventario = {}

    def __init__(self):
        # dizionario di tutti gli animali (keys:nomi, value:oggettoAnimale)
        self.inventario = {}
    
    def aggiungi_animale(self):
        print()
        print(f"Aggiungi animale")
        print("Specie accolte:\nCavallo,\n Ciuco,\n Mulo,\n CiucoParlante,\n CiucoParlanteVolante")
        specie = input("Seleziona specie: ").lower()

        nome = input("Inserisci nome: ")
        if nome not in self.inventario.keys():
            # creazione animale
            eta = input("Inserisci eta")    
            # richiedi il manto se è una delle specie con manto
            specie_con_manto = ["cavallo", "ciuco", "mulo", "ciucoparlante", "ciucoparlantevolante" ]
            specie_parlanti = ["ciucoparlante", "ciucoparlantevolante"]

            if specie in specie_con_manto: 
                manto = input("Inserisci colore manto: ")
            if specie in specie_parlanti:
                lingua = input("Inserisci lingua parlata: ")
                
            if specie == "cavallo":
                self.inventario[nome] = Cavallo(nome, eta, manto)
            elif specie == "ciuco":
                self.inventario[nome] = Ciuco(nome, eta, manto)
            elif specie == "mulo":
                self.inventario[nome] = Mulo(nome, eta, manto)
            elif specie == "ciucoparlante":
                self.inventario[nome] = CiucoParlante(nome, eta, manto, lingua)
            elif specie == "ciucoparlantevolante":
                self.inventario[nome] = CiucoParlanteVolante(nome, eta, manto, lingua)
                                
        else:
            # animale gia presente, creazione interrotta
            print(f"{nome} è già presente nello zoo!")


        print()
        print(f"Animale {nome} inserito, specie {specie}.")
        print("---------------------")
        print()
    
    def rimuovi_animale(self):
        print()
        print("Rimuovi animale ")
        nome = input("Nome: ")
        if nome not in self.inventario.keys():
            print("animale non presente in inventario. ")
        else:
            animale_da_rimuovere = self.inventario[nome][0]
            self.inventario.pop(nome)
            print(f"Animale {nome} rimosso.")
            print()

    def info_animale(self):
        pass

zoo_delle_favole = Zoo()

attivo = True
while attivo == True:
    print(f"Sistema Zoo",)
    print(f"Digita: ")
    print()
    print("add/a per aggiungere un animale allo zoo")
    print("remov/r per rimuovere un animale")
    print("quit/q per uscire")
    risposta = input(": ").lower()
    if risposta == "add" or risposta == "a":
        zoo_delle_favole.aggiungi_animale()
    elif risposta == "sell" or risposta == "s":
        zoo_delle_favole.vendi_animale() 
    elif risposta == "q":
        attivo = False
