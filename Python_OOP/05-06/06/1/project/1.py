from typing import List


class Vet:
    animals: List = []
    space: int = 5

    def __init__(self, name: str):
        self.name = name
        self.animals = []

    def register_animals(self):
        pass

    def unregister_animal(self):
        pass

    def info(self):
        # animals_in_clinic = 0
        # return f"{self.name} has {len(self.animals)} animals. {Vet.space - len(self.animals)} space left in clinic"
