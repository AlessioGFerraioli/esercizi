'''
intermedio
numeri primi in un intervallo

chiedi all'utente di inserire due numeri che definiscono un itnervallo
(es 10 e 50)

stampa tutti i numeri primi
compresi in quell'intervallo

chiedi se vuoi ripetere

'''

continuare_gioco = True

# ciclo per far definire l'intervallo all'utente
while continuare_gioco == True:
    # richiedere primo estremo
    numero_1 = int(input("Inserisci un estremo dell'intervallo (numero intero): "))
    # richiedere secondo estremo
    numero_2 = int(input("Inserisci l'altro estremo dell'intervallo (numero intero): "))
    #controllare se numero_1 > numero_2, se sì scambiarli tra loro

    if numero_1 == numero_2:
            print("I due estremi sono uguali, l'intervallo è nullo.")
    else:
        if numero_1 > numero_2: 
                numero_temp = numero_2
                numero_2 = numero_1
                numero_1 = numero_temp
        # controllare se i due estremi sono uguali, se sì dire che l'intervallo è nullo

        # sezione di stampa dei numeri primi in intervallo
        # lista per i numeri primi in intervallo
        numeri_primi_in_intervallo = []
        # for per scorrere su i numeri in esame e vedere se sono primi
        for numero in range(numero_1, numero_2):
            divisori = []
            for i in range(1, numero+1):
                if numero % i==0:
                    divisori.append(i)
            # se i divisori sono solo 1 e il numero stesso allora il numero è primo 
            if len(divisori) < 3:
                numeri_primi_in_intervallo.append(numero)
        
        print("Numeri primi nell'intervallo: ")
        print(numeri_primi_in_intervallo)
        
        # fine gioco, richiesta di continuare
        risposta = input("Vuoi inserire un nuovo intervallo? y/n: ")
        risposta = risposta.lower()
        if not((risposta == "y") or (risposta == "yes")):
            continuare_gioco = False
 
            


    