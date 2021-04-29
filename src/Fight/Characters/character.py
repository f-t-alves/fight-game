import random

from src.Fight.Characters.character_classes import characterTypes
from src.Fight.ItemsAbilities.character_abilities import characterAbilities

class Character:

    def __init__(self, chosenClass):

        # Character Name
        self.name = ""

        # Character Class
        self.type = chosenClass
        for typeStats in characterTypes:
            if chosenClass in typeStats['NAME']:
                self.stats = typeStats
                break

        # Populate abilities
        self.abilities = []
        for ability in characterAbilities:
            if self.type in ability['CLASSES']:
                self.abilities.append(ability)

        # Level
        self.xp = 0
        self.level = 0

        # HP
        self.hpMax = 10 #temporary
        self.hp = self.hpMax

        # Status
        self.status = []

        # Backpack
        self.pack = {}

        # Wieldables
        self.armorSlots = {
            'head': None,
            'torso': None,
            'right_arm': None,
            'left_arm': None,
            'legs': None,
            'necklace': None,
            'rings': []
        }

    # Level up
    def levelUp(self):
        # Count how many levels it should level up
        levels = int(self.xp / 100)

        # Calculating xp overflow after full levels
        overflow = self.xp % 100
        
        # Applying level up and saving overflow
        self.level += levels
        self.xp = overflow
        
    def rename(self, newName):
        self.name = newName

    # Backpack items
    def storeItem(self, item):
        if item in self.pack.keys():
            self.pack[item] += 1
        else:
            self.pack[item] = 1

    def removeItem(self, item):
        self.pack[item] -= 1
        if self.pack[item] == 0:
            self.pack.pop(item)

    # Wieldable items
    def wieldItem(self, item, target):
        self.armorSlots[target] = item

    def unwieldItem(self, target):
        self.armorSlots[target] = None