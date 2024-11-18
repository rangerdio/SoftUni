from project.animals.animal import Bird, Animal
from project.food import Food, Vegetable, Meat, Fruit, Seed


class Owl(Bird):
    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @property
    def allowed_food(self) -> [Food]:
        return [Meat]

    @property
    def bite_weight(self):
        return 0.25


class Hen(Bird):
    @staticmethod
    def make_sound():
        return "Cluck"

    @property
    def allowed_food(self) -> [Food]:
        return [Vegetable, Fruit, Meat, Seed]

    @property
    def bite_weight(self):
        return 0.35

