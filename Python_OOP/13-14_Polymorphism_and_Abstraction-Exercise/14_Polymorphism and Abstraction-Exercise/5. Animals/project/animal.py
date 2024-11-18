from abc import ABC, abstractmethod


@abstractmethod
class Animal(ABC):
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender
        self.my_sound = ""

    @abstractmethod
    def make_sound(self) -> str:
        pass

    @property
    @abstractmethod
    def get_my_class_name(self) -> str:
        pass

    def __repr__(self):
        return f'This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.get_my_class_name}'
