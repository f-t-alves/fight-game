import random

from src.Monsters.monster_types import monsterTypes

class Monster:

    def __init__(self, level):
        self.level = level
        self.stats = random.choice(monsterTypes)
        
