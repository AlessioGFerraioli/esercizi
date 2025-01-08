"""
2024.11.11 10.47
part 2 il programma legge il file e l’utente dovrà cercare di indovinarne 
almeno 2 numero oppure avrà perso.
"""


class IndovinaGioco:
        def __init__(self, filename):
            self.filename = filename
            self.numeri = self.read_numbers_from_file(self.filename)
        
        def read_numbers_from_file(self, filename):
            # leggo numeri dal file (separati da virgola)
            with open('file_esercizio_es_file.txt', "r") as filename:
                numeri = filename.read()
            filename.close()
            # rimuovo virgola finale
            numeri = numeri[:-1]
            # separo in corrispondenza delle virgole
            numeri = numeri.split(",")
            # converto in int
            numeri_int = [int(num) for num in numeri]
            numeri = numeri_int

            return numeri
               
        def start_gioco(self):
            print("Indovina 2 numeri tra 1 e 20")
            tentativi = 5
            risposte_corrette = 0
            for tentativo in range(tentativi):
                risposta = int(input(": "))
                if risposta in self.numeri:
                    print("Indovinato numero!")
                    self.numeri.remove(risposta)
                    risposte_corrette = risposte_corrette+1
                else:
                    print("Risposta errata!")
                    tentativi = tentativi-1
                    print(f"Ti restano {tentativi} tentativi")
                if risposte_corrette == 2:
                    print("Hai vinto!")
                    break
            if tentativi == 0: print("Hai perso!")


gioco = IndovinaGioco("file_esercizio_es_file.txt")
gioco.start_gioco()