'''
# 2024.10.29 esercizio range 1


TRACCIA 
Chiedi all'utente di inserire un numero. 
Il programma dovrebbe quindi fare un conto alla rovescia a partire da 
quel numero fino a zero, stampando ogni numero.
 e chiederti se vuoi ripetere o no Chiedi all'utente di inserire un numero.


 

workflow

chiedi all'utente di inserire un numero
stampare il countdown da quel numero a zero
alla fine, chiedere all'utente se vuole inserire un nuovo numero o fermarsi

'''



# ciclo per far inserire il numero all'utente
continuare_gioco = True
# chiedi il numero all'utente
while continuare_gioco == True:
    numero = input('Inserisci un numero intero: ')
    # controllare che sia stato inserito un int
    if isinstance(numero, int):     
        # ciclo per stampare il countdown
        print("Countdown: ")
        for numero_stampa in range(numero, 0, -1):
            print(numero_stampa)
        # fine countdown, richiesta di continuare
        risposta = input("Countdown finito. Vuoi inserire un nuovo numero? y/n")
        risposta = risposta.lower()
        if not((risposta == "y") or (risposta == "yes")):
            continuare_gioco = False
        
    
    # caso in cui non sia stato inserito un intero
    else: 
        risposta = input("Il valore inserito non è un numero intero. Vuoi inserire un nuovo numero? y/n")
        risposta = risposta.lower()
        if not((risposta == "y") or (risposta == "yes")):
            continuare_gioco = False
