'''

Create un programma di gestione scolastica che utilizza un file txt come database, potrete aggiungere o eliminare un alunno e i suoi voti

l'utente deve poter:
- aggiungere, rimuovere o aggiornare voti
- aggiungere, rimuovere o aggiornare alunni
- aggiungere la possibilità di stampare nome alunno e sua media

'''


class GestoreVoti:
    
    def __init__(self, nome_file):
        self.registro_voti = {}#{nome:lista_voti}
        self.nome_file = nome_file
        self.leggi_file()
        
    def visualizza_voti(self, nome):
        print(self.registro_voti[nome])

    def registra_nuovo_studente(self, nome, lista_voti):
        self.leggi_file()
        if nome not in self.registro_voti.keys():
            self.registro_voti[nome] = lista_voti
        else:
            print(f"Studente con nome {nome} esiste già.")
        self.aggiorna_file()
    
    def aggiungi_studente(self, nome):
        self.registra_nuovo_studente(nome, lista_voti=[])

    def elimina_studente(self, nome):
        self.leggi_file()
        if nome in self.registro_voti.keys():
            self.registro_voti.pop(nome)
            print(f"Studente {nome} eliminato.")
        else:
            print(f"Nessuno studente di nome {nome}")
        self.aggiorna_file()

    def aggiorna_file(self):
        stringa = ''
        n_studenti = len(self.registro_voti.keys())
        i = 0
        for nome in self.registro_voti.keys():
            stringa = stringa+f"{nome},"
            n_voti = len(self.registro_voti[nome])
            j = 1
            for voto in self.registro_voti[nome]:
                if j != n_voti:
                    stringa = stringa+f"{voto},"
                else:
                    stringa = stringa+f"{voto}"
                j += 1
            i += 1 
            if i != n_studenti:
                stringa = stringa + "\n"
        # sovrascrivi file
        with open(self.nome_file, "w") as nome_file:
            testo_file = nome_file.write(stringa)

    def leggi_file(self):      
        with open(self.nome_file, "r") as nome_file:
            righe_file = nome_file.readlines()
        # svuotiamo il dizoinario esistente per scriverne uno nuovo
        self.registro_voti.clear()
        for riga in righe_file:
            # epariamo per la virgola
            dati = riga.strip().split(",") 
            # primo elemento è il nome dello studente
            nome = dati[0]
            # Convertiamo i voti in interi
            voti = list(map(int, dati[1:])) 
            voti = list(dati[1:])
            self.registro_voti[nome] = voti
      
    def visualizza_voti(self, nome):
        self.leggi_file()
        pass

    def aggiungi_voto_a_studente(self, nome, voto):
        self.leggi_file()
        if nome not in self.registro_voti.keys():
            print(f"Non esiste studente {nome}.")
        else:
            self.registro_voti[nome].append(voto)
            print(f"Aggiunto voto {voto} a studente {nome}.")
        self.aggiorna_file()

    def media_voti(self, nome):
        voti = self.registro_voti[nome]
        voti = list(map(int, voti)) 

        return sum(voti)/len(voti)

    def visualizza_medie_voti(self):
        print("Media voti alunni")
        print("Nome : Media")
        for nome in self.registro_voti.keys():
            print(f"{nome} : {self.media_voti(nome)}")
    


registro = GestoreVoti('voti.txt')

#registro.registra_nuovo_studente("Giancarlo", [1,5,3])
#registro.registra_nuovo_studente("Cosimo", [10,10,10])
#registro.registra_nuovo_studente("Lorenzo", [100,100,120])

#registro.registra_nuovo_studente("Alessio", [0,0,0])


#registro.aggiungi_voto_a_studente("Lorenzo", 1000)

#registro.visualizza_medie_voti()

registro.elimina_studente("Alessio")