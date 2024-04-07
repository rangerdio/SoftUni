def plunder(cities_: dict, town_: str, people_to_kill_: int, gold_to_take_: int):
    # print(cities_)
    mark = False
    current_town_population = cities_[town_]["population"]
    current_town_gold = cities_[town_]["gold"]
    old_current_town_population = current_town_population
    old_current_town_gold = current_town_gold
    current_town_population -= people_to_kill_
    current_town_gold -= gold_to_take_
    cities_[town_]["population"] = current_town_population
    cities_[town_]["gold"] = current_town_gold
    if current_town_gold <= 0 or current_town_population <= 0:
        mark = True
        # if down must stay in the list, with respective 0es, must modify this respectively
        # so, should put the respecive values to 0, not to delete the city
        if current_town_gold <= 0 and current_town_population <= 0:     # both are gone
            print(f'{town_} plundered! {old_current_town_gold} gold stolen, {old_current_town_population} citizens killed.')
        elif current_town_gold <= 0 < current_town_population:  # only gold is gone
            print(f'{town_} plundered! {old_current_town_gold} gold stolen, {people_to_kill_} citizens killed.')
        else:   # only population is gone
            print(f'{town_} plundered! {gold_to_take_} gold stolen, {old_current_town_population} citizens killed.')
    else:   # town is alive
        print(f'{town_} plundered! {gold_to_take_} gold stolen, {people_to_kill_} citizens killed.')
    if mark:
        print(f"{town_} has been wiped off the map!")
        del cities_[town_]
    # print(cities_)
    return cities_


def prosper(cities_: dict, town_: str, gold_to_give_: int):
    # print(' are we here at all?')
    if gold_to_give_ < 0:
        print('Gold added cannot be a negative number!')
        return cities_
    if town_ in cities_.keys():
        cities_[town_]["gold"] += gold_to_give_
        print(f'{gold_to_give_} gold added to the city treasury. {town_} now has {cities_[town_]["gold"]} gold.')
    return cities_


cities = {}
while True:
    line = input().split("||")
    if line[0] == "Sail":
        break
    town = line[0]
    people = int(line[1])
    gold = int(line[2])

    if town not in cities.keys():
        cities[town] = {"population": people, "gold": gold}
    else:
        cities[town]["population"] += people
        cities[town]["gold"] += gold


# print(cities)

while True:
    line = input().split("=>")
    if line[0] == "End":
        break
    event = line[0]
    if event == "Plunder":
        town = line[1]
        people_to_kill = int(line[2])
        gold_to_take = int(line[3])
        cities = plunder(cities, town, people_to_kill, gold_to_take)
    elif event == "Prosper":
        town_target = line[1]
        gold_to_give = int(line[2])
        cities = prosper(cities, town_target, gold_to_give)

# print(cities)
if cities.keys():
    print(f'Ahoy, Captain! There are {len(cities.keys())} wealthy settlements to go to:')
    for city, items in cities.items():
        print(f'{city} -> Population: {items["population"]} citizens, Gold: {items["gold"]} kg')
