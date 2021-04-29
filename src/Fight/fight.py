import random

from src.Fight.Party.party import Party
from src.Fight.Characters.character import Character

class Fight:
    def __init__(self):
        self.party = Party('test party')

    def addRandomCharacter(self):
        classList = ['Mage', 'Paladin', 'Archer', 'Tank']
        character = Character(random.choice(classList))
        
        self.party.addCharacter(character)