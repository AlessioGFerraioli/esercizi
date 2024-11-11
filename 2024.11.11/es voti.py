'''

Create un programma di gestione scolastica che utilizza un file txt come database, potrete aggiungere o eliminare un alunno e i suoi voti
'''


class GestoreVoti:
    
    def __init__(self, nome_file):
        self.registro_voti = {}#{nome:lista_voti}
        self.nome_file = nome_file
        self.leggi_file()
        print(f"init: {self.registro_voti}")
        

    def visualizza_voti(self, nome):
        print(self.registro_voti[nome])

    def registra_nuovo_studente(self, nome, lista_voti):
        print(f"prima di leggi file: {self.registro_voti}")

        self.leggi_file()
        print(f"dopo di leggi file: {self.registro_voti}")

        if nome not in self.registro_voti.keys():
            self.registro_voti[nome] = lista_voti
        else:
            print(f"Studente con nome {nome} esiste già.")
        self.aggiorna_file()
        print(f"dopo di aggiorna file: {self.registro_voti}")
    
    def elimina_studente(self, nome):
        self.leggi_file()
        if nome in self.registro_voti.keys():
            self.registro_voti.pop(nome)
        else:
            print(f"Nessuno studente di nome {nome}")
        self.aggiorna_file()

    def aggiorna_file(self):
        stringa = ''
        for nome in self.registro_voti.keys():
            stringa = stringa+f"{nome},"
            for voto in self.registro_voti[nome]:
                stringa = stringa+f"{voto},"
            stringa = stringa + "\n"
        # sovrascrivi file
        with open(self.nome_file, "w") as nome_file:
            testo_file = nome_file.write(stringa)

    def leggi_file(self):
        print(f"all'interno di leggi_file prima di aprire il file: {self.registro_voti}") # qua lo legge bene
        with open(self.nome_file, "r") as nome_file:
            righe_file = nome_file.readlines()

        # svuoto il dizoinario per sovrascrivlo con quello del file
        self.registro_voti = {}
        print(f"righe_file : {righe_file}")

        if len(righe_file) > 1:
            # scrivo il dizionario uno studente alla volta
            for riga in righe_file:
                nome = riga[0][:-1]
                voti = []
                for voto in riga[1:]:
                    voti.append(voto[:-1])
                self.registro_voti.update({nome : voti})
        elif len(righe_file) == 1:
            nome = righe_file[0][:-1]
            voti = []
            for voto in righe_file[1:]:
                voti.append(voto[:-1])
            self.registro_voti.update({nome : voti})


        elif len(righe_file) == 0:
            pass


        

        print(f"all'interno di leggi_file dopo aver letto il file: {self.registro_voti}")



    def visualizza_voti(self, nome):
        self.leggi_file()
        pass



    '''
    def aggiungi_voto_a_studente(self, nome, voto):
        self.leggi_file()
        self.registro_voti[nome].append(voto)
        self.aggiorna_file()
    '''
'''
class Studente:
    def __init__(self, nome):
        self.nome = nome
        self.lista_voti = []

    def aggiungi_voto(self, voto_da_aggiungere):
        self.lista_voti.append(voto_da_aggiungere)

    def visualizza_voti(self):
        print(self.lista_voti)
'''



registro = GestoreVoti('prova.txt')

#registro.registra_nuovo_studente("Giancarlo", [1,5,3])
#registro.registra_nuovo_studente("Cosimo", [10,10,10])
registro.registra_nuovo_studente("Lorenzo", [100,100,100])