'''
2024.11.05 15.48

esercizio conto bancario (incapsulmaneto)

creare una classe ContoBancario che incapsula le informazioni di un conto
e fornisce metodi per gestire il saldo in modo sicuro.
L'obiettivo è utilizzare l'incapsulmaento per prevenire accessi
non autorizzati o modifiche inappropriate al saldo del conto.


'''

class Banca:
    
    def __init__(self, conto):
        self.conto = conto

    def prelievo(self):
        importo = float(input("Inserisci importo da prelevare: "))
        if self.conto.get_saldo() < importo:
            print("Disponibilità insufficiente. ")
        else:
            self.conto.preleva(importo)

    def deposito(self):
        importo = float(input("Inserisci importo da depositare: "))
        self.conto.deposita(importo)

    def visualizzazione(self):
        self.conto.visualizza_saldo()

    def start(self):
        continuare = True
        while continuare == True:
            risposta = int(input("Digita 1 per prelievo, 2 per deposito, 3 per visualizzaione, 4 per uscire: "))
            if risposta == 1:
                self.prelievo()
            elif risposta == 2:
                self.deposito()
            elif risposta == 3:
                self.visualizzazione()
            elif risposta == 4:
                continuare = False


class ContoBancario:
    
    def __init__(self, titolare, saldo):
        self.__titolare = titolare
        self.__saldo = saldo

    def deposita(self, importo):
        if importo <= 0:
            print("Errore: l'importo deve essere un numero positivo. ")
        else:
            self.__saldo = self.__saldo + importo

    def preleva(self, importo):
        if importo <= 0:
            print("Errore: l'importo deve essere un numero positivo. ")
        self.__saldo = self.__saldo - importo

    def visualizza_saldo(self):
        print()
        print(f"Il saldo attuale è: {self.__saldo}")

    def get_saldo(self):
        return self.__saldo 

    def set_saldo(self, importo):
        self.__saldo = importo

    def get_titolare(self):
        return self.__titolare 

    def set_titolare(self, importo):
        self.__titolare = importo

    




conto = ContoBancario('Alessio', 0)
banca = Banca(conto)

banca.start()