from abc import ABC, abstractmethod
from typing import Optional, Union

from project.food import Food


class Animal(ABC):
    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight
        self.food_eaten: int = 0

    @staticmethod
    @abstractmethod
    def make_sound() -> str:
        pass

    @property
    @abstractmethod
    def allowed_food(self) -> Food:
        pass

    @property
    @abstractmethod
    def bite_weight(self) -> float:
        pass

    def feed(self, food: Food) -> Optional[Union[str, None]]:
        if type(food) not in self.allowed_food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += 1
        self.weight += food.quantity * self.bite_weight


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float) -> None:
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str) -> None:
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}]"
