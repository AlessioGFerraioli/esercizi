'''
2024.10.30 16.24

esercitazione base su decoratori

esercizio 

chiedi un nome
chiedi un numero

funzione primo_o_no che determina se è primo
    deve restiture True se è primo, false altrimento

Se è primo lo salva e continua il ciclo richiededno un nuovo numero
altrimenti ti dice quanto volte sta nel divisore piu piccolo


'''

def continuare_gioco(gioco):
    def wrapper(*args, **kwargs):
        gioco(*args, **kwargs))
        risposta = input("vuoi continuare a giocare? y/n ")
        if risposta == 'y' :
            
        return False
    return wrapper

def gioco():
    print("sto giocando..")
    
    
