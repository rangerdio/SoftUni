def plunder(cities_: dict, city_: str, people_to_kill_: int, gold_to_take_: int):
    return cities_


def prosper(cities_: dict, city_: str, gold_to_give_: int):
    return cities_


cities = {}
while True:
    line = input().split("||")
    if line[0] == "Sail":
        break
    city = line[0]
    people = int(line[1])
    gold = int(line[2])

    if city not in cities.keys():
        cities[city] = {"population": people, "gold": gold}
    else:
        cities[city]["population"] += people
        cities[city]["gold"] += gold


print(cities)

while True:
    line = input().split("=>")
    if line[0] == "End":
        break
    event = line[0]
    if event == "Plunder":
        city = line[1]
        people_to_kill = int(line[2])
        gold_to_take = int(line[3])
        cities = plunder(cities, city, people_to_kill, gold_to_take)
    elif event == "Prosper":
        city_target = line[1]
        gold_to_give = int(line[2])
        cities = prosper(cities, city_target, gold_to_give)
