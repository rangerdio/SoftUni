from abc import ABC, abstractmethod


class BasePeak(ABC):
    def __init__(self, name: str, elevation: int):
        self.name = name
        self.elevation = elevation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if len(value) < 2:
            raise ValueError("Peak name cannot be less than 2 symbols!")
        self._name = value

    @property
    def elevation(self):
        return self._elevation

    @elevation.setter
    def elevation(self, value: int):
        if value < 1500:
            raise ValueError("Peak elevation cannot be below 1500m.")
        self._elevation = value

    @abstractmethod
    def calculate_difficulty_level(self):
        pass

    @abstractmethod
    def get_recommended_gear(self):
        pass
