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
    def __init__(self):
        pass

    def prenota(self):
        if __test_azione_concessa(self, occupato=True) == True:
            self.__set_occupato(self, True)
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
    '''
    pass

class PostoStandard(Posto):
        '''
    classe derivata figlia di Posto per i posti standard
    '''
    pass