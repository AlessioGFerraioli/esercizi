'''
Esercizio 1: Oggetti

Descrizione:  Crea un programma in Python per gestire una semplice libreria di libri.

 Il programma dovrebbe presentare un menu all'utente con le seguenti opzioni:

    Aggiungere un nuovo libro: 
        L'utente può inserire il titolo, l'autore e l'anno di pubblicazione del libro e quantità.

    Visualizzare tutti i libri: 
        Mostra una lista di tutti i libri attualmente nella libreria.

    Cercare un libro per titolo: 
        L'utente inserisce un titolo e il programma cerca e mostra i dettagli del libro se trovato.

    Gestione libri: 
        Far rimuovere modificare e/o aggiungere una compia in più del libro

    Uscire dal programma: 
        Termina l'esecuzione del programma.



'''

'''

crea una classe biblioteca 
che permetta di creare un libro e stamparlo

extra: permetti di creare quanti libri vuole l'utente (ed eventualmente stamparli)

'''



class Libro():
    def __init__(self, titolo, autore, anno, quantita):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.quantita = quantita

    def show_info(self):
        print(f"Titolo: ", self.titolo,", autore:  ", self.autore, ", anno: ", self.anno, "quantita: ", self.quantita)
        print()


class Biblioteca():
    
    lista_libri = []

    def _init__(self):
        self.lista_libri = []

    def inserisci_libro(self):
        # metodo per registrare un nuovo libro in biblioteca
        # vanno aggiunti dei controlli sugli input
        titolo = input("\nDigita titolo libro da inserire in biblioteca: ")
        autore = input("Nome autore: ")
        anno = int(input("Anno di pubblicazione: "))

        if self._libro_gia_presente(titolo, autore, anno):
            print("Libro già presente in libreria!\nVuoi aggiornare la quantità per questo libro?")
            risposta = input("y/n: ")
            if risposta.lower() == "y":
                self.aggiorna_quantita(titolo, autore, anno)
        else:
            quantita = int(input("Inserisci quantità: "))

            libro_da_inserire = Libro(titolo, autore, anno, quantita)
            self.lista_libri.append(libro_da_inserire)

    
    def stampa_biblioteca(self):
        print()
        for libro in self.lista_libri:
            libro.show_info()

    def cerca_libro(self):
        print()
        keyword = input("Digita una parola chiave di ricerca: ")
        risultati_ricerca = []
        for libro in self.lista_libri:
            if keyword in libro.titolo or keyword in libro.autore:
                risultati_ricerca.append(libro)
        
        print(f"La ricerca ha prodotto ", len(risultati_ricerca), "risultati: ")
        if len(risultati_ricerca) > 0:
            for libro in risultati_ricerca:
                libro.show_info()
        print()


    def _libro_gia_presente(self, titolo, autore, anno):
        for libro in self.lista_libri:
            if (titolo == libro.titolo) and (autore == libro.autore) and (anno == libro.anno):
                return True
        return False

    def aggiorna_quantita(self, titolo=None, anno=None, autore=None): 
        # metodo per aggiornare la quantità di un libro esistente
        # vanno aggiunti dei controlli sugli input
        if titolo is None:
            titolo = input("Digita titolo libro: ")
        if autore is None:
            autore = input("Nome autore: ")
        if anno is None:
            anno = int(input("Anno di pubblicazione: "))
    
        if self._libro_gia_presente(titolo, autore, anno):
            nuova_quantita = int(input("Nuova quantità: "))
            self._cambia_quantita(titolo, autore, anno, nuova_quantita)
            print("Quantita aggiornata.\n")
        else:
            print("Libro non trovato!")
            

    def _cambia_quantita(self, titolo, autore, anno, nuova_quantita):
        for libro in self.lista_libri:
            if (titolo == libro.titolo) and (autore == libro.autore) and (anno == libro.anno):
                libro.quantita = nuova_quantita
                


la_mia_biblioteca = Biblioteca()

# booleana per segnalare se il programma deve continuare
continuare_gioco = True
# ciclo principale del programma 
while continuare_gioco == True:
    print("Sistema Biblioteca")
    print()
    print("Digita: ")
    print("i per inserire un nuovo libro")
    print("a per aggiornare quantità di un libro presente in biblioteca")
    print("c per cercare un libro presente in biblioteca")
    print("s per stampare la lista di tutti i libri in biblioteca")
    print("q per uscire")
    risposta = input(": ").lower()
    if risposta == "i":
        la_mia_biblioteca.inserisci_libro()
    elif risposta == "c":
        la_mia_biblioteca.cerca_libro()
    elif risposta == "a":
        la_mia_biblioteca.aggiorna_quantita()
    elif risposta == "s":
        la_mia_biblioteca.stampa_biblioteca()
    elif risposta == "q":
        continuare_gioco = False
    print()
        

