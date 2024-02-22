class Zoo:
    __animals = 1

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fish.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            pass
        elif species == "fish"
            pass
        elif species == "bird":
            pass


        return f"{self.species} in {self.zoo_name}: {self.name}\nTotal animals: {Zoo.__animals}"


name_ = input()
total = int(input())
for i in range(total):
    animal_info = input().split()
