'''

crea una classe biblioteca 
che permetta di creare un libro e stamparlo

extra: permetti di creare quanti libri vuole l'utente (ed eventualmente stamparli)

'''



class Libro():
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def show_info(self):
        print(f"Titolo: ", self.titolo,", autore:  ", self.autore, ", n. pagine: ", self.pagine)
        print()


class Biblioteca():
    
    lista_libri = []

    def _init__(self):
        self.lista_libri = []

    def inserisci_libro(self):
        print()
        # metodo per registrare un nuovo libro in biblioteca
        # vanno aggiunti dei controlli sugli input
        titolo = input("Digita titolo libro da inserire in biblioteca: ")
        autore = input("Nome autore: ")
        pagine = int(input("Numero pagine: "))

        libro_da_inserire = Libro(titolo, autore, pagine)
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



la_mia_biblioteca = Biblioteca()

# booleana per segnalare se il programma deve continuare
continuare_gioco = True
# ciclo principale del programma 
while continuare_gioco == True:
    print("Sistema Biblioteca")
    print()
    print("Digita: ")
    print("i per inserire un nuovo libro")
    print("c per cercare un libro presente in biblioteca")
    print("s per stampare la lista di tutti i libri in biblioteca")
    print("q per uscire")
    risposta = input(": ").lower()
    if risposta == "i":
        la_mia_biblioteca.inserisci_libro()
    elif risposta == "c":
        la_mia_biblioteca.cerca_libro()
    elif risposta == "s":
        la_mia_biblioteca.stampa_biblioteca()
    elif risposta == "q":
        continuare_gioco = False
    print()
        
