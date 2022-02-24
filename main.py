import random

AUSWAHL = ['Schere', 'Stein', 'Papier']

class SchereSteinPapierSimulator:
    def __init__(self):
        mensch_auswahl = None
        computer_auswahl = None
    def get_mensch_auswahl(self):
        auswahl_nr = int(input('Bitte Auswahl als Zahl eingeben'))
        self.mensch_auswahl = AUSWAHL[auswahl_nr-1]

    def get_computer_auswahl(self):
        self.computer_auswahl = random.choice(AUSWAHL)

    def ausgabe_optionen(self):
        
        print('\n'.join(f'({i}) {optionen.title()}' for i,
        optionen in enumerate(AUSWAHL)))

    def ausgabe_wahl(self):
        print(f'Du hast {self.mensch_auswahl} gewählt')
        print(f'Der Computer hat {self.computer_auswahl} gewählt')
    
    def ausgabe_gewonnen_verloren(self, mensch_gewinnt, mensch_verliert):
        if self.computer_auswahl == mensch_verliert:
            print(f'{self.computer_auswahl} schlägt {self.mensch_auswahl}')
        elif self.computer_auswahl == mensch_gewinnt:
            print(f'{self.mensch_auswahl} schlägt {self.computer_auswahl}')
    
    def ausgabe_ergebnis(self):
        if self.mensch_auswahl == self.computer_auswahl:
            print('Unentschieden!')
        
        if self.mensch_auswahl == 'Stein':
            self.ausgabe_gewonnen_verloren('Schere','Papier')
        elif self.mensch_auswahl == 'Papier':
            self.ausgabe_gewonnen_verloren('Stein','Schere')
        elif self.mensch_auswahl == 'Schere':
             self.ausgabe_gewonnen_verloren('Papier','Stein')

    def simulation(self):
        self.ausgabe_optionen()
        self.get_mensch_auswahl()
        self.get_computer_auswahl()
        self.ausgabe_wahl()
        self.ausgabe_ergebnis()


STP = SchereSteinPapierSimulator()
STP.simulation()