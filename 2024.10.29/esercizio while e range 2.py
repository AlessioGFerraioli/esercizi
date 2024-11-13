'''
2024.10.29 esercizio range 2
Il programma dovrebbe controllare se il numero inserito è primo o no.
Se è primo, lo salva e stampa "Il numero è primo".
 Altrimenti, stampa "Il numero non è primo". si ferma il tutto quando ha 5 numeri primi

'''


# inizializzo il conto di quanti numeri primi sono stati inseriti
counter_numeri_primi = 0  


# ciclo per far inserire il numero all'utente
# chiedi il numero all'utente
while counter_numeri_primi < 5: 
    numero = int(input('Inserisci un numero primo: '))
    # controllare se il numero è primo
    # inizializzo lista divisori
    divisori = []
    for i in range(1, numero+1):
        if numero % i==0:
            divisori.append(i)
    # se i divisori sono solo 1 e il numero stesso allora il numero è primo 
    if len(divisori) < 3:
        if counter_numeri_primi == 5:
            print("Questo è un numero primo! Hai completato l'esercizio.")
        else:
            print(f"Questo è un numero primo! Ne mancano ancora "+5-counter_numeri_primi)
            counter_numeri_primi += 1









