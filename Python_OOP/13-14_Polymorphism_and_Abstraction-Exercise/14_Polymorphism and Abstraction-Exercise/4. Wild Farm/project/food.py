from abc import ABC, abstractmethod


class Food(ABC):
    def __init__(self, quantity: int) -> None:
        self.quantity = quantity


class Vegetable(Food):
    def feed(self) -> None:
        pass


class Fruit(Food):
    pass


class Meat(Food):
    pass


class Seed(Food):
    pass

