'''
creare pagina login
chiede inizialmente se vuole registrare nuovo utente o accedere

nel caso vuole registrare nome utente ,
chiedere di scegliere nome utente e passw
e salvarlo

nel caso vuole fare il login,
richiedere nome utente e password

se corretti, fmessaggio di avvenuto accesso (personalizzato)

consentire di giocare a un giochino 
o fare il logout
'''

def gioco_indovina_numero():

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


def registrazione(utenti):
    # richiedere username e passworda all'utente
    username = input("Scegli il tuo username : ")
    if username in utenti.keys():
        print("Esiste già un utente con questo username.")
        print()
    else:
        password = input("Scegli la tua password: ")

        #aggiungerli al dizionario
        utenti[username] = password
    return utenti


def giochino():
    print("giochino 8====D") 


def login(utenti):
    # richiedere username
    username = input("Username : ")
    if username not in utenti.keys():
        print("Non esiste nessun utente con questo username.")
        print()
        return False
    else: 
        password = input("Password: ")
        if password == utenti[username]:
            return (username, password)
        else:
            print("Password errata.")
            print()
            return False


def accesso(utenti):
    # inserire il login
    utente_corrente = login(utenti)
    if utente_corrente != False:
        print(f"Ciao ",utente_corrente[0],", la tua password è ",utente_corrente[1],", ma non dirla in giro!")
        risposta = input("Digita g per giocare o u per uscire ")
        if risposta.lower() == 'g':
            gioco_indovina_numero()
        elif risposta.lower() == 'u':
            utente_corrente != False




# userò un dizionario del tipo utenti = {username:password, username:password ecc}
utenti = {}

continuare = True
while continuare == True:
    print()
    print("Pagina di Login")
    risposta = input("Digita a per accedere, r per registrare un nuovo utente, q per chiudere. ")
    if risposta.lower() == "r":
        utenti = registrazione(utenti)
    elif risposta.lower() == 'a': 
        accesso(utenti)
    elif risposta.lower() == 'q': 
        #interrompere il ciclo
        continuare = False
    else:
        print("Il carattere digitato non è tra quelli riconosciuti.")
        print()
