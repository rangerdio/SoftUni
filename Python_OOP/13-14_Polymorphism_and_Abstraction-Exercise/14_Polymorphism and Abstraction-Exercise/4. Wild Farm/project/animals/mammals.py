from project.animals.animal import Mammal
from project.food import Food, Meat, Vegetable, Fruit


class Mouse(Mammal):
    @staticmethod
    def make_sound() -> str:
        return "Squeak"

    @property
    def allowed_food(self) -> [Food]:
        return [Vegetable, Fruit]

    @property
    def bite_weight(self):
        return 0.10


class Dog(Mammal):
    @staticmethod
    def make_sound() -> str:
        return "Woof!"

    @property
    def bite_weight(self):
        return 0.40

    @property
    def allowed_food(self) -> [Food]:
        return [Meat]


class Cat(Mammal):
    @staticmethod
    def make_sound() -> str:
        return "Meow"

    @property
    def allowed_food(self) -> [Food]:
        return [Vegetable, Meat]

    @property
    def bite_weight(self):
        return 0.30


class Tiger(Mammal):
    @staticmethod
    def make_sound() -> str:
        return "Meow"

    @property
    def allowed_food(self) -> [Food]:
        return [Meat]

    @property
    def bite_weight(self):
        return 1
