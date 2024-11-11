'''
2024.11.11 12.00

Create un file.txt con uno script python e testo preso da https://it.lipsum.com/ , dopo
averlo fatto scrivete un programma che legge il documento e ci restituisce 
il numero di parole, 
righe
 e caratteri.

'''



lorem_ipsum = """

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis lacus arcu, mattis sit amet dolor eu, porta ultrices ligula. Aenean a faucibus nisi. Aenean vitae est libero. Fusce commodo quis libero vitae accumsan. Aliquam velit odio, tristique sed nisi id, interdum aliquet est. Vestibulum scelerisque mollis mauris vitae rutrum. Nullam porta ligula nec sapien hendrerit, a dictum metus varius. Nunc et elit placerat, pulvinar est ultricies, ullamcorper dolor. Integer eget varius lectus, eget malesuada quam. Morbi ac venenatis turpis. Nulla sit amet sodales augue, et consectetur augue. Cras ante turpis, pulvinar eu vulputate sed, varius eget nisi. Duis ut nunc cursus, lobortis justo quis, dignissim massa.

Fusce ultricies, mi vitae fringilla luctus, turpis nisl posuere turpis, quis congue dui est at lectus. Morbi id placerat lorem. Quisque a sem nec tellus sollicitudin placerat id eget nisl. Donec faucibus massa eget metus auctor maximus. Vestibulum in mauris a ipsum lacinia commodo at a nulla. Pellentesque eros massa, lacinia eu eros a, tempus scelerisque ipsum. Nulla porttitor finibus massa ut condimentum. Nunc vulputate est vitae tellus malesuada, in pellentesque nibh condimentum. Vivamus pretium id justo non ornare. Praesent et pretium justo. Vestibulum non lectus laoreet, convallis metus scelerisque, volutpat orci. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aliquam neque nisi, maximus ut tellus vel, commodo rhoncus tortor. Nulla scelerisque quam vel velit semper condimentum. Fusce eget commodo sem. Maecenas pretium lacinia odio, eget mollis sem venenatis et.

Praesent efficitur luctus vulputate. Vivamus enim massa, pharetra sit amet sapien at, iaculis pellentesque dolor. Aenean maximus tortor dapibus nunc hendrerit, et cursus lectus posuere. Sed aliquam orci eu cursus feugiat. Nam finibus, orci vitae lobortis rutrum, nulla tortor vehicula nisi, a viverra nisi orci a nisi. Donec consectetur posuere porttitor. Etiam non laoreet magna. Maecenas posuere fermentum leo tincidunt tempus. Sed ut varius tortor. Phasellus fringilla vitae arcu ut commodo. Vestibulum sed vehicula tortor. Pellentesque eget malesuada arcu, quis fringilla lacus. Pellentesque semper, metus sit amet sodales sagittis, arcu erat cursus quam, eu venenatis leo tortor in arcu.

Integer at felis luctus sapien volutpat pulvinar sit amet at velit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Curabitur non dolor fringilla, ullamcorper sem auctor, viverra sapien. Maecenas quis tellus ullamcorper, fringilla augue quis, hendrerit libero. Quisque risus magna, faucibus id lectus sit amet, sodales hendrerit nisl. Nulla mi augue, aliquet sit amet egestas eu, malesuada non ante. In tristique aliquet est, sed facilisis odio posuere nec. Mauris in sapien in quam scelerisque rhoncus.

Morbi pulvinar, massa a hendrerit condimentum, augue leo consequat lacus, in posuere tellus nisl nec ipsum. Proin ultrices augue ante, ac fringilla orci rutrum et. Aliquam erat volutpat. Proin erat mauris, pellentesque ut est eget, pulvinar iaculis augue. Mauris consectetur massa sodales lobortis porta. Phasellus iaculis vel arcu ut fringilla. Sed malesuada arcu a justo sollicitudin, non fermentum lacus semper. Duis eleifend urna vel venenatis interdum. Morbi suscipit nulla in rhoncus pellentesque. Nullam pretium risus sit amet vehicula mattis. Vivamus pharetra ipsum vitae nunc congue mollis. Proin vulputate lorem lectus, ut condimentum eros commodo at. Etiam elementum efficitur turpis. Sed volutpat enim quis sem elementum, vel vestibulum dolor cursus.

"""


with open("testo_lorem_ipsum.txt", "w") as filename:
    filename.write(lorem_ipsum)



class LettoreTesti:

    def __init__(self, filename):
        self.filename = filename
        self.testo = self.read_from_file(filename)

    def read_from_file(self, filename):
        # leggi file con nome filename
        with open(filename, "r") as nome_file:
            testo = nome_file.read()
        return testo
    
    def print_testo(self):
        # visualizza tutto il testo
        print(self.testo)

    def conta_righe(self):
        righe = self.testo.splitlines()
        n_righe = 0
        for riga in righe:
            if riga == "":
                pass
            else:
                n_righe += 1
        print(f"numero righe: {n_righe}")

    def conta_parole(self):        
        parole = self.testo.split()
        n_parole = len(parole)
        print(f"numero parole: {n_parole}")
   
    def conta_caratteri(self):  
        n_caratteri = 0    
        for carattere in self.testo:
            if carattere != " " and carattere != "\n":
                n_caratteri += 1
        print(f"numero caratteri: {n_caratteri}")

il_mio_lettore = LettoreTesti("testo_lorem_ipsum.txt")
il_mio_lettore.print_testo()
il_mio_lettore.conta_parole()
il_mio_lettore.conta_righe()
il_mio_lettore.conta_caratteri()