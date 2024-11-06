'''
2024.11.05 17.32

esercizio teatro

'''



class Teatro:
    '''
    classe per gestire tutte le prenotazioni (definite come oggetto Posto)
    '''
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
        if self.__test_azione_concessa(True) == True:
            self.__set_occupato(True)
        else:
            print("posto occupato! Impossibile prenotare!")

    def libera(self):
        self.__set_occupato(self, False)

    def get_posto(self):
        # getter per prendere numero e fila e stato di occupazione
        return (self.__numero, self.__fila, self.__occupato)
    
    def get_stato(self):
        return self.__occupato

    def __set_occupato(self, stato):
        self.__occupato = stato
    
    def __test_azione_concessa(self, occupato):
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

    def __init__(self, numero, fila, occupato)
        Posto.__init__(self, numero, fila, occupato)
        self.servizi_extra = 'Nessun servizio extra'

    def prenota():
            '''
            questo blocco (che è Posto.prenota()):
            if self.__test_azione_concessa(True) == True:
            self.__set_occupato(True)
        else:
            print("posto occupato! Impossibile prenotare!")

            lo devo riscrivere qui 

            o posso chiamare semplicemente la "prenota()" del padre (Posto) qui dentro
            in modo che esegua quel blocco di codice: 

            prenota()
            '''

        # e successivamente aggiungere servizio extra
        # blocco di codice per impostare servizio extra
        # servizio extra ........



class PostoStandard(Posto):
    '''
    classe derivata figlia di Posto per i posti standard
    '''
    pass




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
print("set libero tramite __set_occupato")
mio_posto._Posto__set_occupato(False)

print("info posto:")
print(mio_posto.get_posto())

# provo a prenotare quando è libero
print("prenota")
mio_posto.prenota()
print("info posto:")
print(mio_posto.get_posto())