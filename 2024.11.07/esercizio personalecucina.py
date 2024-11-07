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
    
    def __init__(self, nome, eta):
        self.__nome = nome
        self.__eta = eta
        self.LISTA_MAGICA_RICHIESTA = []

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

        


class Chef(PersonaleCucina):
    
    def __init__(self, nome, eta, specialita):
        PersonaleCucina.__init__(self, nome, eta)
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
    
    def gestisci_inventario(self):
        print(f"{self.get_nome()} gestisce inventario.")  

    def lavora(self):
        self.gestisci_inventario()   



class CuocoLinea(PersonaleCucina):
     
     def cucina_piatto(self, nome_piatto):
        print(f"{self.get_nome()} prepara {nome_piatto}.")  
     
     def lavora(self):
        self.cucina_piatto("pizzoccheri")
     
     

