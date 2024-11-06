'''
2024.11.06 11.25

esercizio metodo pagamento



'''



class MetodoPagamento:

    def __init__(self, giacenza=0):
        self.__giacenza = giacenza

    def effettua_pagamento(self, importo):
        if self.test_giacenza_sufficiente == True:
            pagamento_effettuato = True
        else:
            pagamento_effettuate = False    
        return pagamento_effettuato

    def get_giacenza(self):
        return self.__giacenza

    def set_giacenza(self, giacenza):
        self.__giacenza = giacenza

    def test_giacenza_sufficiente(self, importo):
        if importo > self.get_giacenza():
            return False
        else:
            return True


class CartaDiCredito(MetodoPagamento):

    def effettua_pagamento(self, importo):
        # richiedi data carta
        numero_carta = input("Numero carta: ")
        scadenza = input("Scadenza mm/yy: ")
        codice_segreto = input("Codice segreto: ")

        if self.__test_credenziali_corrette(numero_carta, scadenza, codice_segreto):
            # effettua pagamento
            super().effettua_pagamento(importo)
        else:
            print("Credenziali errate.")

    def __test_credenziali_corrette(self, numero_carta, scadenza, codice_segreto):
        return True
        
class PayPal(MetodoPagamento):

    def effettua_pagamento(self, importo):
        # richiedi dati paypal
        mail = input("Indirizzo email: ")
        password = input("Password: ")

        if self.__test_credenziali_corrette(mail, password):
            # effettua pagamento
            super().effettua_pagamento(importo)
        else:
            print("Credenziali errate.")
    

    def __test_credenziali_corrette(self, mail, password):
            return True


class BonificoBancario(MetodoPagamento):
    
    pass

    '''
    def effettua_pagamento(self, importo):
        return super().effettua_pagamento()
    '''


class GestorePagamenti:

    metodi_di_pagamento = {}

    def __init__(self):
        # dizionario metodi di pagmaento (nome:oggetto)
        self.metodi_di_pagamento = {}

    def inserisci_metodo(self):
        print("Inserisci nuovo metodo di pagamento")
        nome = input("Dai nome: ")

        print("Tipologia (c per carta di credito, p per paypal, b per bonifico)")
        tipo = input(": ")
        
        giacenza = input("Inserisci giacenza: ")

        if tipo == 'c':
            self.metodi_di_pagamento[nome] = CartaDiCredito()
            print(f"Metodo di pagamento carta di credito {nome} creato")
        elif tipo == 'p':
            self.metodi_di_pagamento[nome] = PayPal()
            print(f"Metodo di pagamento paypal {nome} creato")
        elif tipo == 'b':
            self.metodi_di_pagamento[nome] = BonificoBancario()
            print(f"Metodo di pagamento bonifico bancario {nome} creato")

    def paga(self):
        print()
        nome_metodo = input("Digita nome metodo pagamento da utilizzare: ")
        if nome_metodo in self.metodi_di_pagamento.keys():
            print(f"selezionato metodo {self.metodi_di_pagamento[nome_metodo]}")
            importo = input("Digita l'importo da pagare: ")
            pagamento_effettuato = self.metodi_di_pagamento[nome_metodo].effettua_pagamento(importo)
            if pagamento_effettuato:
                print("Pagamento effettuato!")
            else:
                print("Pagamento non andato a buon fine, riprovare. ")
        else:
            print("Non esiste nessun metodo pagamento con questo nome. ")
        print()

    def start(self):
        attivo = True
        while attivo == True:
            print()
            print("Sistema Gestore Pagamenti")
            print("Digita")
            print("i per inserire metodo di pagamento,")
            print("e per effettuare pagamento,")
            print("q per uscire")
            risposta = input(": ")
            if risposta == "i":
                self.inserisci_metodo()
            elif risposta == 'e':
                self.paga()
            elif risposta == 'q':
                attivo = False
            

    

mio_gestore = GestorePagamenti()

mio_gestore.start()