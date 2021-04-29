import random

from src.Fight.Monsters.monster_types import monsterTypes

class Monster:

    def __init__(self, level):
        self.level = level
        self.stats = random.choice(monsterTypes)
        
