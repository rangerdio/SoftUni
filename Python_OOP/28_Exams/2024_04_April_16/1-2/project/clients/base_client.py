from abc import ABC, abstractmethod

class BaseClient(ABC):
    def __init__(self, name: str, membership_type: str):
        self.name = name
        self.membership_type = membership_type
        self.points = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Client name should be determined!")
        self._name = value

    @property
    def membership_type(self):
        return self._membership_type

    @membership_type.setter
    def membership_type(self, value: str):
        if value not in ["Regular", "VIP"]:
            raise ValueError("Invalid membership type. Allowed types: Regular, VIP.")
        self._membership_type = value

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value: int):
        if value < 0:
            raise ValueError("Points cannot be negative!")
        self._points = value

    @abstractmethod
    def earning_points(self, order_amount: float):
        pass

    def apply_discount(self):
        if self.points >= 100:
            self.points -= 100
            return 10, self.points
        elif self.points >= 50:
            self.points -= 50
            return 5, self.points
        return 0, self.points