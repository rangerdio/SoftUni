from abc import ABC, abstractmethod


class BaseWaiter(ABC):
    def __init__(self, name: str, hours_worked: int):
        if not (3 <= len(name) <= 50):
            raise ValueError("Waiter name must be between 3 and 50 characters in length!")
        if hours_worked < 0:
            raise ValueError("Cannot have negative hours worked!")

        self.name = name
        self.hours_worked = hours_worked

    @abstractmethod
    def calculate_earnings(self):
        pass

    @abstractmethod
    def report_shift(self):
        pass

    def __str__(self):
        return f"Name: {self.name}, Total earnings: ${self.calculate_earnings():.2f}"
