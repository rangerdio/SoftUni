def drive(cars_: dict, car_: str, distance_: int, fuel_: int):
    return cars_


def refuel(cars_: dict, car_: str, fuel_: int, max_fuel_: int):
    current_fuel = cars_[car_]["fuel"]
    old_fuel = current_fuel
    current_fuel += fuel_
    if current_fuel > max_fuel_:
        current_fuel = max_fuel_
    print(f'{car} refueled with {current_fuel - old_fuel} liters')
    return cars_


def revert(cars_: dict, car_: str, kilometers_: int):
    current_mileage = cars_[car]["mileage"]
    old_mileage = current_mileage
    current_mileage -= kilometers_
    if current_mileage < 10000:
        current_mileage = 10000
    else:
        print(f'{car_} mileage decreased by {old_mileage - current_mileage} kilometers')
    cars_[car]["mileage"] = current_mileage
    return cars_


max_fuel = 75
cars = {}
n = int(input())
for i in range(n):
    line = input().split("|")
    car, mileage, fuel = line[0], int(line[1]), int(line[2])
    cars[car] = {"mileage": mileage, "fuel": fuel}
print(cars)

while True:
    line = input()
    if line == "Stop":
        break
    command, car = line[0], line[1]

    if command == "Drive":
        distance = int(line[2])
        fuel = int(line[3])
        cars = drive(cars, car, distance, fuel)
    elif command == "Refuel":
        fuel = int(line[2])
        cars = refuel(cars, car, fuel, max_fuel)
    elif command == "Revert":
        kilometers = int(line[2])
        cars = revert(cars, car, kilometers)
print(cars)

for car, car_data in cars.items():
    print(f'{car} -> Mileage: {car_data["mileage"]} kms, Fuel in the tank: {car_data["fuel"]}')
