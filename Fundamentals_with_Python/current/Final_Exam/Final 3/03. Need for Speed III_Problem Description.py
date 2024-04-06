def drive(cars_: dict, car_: str, distance_: int, fuel_: int):
    current_fuel, current_mileage = cars_[car_]["fuel"], cars_[car_]["mileage"]
    old_fuel, old_mileage = current_fuel, current_mileage
    if current_fuel < fuel_:
        print(f'Not enough fuel to make that ride')
    else:
        current_fuel -= fuel_
        current_mileage += distance_
        print(f'{car_} driven for {current_mileage - old_mileage} kilometers.'
              f' {old_fuel - current_fuel} liters of fuel consumed.')
    cars_[car_]["fuel"], cars_[car_]["mileage"] = current_fuel, current_mileage
    if cars_[car_]["mileage"] >= 100000:
        del cars_[car_]
        print(f'Time to sell the {car_}!')
    return cars_


def refuel(cars_: dict, car_: str, fuel_: int, max_fuel_: int):
    current_fuel = cars_[car_]["fuel"]
    old_fuel = current_fuel
    current_fuel += fuel_
    if current_fuel > max_fuel_:
        current_fuel = max_fuel_
    print(f'{car_} refueled with {current_fuel - old_fuel} liters')
    cars_[car_]["fuel"] = current_fuel
    return cars_


def revert(cars_: dict, car_: str, kilometers_: int):
    current_mileage = cars_[car_]["mileage"]
    old_mileage = current_mileage
    current_mileage -= kilometers_
    if current_mileage < 10000:
        current_mileage = 10000
    else:
        print(f'{car_} mileage decreased by {old_mileage - current_mileage} kilometers')
    cars_[car_]["mileage"] = current_mileage
    return cars_


max_fuel = 75
cars = {}
n = int(input())
for i in range(n):
    line = input().split("|")
    car, mileage, fuel = line[0], int(line[1]), int(line[2])
    cars[car] = {"mileage": mileage, "fuel": fuel}
# print(cars)

while True:
    line = input()
    if line == "Stop":
        break
    line = line.split(" : ")
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
# print(cars)

for car, car_data in cars.items():
    print(f'{car} -> Mileage: {car_data["mileage"]} kms, Fuel in the tank: {car_data["fuel"]} lt.')
