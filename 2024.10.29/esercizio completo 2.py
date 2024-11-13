'''
esercizio completo 
punto 2 utilzizo di while e range

scrivi un sistema che prende in input un numero inter positivo n


e stampa tutti i numeri da n a 0 (compreso) 

decrementando di 1. 

deve potersi ripetere all'inifinito
'''

# ciclo per far inserire il numero all'utente
continuare_gioco = True
# chiedi il numero all'utente
while continuare_gioco == True:
    numero = int(input('Inserisci un numero intero positivo: '))
    # controllare che sia stato inserito un numero positivo
    if numero > 0:     
        # ciclo per stampare il countdown
        print("Countdown: ")
        for numero_stampa in range(numero, -1, -1):
            print(numero_stampa)
        # fine countdown, richiesta di continuare
        risposta = input("Countdown finito. Vuoi inserire un nuovo numero? y/n")
        risposta = risposta.lower()
        if not((risposta == "y") or (risposta == "yes")):
            continuare_gioco = False
        
    
    # caso in cui non sia stato inserito un intero
    else: 
        risposta = input("Il valore inserito non è un numeropositivo. Vuoi inserire un nuovo numero? y/n")
        risposta = risposta.lower()
        if not((risposta == "y") or (risposta == "yes")):
            continuare_gioco = False
