import random

from src.Player.player_classes import playerClasses
from src.ItemsAbilities.player_abilities import playerAbilities

class Player:

    def __init__(self, chosenClass):
        self.type = chosenClass
        for type in playerClasses:
            if chosenClass in type['NAME']:
                self.stats = type
                break
        self.level = 1

        # Populate abilities
        self.abilities = []
        for ability in playerAbilities:
            if self.type in ability['CLASSES']:
                self.abilities.append(ability)

    def levelUp(self):
        self.level += 1
        