from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, fuel: int):
        pass


class Car(Vehicle):
    AC_CONSUMPTION = 0.9

    def drive(self, distance: int):
        fuel_to_drive = distance * (self.fuel_consumption + self.AC_CONSUMPTION)
        if self.fuel_quantity >= fuel_to_drive:
            self.fuel_quantity -= fuel_to_drive

    def refuel(self, amount: int) -> None:
        self.fuel_quantity += amount


class Truck(Vehicle):
    AC_CONSUMPTION = 1.6
    FUEL_LOST = 0.95

    def drive(self, distance: int):
        fuel_to_drive = distance * (self.fuel_consumption + self.AC_CONSUMPTION)
        if self.fuel_quantity >= fuel_to_drive:
            self.fuel_quantity -= fuel_to_drive

    def refuel(self, amount: int) -> None:
        self.fuel_quantity += self.FUEL_LOST * amount


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
