from src.Fight.Characters.character import Character

class Party:

    def __init__(self, name):
        self.members = []
        self.name = name

    def addCharacter(self, character):
        self.members.append(character)

    def removeCharacter(self, index):
        return self.members.pop(index)
