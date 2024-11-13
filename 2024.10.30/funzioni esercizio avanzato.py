'''

2024.10.30

def

2. esercizio avanzato: sequenza di fibonacci fino a n



'''



def domanda_numero():
    '''
    funzione per chiedere un numero all'utente con dei check inclusi
    '''
    risposta = input("Inserisci un numero positivo; se vuoi interrompere il gioco, digita stop: ")
    if risposta.lower() == "stop":
        return risposta
        
    # controllare sia numero o stringa - vabe magari poi aggiungo 

    risposta = int(risposta)
    # controllare sia tra 1 e 100
    if risposta > 0:
        return risposta
    else:
        print("Il numero inserito non è positivo")
        return False



def prossimo_numero_fibonacci(lista):
    # calcola il prossimo numero di una lista secondo la regola di fibonacci (somma degli ultimi due)
    return lista[-1] + lista[-2]


def sequenza_fibonacci_fino_a_n(n):
    '''
    calcola sequenza fibonacci fino a n, definita nella forma: 
    0 1 1 2 3 5 ..
    '''
    sequenza_fibonacci = [0, 1]
    while sequenza_fibonacci[-1] < n:
        sequenza_fibonacci.append(prossimo_numero_fibonacci(sequenza_fibonacci))
    if sequenza_fibonacci[-1] > n:
        return sequenza_fibonacci[:-1]
    else:
        return sequenza_fibonacci

def sequenza_fibonacci2_fino_a_n(n):
    '''
    calcola sequenza fibonacci fino a n, definita nella forma: 
    0 1 2 3 5 ..
    '''
    fibonacci_starter = [0, 1]
    if n == 1:
        return fibonacci_starter
    else: 
        sequenza_fibonacci = [0,1,2]
        while sequenza_fibonacci[-1] < n:
            sequenza_fibonacci.append(prossimo_numero_fibonacci(sequenza_fibonacci))
        if sequenza_fibonacci[-1] > n:
            return sequenza_fibonacci[:-1]
        else:
            return sequenza_fibonacci


continuare_gioco = True
while continuare_gioco == True:
    numero_utente = domanda_numero()
    if numero_utente == "stop":
        continuare_gioco = False
    elif numero_utente != False:
        sequenza_fibonacci = sequenza_fibonacci2_fino_a_n(numero_utente)
        print("Sequenza fibonacci: ")
        print(sequenza_fibonacci)
        
