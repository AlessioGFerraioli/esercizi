



class Utenti:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.punteggio = 0



#classe per gestire il sistema di registrazione -- simone
class Sistema:
    def init(self):
        #lista per memorizzare gli utenti registrati
        self.lista_utenti =[]

    def registrazione(self):
        print("Benvenuto nella fase di registrazione!")

        while True:
            username = input("Inserisci un nome utente: ")

            #controlla se l'utente è gia registrato (any)
            if any(utente.username == username for utente in self.lista_utenti):
                print("Nome utente già esistente. Scegli un altro nome utente.")
            else:
                break

        password = input("Inserisci una password: ")

        #crea un nuovo oggetto utente e lo aggiunge alla lista
        nuovo_utente = Utente(username, password)
        self.lista_utenti.append(nuovo_utente)

        print(f"Registrazione completata! Benvenuto/a {username}.")

    def mostra_utenti(self):
        print("Utenti registrati:")
        for utente in self.lista_utenti:
            print(f"- {utente.username}")


    #funzione login - alessandro 
    def login(self):
        while True:
                nomeutente_login = input("Inserisci il tuo nome utente: ")
                password_login = input("Inserisci la tua password: ")
                if utente.nome_utente == nomeutente_login and utente.password == password_login:
                    loggato = True
                    return nomeutente_login
                else:
                    print("Credenziali errate! Riprova!") 
                    loggato = False

                if loggato == True:
                    break

    
    def accesso(self):
        username = login()
        username = lista_utenti
        if username is not None:
            gioco()

    

    def stampa_classifica(lista_utenti):
            #li ordino in ordine decrescente

            for i in range(len(lista_utenti)): 
                for j in range(0,len(lista_utenti)-1-i):
                    if lista_utenti[j].punteggio < lista_utenti[j+1].punteggio: 
                        #scambio di posizione se l'ogggetto successivo è maggiore

                        lista_utenti[j],lista_utenti[j+1]= lista_utenti[j+1],lista_utenti[j]
            print("Classifica : \n")
            for x in range(1,len(lista_utenti)+1):
                print(f"{x}.Nome : {lista_utenti[x].username} - Punteggio : {lista_utenti[x].punteggio}")





# creo un sistema di archivio utenti
archivio_utenti = Sistema()

# booleana per segnalare se il programma deve continuare
continuare_gioco = True
# ciclo principale del programma 
while continuare_gioco == True:

    risposta = input("Digita a per accedere, r per registrare nuovo utente, c per visualizzare la classifica, q per uscire: ").lower()
    if risposta == "r":
        archivio_utenti.registrazione()
    elif risposta == "a":
        archivio_utenti.accesso()
    elif risposta == "c":
        archivio_utenti.stampa_classifica()
    elif risposta == "q":
        continuare_gioco == True
        
        