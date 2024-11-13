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
