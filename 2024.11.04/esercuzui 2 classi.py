'''


'''


class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def show_info(self):
        print(f"Il libro", self.titolo, "è stato scritto da", self.autore,"e ha ", self.pagine," pagine.")

libro_alessio = Libro("La mia vita", "Alessio", "0")

libro_alessio.show_info()