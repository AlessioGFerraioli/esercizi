'''
2024.11.06 11.25

esercizio metodo pagamento



'''



class MetodoPagamento:

    def __init__(self):
        pass

    def effettua_pagamento(self, importo):
        pagamento_effettuato = True
        return pagamento_effettuato


class CartaDiCredito(MetodoPagamento):

    def __init__(self):
        pass

    '''
    def effettua_pagamento(self, importo):
        return super().effettua_pagamento()
    '''

class PayPal(MetodoPagamento):

    def __init__(self):
        pass

    '''
    def effettua_pagamento(self, importo):
        return super().effettua_pagamento()
    '''


class BonificoBancario(MetodoPagamento):

    def __init__(self):
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