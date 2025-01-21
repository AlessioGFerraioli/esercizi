import requests as rq
import random
import json
import os
import time

# (1)
class Pokemon:
    def __init__(self, id, nome, abilita, peso, xp, altezza, hp, attack, speed, defense):
        ''' costruttore della classe '''
        self.id = id
        self.nome = nome
        self.abilita = abilita
        self.peso = peso
        self.xp = xp
        self.altezza = altezza
        self.hp = hp
        self.attack = attack
        self.speed = speed
        self.defense = defense

    def __str__(self):
        ''' formattazione della stringa con i dati del pokemon '''
        return (f'ID: {self.id}, Nome: {self.nome}, Abilità: {self.abilita}, '
                f'Peso: {self.peso/10} Kg, XP: {self.xp}, Altezza: {self.altezza/10}m; '
                f'HP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}')

# (2)
class Pokedex:
    def __init__(self, file_path='pokedex.json'):
        ''' costruttore della classe '''
        self.file_path = file_path
        self.box_pokemon = {}

    def load(self):
        ''' carica dal file i pokemon posseduti dal giocatore'''
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save(self, data):
        ''' salva sul file i pokemon posseduti dal giocatore '''
        self.box_pokemon = self.load()
        self.box_pokemon[list(data.keys())[0]] = data
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.box_pokemon, f, indent=4)

    def is_in_pokedex(self, pokemon_id):
        ''' controlla se un pokemon è posseduto dal giocatore '''
        return self.load().get(pokemon_id) is not None

# (3)
class Battaglia:
    def __init__(self, pokemon_giocatore, pokemon_avversario):
        ''' costruttore della classe '''
        self.pokemon_giocatore = pokemon_giocatore
        self.pokemon_avversario = pokemon_avversario

    def inizia_battaglia(self):
        ''' funzione che inizia e gestisce la battaglia '''
        hp_giocatore = self.pokemon_giocatore.hp
        hp_avversario = self.pokemon_avversario.hp
        turno_giocatore = True if self.pokemon_giocatore.speed > self.pokemon_avversario.speed else False

        while hp_giocatore > 0 and hp_avversario > 0:
            time.sleep(1)
            if turno_giocatore:
                hp_avversario = self.attacco(self.pokemon_giocatore, self.pokemon_avversario, hp_avversario)
                if hp_avversario <= 0:
                    return True
            else:
                hp_giocatore = self.attacco(self.pokemon_avversario, self.pokemon_giocatore, hp_giocatore)
                if hp_giocatore <= 0:
                    return False
            turno_giocatore = not turno_giocatore

    @staticmethod
    def attacco(attaccante, difensore, hp_difensore):
        ''' funzione per effettuare un attacco e calcolare danno e hp risultanti '''
        print(f'\n-{attaccante.nome} attacca {difensore.nome}!\n')
        danno = max(1, attaccante.attack - difensore.defense)
        hp_difensore -= danno
        if hp_difensore > 0:
            print(f'HP {difensore.nome}: {hp_difensore}/{difensore.hp}')
        else:
            print(f'{difensore.nome} è esausto!')
        return hp_difensore

# (4)
class ErbaAlta:
    def __init__(self, link_api='https://pokeapi.co/api/v2/pokemon/'):
        ''' costruttore della classe '''
        self.link_api = link_api

    def incontra_pokemon(self):
        ''' funzione per estrarre un poco random e incontrarlo '''
        numero = random.randint(1, 1025)
        url = self.link_api + str(numero)
        res = rq.get(url)
        if res.status_code == 200:
            data = res.json()
            nome = data['forms'][0]['name'].upper()
            ab = random.choice(data['abilities'])['ability']['name']
            weight = data['weight']
            exp = data['base_experience']
            height = data['height']
            stats = data['stats']

            hp = next(stat['base_stat'] for stat in stats if stat['stat']['name'] == 'hp')
            attack = next(stat['base_stat'] for stat in stats if stat['stat']['name'] == 'attack')
            speed = next(stat['base_stat'] for stat in stats if stat['stat']['name'] == 'speed')
            defense = next(stat['base_stat'] for stat in stats if stat['stat']['name'] == 'defense')

            return Pokemon(data['id'], nome, ab, weight, exp, height, hp, attack, speed, defense)
        else:
            print('Errore nel recupero del pokemon.')
            return None

# (5)
class Gioco:
    def __init__(self):
        ''' costruttore della classe '''
        self.pokedex = Pokedex()
        self.erba_alta = ErbaAlta()
        self.carica_pokemon_iniziale()

    def carica_pokemon_iniziale(self):
        ''' assegna un utente un pokemon iniziale se non ne ha nessuno'''
        if not self.pokedex.load():
            pokemon = self.erba_alta.incontra_pokemon()
            self.pokedex.save({pokemon.id: pokemon.__dict__})
            print(f'Il tuo primo pokemon è: {pokemon.nome}')

    def mostra_pokedex(self):
        ''' mostra tutti i pokemon dell'utente '''
        print('\nTutti i tuoi pokemon:')
        for p in self.pokedex.load().values():
            print(p)

    def scegli_pokemon(self):
        ''' fa scegliere all'utente quale pokemon usare per la lotta'''
        print('Scegli il pokemon con cui lottare')
        self.mostra_pokedex()
        while True:
            nav = input('Dimmi l\'ID del pokemon da scegliere: ')
            pkm = self.pokedex.load().get(nav)
            if pkm is not None:
                return Pokemon(**pkm)
            else:
                print('ID non valido!')
                

    def lotta(self, pokemon_selvatico):
        ''' avvia la lotta pokemon '''
        self.pokemon_giocatore = self.scegli_pokemon()
        print(f'\nInizi la lotta tra {self.pokemon_giocatore.nome} e {pokemon_selvatico.nome}')
        time.sleep(1)
        battaglia = Battaglia(self.pokemon_giocatore, pokemon_selvatico)
        if battaglia.inizia_battaglia():
            return '1'
        else:
            return '2'

    def cattura_pokemon(self, pokemon_selvatico):
        ''' funzione per provare a cattuarare il pokemon avversario '''
        rand = random.randint(0, 5)
        if rand > 0:
            self.pokedex.save({pokemon_selvatico.id: pokemon_selvatico.__dict__})
            time.sleep(1)
            print(f'\tPreso! {pokemon_selvatico.nome} è stato catturato!')
            print(f'\tInfo:\n\tAbilità: {pokemon_selvatico.abilita}\n\tPeso: {pokemon_selvatico.peso/10} Kg\n\tXP: {pokemon_selvatico.xp}, Altezza: {pokemon_selvatico.altezza/10}m; HP: {pokemon_selvatico.hp}, Attack: {pokemon_selvatico.attack}, Defense: {pokemon_selvatico.defense}')
        else:
            print('Oh no il pokemon si è liberato ed è scappato!')

    def avvia_gioco(self):
        ''' menu principale del gioco '''
        self.pokemon_giocatore = list(self.pokedex.load().values())[0]
        while True:
            nav = input('1: Vai nell\'erba alta, 2: Visualizza i tuoi pokemon, 3: Esci ')
            if nav == '1':
                while True:
                    pokemon_selvatico = self.erba_alta.incontra_pokemon()
                    if not self.pokedex.is_in_pokedex(pokemon_selvatico.id):
                        print('Camminando nell\'erba alta...\n')
                        time.sleep(1)
                        print(f'Appare un {pokemon_selvatico.nome} selvatico.\n')
                        nav_sub = input('1: Lotta, 2: Scappa ')
                        if nav_sub == '1':
                            risultato_lotta = self.lotta(pokemon_selvatico)
                            if risultato_lotta == '1':
                                self.cattura_pokemon(pokemon_selvatico)
                        elif nav_sub == '2':
                            print('Scampato pericolo!')
                            break
                        else:
                            print('Scelta non valida.')
                    else:
                        print(f'\tQuesto {pokemon_selvatico.nome} è già presente nella tua pokedex!')
            elif nav == '2':
                self.mostra_pokedex()
            elif nav == '3':
                break
            else:
                print('Scelta non valida.')

gioco = Gioco()
gioco.avvia_gioco()