'''

2024.11.04 16.56
esercizio ristorante

obiettivo: creare una classe ristorante che permetta di gestire
alcune funzionalità di base

'''



class Piatto:

    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo



class Menu:

    lista_piatti = []

    def __init__(self):
        self.lista_piatti = []

    def inserisci_piatto(self, nome, prezzo):
        self.lista_piatti.append(Piatto(nome, prezzo))

    def rimuovi_piatto(self, nome):
        print(f"stai rimuovendo il piatto dal nome: " , nome)
        i = 0
        for piatto in self.lista_piatti:
            if piatto.nome == nome:
                indice_piatto_da_rimuovere = i
                break
            i = i+1
        self.lista_piatti.pop(indice_piatto_da_rimuovere)
    
    def stampa_menu(self):
        for piatto in self.lista_piatti:
            print(piatto.nome)
            print(f"...............................", piatto.prezzo,"€")
            print()



class Ristorante:
    # flag per indicare se il ristorante è attualmente aperto
    aperto = False 
    menu = Menu()

    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.menu = Menu()

    def descrivi_ristorante(self):
        # stampa una frase descrivendo nome e tipo di cucina del ristorante
        print(f"Il istorante", self.nome, "offre cucina", self.tipo_cucina)

    def stato_apertura(self):
        if self.aperto == True:
            print(f"Il ristorante", self.nome,"è aperto. ")
        else: 
            print(f"Il ristorante", self.nome,"è chiuso. ")

    def apri_ristorante(self):
        # cambia lo stato del ristorante ad aperto e notifica l'apertura (verificare non sia già aperto?)
        self.aperto = True
        self.stato_apertura()

    def chiudi_ristorante(self):
        # cambia lo stato del ristorante a chiuso e notifica la chiusura
        self.aperto = False
        self.stato_apertura()

    def aggiungi_al_menu(self):
        print(f"Inserimento nuovo piatto al menu di", self.nome)
        nome = input("Nome del piatto: ")
        prezzo = float(input("Prezzo: "))
        piatto_da_inserire = self.menu.inserisci_piatto(nome, prezzo)

    def togli_dal_menu(self):
        print(f"Rimozione di un piatto dal menu di", self.nome)
        nome = input("Nome del piatto: ")
        piatto_da_rimuovere = self.menu.rimuovi_piatto(nome)


    def stampa_menu(self):
        print(f"Stampa Menu ristorante", self.nome)
        print()
        self.menu.stampa_menu()



ristorante_alessio = Ristorante("Alessione", "avanguardistica")

'''
# esempio di funzionamento: 
ristorante_alessio.descrivi_ristorante()
ristorante_alessio.stato_apertura()
ristorante_alessio.aggiungi_al_menu()
ristorante_alessio.aggiungi_al_menu()
ristorante_alessio.stampa_menu()
ristorante_alessio.togli_dal_menu()
ristorante_alessio.stampa_menu()
'''


while attivo = True:
    print(f"Sistema Ristorante ", ristorante_alessio.nome)
    print(f"Digita: ")
    print()
    print("descr/d per una descrizione del ristorante")
    print("ins/i per inserire un piatto nel menu")
    print("togli/t per togliere un piatto dal menu")
    print("stato/st per verificare lo stato del ristorante")
    print("apri/a per aprire il ristorante")
    print("chiudi/c per chiudere il ristorante")
    print("stampa/s per stampare il menu completo")
    print("quit/q per uscire")
    risposta = input(": ").lower()
    if risposta == "d" or risposta == "descr":
        ristorante_alessio.descrivi_ristorante()
    elif risposta == "i" or risposta == "ins":
        ristorante_alessio.aggiungi_al_menu()        
    elif risposta == "t" or risposta == "togli":
        ristorante_alessio.togli_dal_menu()        
    elif risposta == "st" or risposta == "stato":
        ristorante_alessio.stato_apertura()        
    elif risposta == "a" or risposta == "apri":
        ristorante_alessio.apri_ristorante()        
    elif risposta == "c" or risposta == "chiudi":
        ristorante_alessio.chiudi_ristorante()        
    elif risposta == "s" or risposta == "stampa":
        ristorante_alessio.stampa_menu()        
    elif risposta == "q":
        attivo = False





