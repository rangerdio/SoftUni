from abc import ABC, abstractmethod
from project.peaks.base_peak import BasePeak


class BaseClimber(ABC):
    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks = []
        self.is_prepared = True

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Climber name cannot be null or empty!")
        self._name = value

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value: float):
        if value <= 0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        self._strength = value

    @abstractmethod
    def can_climb(self):
        pass

    @abstractmethod
    def climb(self, peak: BasePeak):
        pass

    def rest(self):
        self.strength += 15

    def __str__(self):
        conquered = ", ".join(sorted(self.conquered_peaks))
        return f"{self.__class__.__name__}: /// Climber name: {self.name} * Left strength: {self.strength:.1f} * Conquered peaks: {conquered} ///"

