'''

2024.10.30

def

esercizio base: indovina il numero

descrizione:
scrivi un programma che genera unn numero casuale tra 1 e 100 inclusi.
l'utente deve indovinare quale numero è stato generato
dopo ogni tentativo il programma dovrebbe dire all'utente
se il numero da indovinare è più alto o più basso rispetto al numero inserito
il gioco termina quando l'utente indovina o decide di uscire


'''
# genera numero casuale
from random import random
numero_casuale = int(random()*100)

def domanda_numero():
    '''
    funzione per chiedere un numero all'utente con dei check inclusi
    '''
    risposta = input("Inserisci un numero da 1 a 100; se vuoi interrompere il gioco, digita stop: ")
    if risposta.lower() == "stop":
        return risposta
        
    # controllare sia numero - vabe magari poi aggiungo 

    risposta = int(risposta)
    # controllare sia tra 1 e 100
    if risposta > 0 and risposta < 101:
        return risposta
    else:
        print("Il numero inserito non è tra 1 e 100")
        return False


def calcola_risultato_gioco(numero_inserito, numero_da_indovinare):
    # return 1 se è pi alto, 0 se è uguale, -1 se è più basso
    if numero_da_indovinare > numero_inserito:
        return 1
    elif numero_da_indovinare < numero_inserito:
        return -1
    elif numero_da_indovinare == numero_inserito:
        return 0




continuare_gioco = True
while continuare_gioco == True:
    numero_utente = domanda_numero()
    if numero_utente == "stop":
        continuare_gioco = False
    elif numero_utente != False:
        risultato = calcola_risultato_gioco(numero_utente, numero_casuale)
        if risultato == 1:
            print("Il numero da indovinare è più alto del numero inserito")
            print()
        elif risultato == -1:
            print("Il numero da indovinare è più basso del numero inserito")
            print()
        elif risultato == 0:
            print("Hai indovinato il numero!")
            continuare_gioco = False

