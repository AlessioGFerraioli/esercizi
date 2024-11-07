'''
2024.11.07 09.43

creare una classe base PersonaleCucina e diverse classi derivate che rappresentano differenti ruoli all'interno della cucina di un ristorante. L'obiettivo è di utilizzare l'ereditarietà per condividere alcune caratteristiche comuni mentre si distinguono le responsabilità e le azioni specifiche di ogni ruolo.

Classe PersonaleCucina:
    Attributi:
    nome (stringa)
    età (intero)
    Metodi:
    lavora() (metodo generico che può essere sovrascritto per specificare il tipo di lavoro svolto)

Classi Derivate:
Chef:
    Attributi aggiuntivi come specialità (tipo di cucina in cui è specializzato)
    Metodi come prepara_menu() che dettaglia come lo chef crea nuovi piatti e menu
SousChef:
    Metodi come gestisci_inventario() per gestire l'inventario della cucina e assistere lo chef
CuocoLinea:
    Metodi come cucina_piatto(nome_piatto) che specifica la preparazione di un piatto specifico nella linea di produzione

'''


class PersonaleCucina:
    
    def __init__(self, nome, eta, piatti_conosciuti):
        self.__nome = nome
        self.__eta = eta
        self.__piatti_conosciuti = piatti_conosciuti

    def lavora(self):
        print(f"{self.get_nome()} sta lavorando.")

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_eta(self):
        return self.__eta
    
    def set_eta(self, eta):
        self.__eta = eta

    def get_piatti_conosciuti(self):
        return self.__piatti_conosciuti
    
    def set_piatti_conosciuti(self, piatti_conosciuti):
        self.__piatti_conosciuti = piatti_conosciuti

    def cucina_piatto(self, nome_piatto):
        print(f"{self.get_nome()} prepara {nome_piatto}.")      


class Chef(PersonaleCucina):
    
    def __init__(self, nome, eta, piatti_conosciuti, specialita):
        PersonaleCucina.__init__(self, nome, eta, piatti_conosciuti)
        self.__specialita = specialita

    def prepara_menu(self):
        print(f"{self.get_nome()} prepara il menu.")

    def coordina_il_team(self):
        print(f"{self.get_nome()} coordina il team.")

    def get_specialita(self):
        return self.__specialita
    
    def set_specialita(self, specialita):
        self.__specialita = specialita

    def lavora(self):
        self.prepara_menu()    
        self.coordina_il_team()

class SousChef(PersonaleCucina):
    
    def gestisci_inventario(self, inventario):
        pass

    def rifornisci_inventario(self, inventario, menu):
        pass

    def controlla_ingredienti_necessari(self, piatto, inventario, menu):
        for ingrediente in menu[piatto]:
            if ingrediente not in inventario:
                return False
        return True


    def lavora(self):
        self.gestisci_inventario()   



class CuocoLinea(PersonaleCucina):
     
    def cucina_piatto(self, nome_piatto):
        print(f"{self.get_nome()} prepara {nome_piatto}.")  
     
    def lavora(self):
        self.cucina_piatto("pizzoccheri")
     
     

class Ristorante:

    def __init__(self, menu, personale):
        self.menu = menu
        self.__personale = personale
        self.__ordinazioni = []
        self.__inventario = []
        

    def visualizza_menu(self):
        print(self.menu)

    def aggiungi_piatto_al_menu(self):
        pass

    def aggiungi_personale(self):
        pass

    def aggiungi_ordinazione(self, ordinazione):
        self.get_ordinazioni().append(ordinazione)

    def get_ordinazioni(self):
        return self.__ordinazioni
    
    def set_ordinazioni(self, ordinazioni):
        self.__ordinazioni = ordinazioni

    def cucina(self):
        for ordinazione in self.get_ordinazioni():
            nome_cliente, piatto = ordinazione
            piatto_preparato = self.prepara_piatto(piatto)
            if piatto_preparato:
                self.servi_piatto(piatto, nome_cliente)
        # clears the list of ordinazioni
        self.set_ordinazioni([])

    def prepara_piatto(self, piatto):
        piatto_conosciuto = False
        for dipendente in self.__personale:
            if piatto in dipendente.get_piatti_conosciuti():
                piatto_conosciuto = True
                dipendente.cucina_piatto(piatto)
                return True
        if piatto_conosciuto == False:
            print(f"Nessun dipendente disponibile per cucinare il piatto {piatto}. ")
            return False

    def servi_piatto(self, piatto, nome_cliente):
        print(f"Il piatto {piatto} è servito al cliente {nome_cliente}. ")


vellutata_di_zucca = ["zucca", "velluto"]
peperone_imbottonato = ["peperone", "bottoni"]
cornetti_fraciti = ["cornetti", "fraciti"]

menu_alessio = {
                "vellutata di zucca" : ["zucca", "velluto"],
                "peperone imbottonato" : ["peperone", "bottoni"],
                "cornetti fraciti" : ["cornetti", "fracitume"]
                }



class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    def ordina_piatto(self, ristorante, piatto):
        # controllare se il piatto è nel menu
        if piatto not in ristorante.menu.keys():
            print("Il piatto non è nel menu. Impossibile ordinare. ")
            return False
        else:
            print(f"Il cliente {self.get_nome()} ordina il piatto {piatto}")
            ordinazione = (self.get_nome(), piatto)
            ristorante.aggiungi_ordinazione(ordinazione)
            return ordinazione
    
    def get_nome(self):
        return self.__nome


alessio = Chef("alessio", 30, "peperone_imbottonato", "nessuna")
sara = SousChef("sara", 23, "vellutata di zucca")

staff_alessio = [alessio,sara]
ristorante_da_alessio = Ristorante(menu_alessio, staff_alessio)


giacomo = Cliente("giacomo")
giacomo.ordina_piatto(ristorante_da_alessio, "peperone imbottonato")
giacomo.ordina_piatto(ristorante_da_alessio, "cornetti fraciti")

cristina = Cliente("cristina")
cristina.ordina_piatto(ristorante_da_alessio, "vellutata di zucca")

ristorante_da_alessio.cucina()

