'''
2024.11.05 17.32

esercizio teatro

'''



class Teatro:
    '''
    classe per gestire tutte le prenotazioni (definite come oggetto Posto)
    '''

    __posti_obj = {}
    def __init__(self, posti):
        # posti è un dict (codice_posto:tipologia)
        self._posti = posti
        # creo oggetti posto per ogni posto fornito all'init (settandoli non occupati in partenza)
        for codice_posto in posti.keys():
            # separa codice posto in numero e fila
            numero = codice_posto[1]
            fila = codice_posto[0]
            # controlla il tipo di posto e crea oggetto postostandard o vip
            if posti[codice_posto] == 'std':
                self.__posti_obj[codice_posto] = PostoStandard(numero, fila, occupato=False)
            if posti[codice_posto] == 'vip':
                self.__posti_obj[codice_posto] = PostoVIP(numero, fila, occupato=False)


    def prenota_posto(self, codice_posto):
        #codice_posto = fila+numero
        print(f"Ricerca posto {codice_posto}..")
        self.__posti_obj[codice_posto].prenota()
        
    
    def stampa_tutti_posti(self):
        print("Stampa tutti i posti:")
        print(posti)


    def stampa_posti_occupati(self): 
        # mostra tutti i posti occupati
        pass



class Posto:
    '''
    classe padre per tutti i tipi di Posto del teatro

    attributi privati: 
        __numero (intero, numero del posto)
        __fila (stringa, fila in cui trova il posto)
        __occupato (booleano: stato del posto, occupato o libero)

    metodi:
        prenota(): prenota il posto SE non è gia occupato
        libera(): libera il posto SE è occupato
        getter per numero e fila e uno stato che indica se il posto è occupato.
    '''
    def __init__(self, numero, fila, occupato):
        self.__numero = numero
        self.__fila = fila
        self.__occupato = occupato

    def prenota(self):
        if self.test_azione_concessa(True) == True:
            self.set_occupato(True)
            return True
        else:
            print("Posto occupato! Impossibile prenotare!")
            return False

    def libera(self):
        self.set_occupato(self, False)

    def get_posto(self):
        # getter per prendere numero e fila e stato di occupazione
        return (self.__numero, self.__fila, self.__occupato)
    
    def get_stato(self):
        return self.__occupato

    def set_occupato(self, stato):
        self.__occupato = stato
    
    def test_azione_concessa(self, occupato):
        if self.get_stato() == occupato:
            azione_concessa = False
        else:
            azione_concessa = True
        return azione_concessa
        
        

class PostoVIP(Posto):
    '''
    classe derivata figlia di Posto per i posti VIP
    aggiunge attributo servizi_extra 
    sovrascive il metodo prenota() per gestire i servizi extra
    '''

    servizi_extra = 'Nessun servizio extra'

    def __init__(self, numero, fila, occupato):
        Posto.__init__(self, numero, fila, occupato)
        self.servizi_extra = 'Nessun servizio extra'


    def prenota(self):

        '''
            questo blocco (che è Posto.prenota()):
            if self.test_azione_concessa(True) == True:
            self.set_occupato(True)
        else:
            print("posto occupato! Impossibile prenotare!")

            lo devo riscrivere qui 

            o posso chiamare semplicemente la "prenota()" del padre (Posto) qui dentro
            in modo che esegua quel blocco di codice: 

          prenota()
        '''
        prenotazione_avvenuta = Posto.prenota(self)

        if prenotazione_avvenuta:
            # blocco di codice per impostare servizio extra
            print("Prenotato posto VIP")
            servizio_extra = input("Inserisci servizio extra: ")
            self.servizi_extra = servizio_extra
            print(f"Servizio extra {servizio_extra} aggiunto.")
        
        print()

class PostoStandard(Posto):
    '''
    classe derivata figlia di Posto per i posti standard
    '''

    def __init__(self, numero, fila, occupato):
        Posto.__init__(self, numero, fila, occupato)


    def prenota(self):
        '''
            questo blocco (che è Posto.prenota()):
            if self.test_azione_concessa(True) == True:
            self.set_occupato(True)
        else:
            print("posto occupato! Impossibile prenotare!")

            lo devo riscrivere qui 

            o posso chiamare semplicemente la "prenota()" del padre (Posto) qui dentro
            in modo che esegua quel blocco di codice: 

          prenota()
        '''
        prenotazione_avvenuta = Posto.prenota(self)

        if prenotazione_avvenuta:
            # blocco di codice per impostare servizio extra
            print("Prenotato posto standard")        
        print()
 
 

'''
# esempio di utilizzo 
mio_posto = Posto(4, "C", True)

print("info posto:")
print(mio_posto.get_posto())

# provo a prenotare quando è gia occupato
print("prenota")
mio_posto.prenota()
print("info posto:")
print(mio_posto.get_posto())

# esempio di accesso "forzato" a metodo privato
print("set libero tramite set_occupato")
mio_posto._Postoset_occupato(False)

print("info posto:")
print(mio_posto.get_posto())

# provo a prenotare quando è libero
print("prenota")
mio_posto.prenota()
print("info posto:")
print(mio_posto.get_posto())

'''

posti = {"A1" : "std", "A2": "std", "A3" : "std",
         "B1" : "vip", "B2" : "vip", "B3" : "vip", "B4" : "vip",
         "C1" : "std", "C2" : "std", "C3" : "std"}

teatro_alessione = Teatro(posti)

teatro_alessione.stampa_tutti_posti()

print("provo a prenotare A2 (std)")
teatro_alessione.prenota_posto("A2")

print("provo a prenotare B3 (vip)")
teatro_alessione.prenota_posto("B3")

