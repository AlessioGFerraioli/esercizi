'''
2024.10.29
Esercizio su Python: Cicli e Condizioni
Punto 1: Utilizzo di if
Scrivi un sistema che prende in input un numero e stampa "Pari"
 se il numero è pari e "Dispari" se il numero è dispari.

Punto 2: Utilizzo di while e range
Scrivi un sistema che prende in input un numero intero positivo n e
 stampa tutti i numeri da n a 0 (compreso), decrementando di 1.Deve potersi ripete all’infinito

Punto 3: Utilizzo di for
Scrivi un sistema che prende in input una lista di numeri e
 stampa il quadrato di ciascun numero nella lista.

Punto 4: Utilizzo di if, while e for insieme Scrivi un sistema che prende in input una lista di numeri interi che precedente è stata valorizzata dall’utente.
Il sistema deve:
Utilizzare un ciclo for per trovare il numero massimo nella lista.
Utilizzare un ciclo while per contare quanti numeri sono presenti nella lista.
Utilizzare una condizione if per stampare "Lista Vuota" se la lista è vuota, altrimenti 
stampare il numero massimo trovato e il numero di elementi nella lista.

'''


'''
esercizio completo 
punto 1 utilizzo di if


scrivi un sistema che prende in inpuit un numero e stampa pari se il numero è pari
e dispari se il numero è dispari


'''

# ciclo per far inserire il numero all'utente
continuare_gioco = True
# chiedi il numero all'utente
while continuare_gioco == True:
    numero = int(input('Inserisci un numero intero positivo: '))
    # controllare che sia stato inserito un numero positivo
    if numero > 0:
        if numero%2 == 0:     
            print("Pari")
        else:
            print("Dispari")
        risposta = input("Vuoi inserire un nuovo numero? y/n")
        risposta = risposta.lower()
        if not((risposta == "y") or (risposta == "yes")):
            continuare_gioco = False
        
    # caso in cui non sia stato inserito un positivo
    else: 
        risposta = input("Il valore inserito non è un numero positivo. Vuoi inserire un nuovo numero? y/n")
        risposta = risposta.lower()
        if not((risposta == "y") or (risposta == "yes")):
            continuare_gioco = False


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


'''
esercizio completo 
punto 3 utilizzo di for

scrivi un sistema che prende in input una lsita di numeri
e stampa il quadrato di ciascun numero
nella lista
'''



# inizializzo lista vuota per i numeri utente
lista_utente = []

continuare_ad_aggiungere = True

# chiedo all'utente di inserire i numeri 
while continuare_ad_aggiungere == True:
    lista_utente.append(float(input("Inserisci un numero: ")))
    risposta = input("Vuoi aggiungere altri numeri alla lista? y/n ")
    risposta = risposta.lower()
    if not((risposta == "y") or (risposta == "yes")):
        continuare_ad_aggiungere = False

#calcolo i quadrati salvandoli in una nuova lista
lista_quadrati = []
for numero in lista_utente:
    lista_quadrati.append(numero**2)
print(f"Lista numeri al quadrato: ")
print(lista_quadrati)
    

