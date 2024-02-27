class Vehicle:

    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        if self.owner:
            return "Car already sold"
        elif money < self.price:
            return "Sorry, not enough money"
        else:
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {self.price - money}"


    def sell(self):
        pass

    def __repr__(self):
        pass


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
