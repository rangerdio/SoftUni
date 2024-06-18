def rate(plants_: dict, cmd_plant_: str, cmd_rating_: int):
    plants_[cmd_plant_]['rating'] += cmd_rating_
    plants_[cmd_plant_]['rating_counter'] += 1
    return plants_


def update(plants_: dict, cmd_plant_: str, cmd_new_rarity_: int):
    plants_[cmd_plant_]["rarity"] = cmd_new_rarity_
    return plants_


def reset(plants_: dict, cmd_plant_: str):
    plants_[cmd_plant_]["rating"] = 0
    return plants_


n = int(input())
plants = {}
for i in range(n):
    line = input().split("<->")
    plant, rarity = line[0], line[1]
    plants[plant] = {"rarity": int(rarity), "rating": 0, "rating_counter": 0}

while True:
    line = input().split(": ")
    if line[0] == "Exhibition":
        break
    command = line[0]

    if command == "Rate":
        cmd_plant, cmd_rating = line[1].split(" - ")
        plants = rate(plants, cmd_plant, int(cmd_rating))

    elif command == "Update":
        cmd_plant, cmd_new_rarity = line[1].split(" - ")
        plants = update(plants, cmd_plant, int(cmd_new_rarity))

    else:   # Reset
        cmd_plant = line[1]
        plants = reset(plants, cmd_plant)

print(f'Plants for the exhibition:')
for plant, data in plants.items():
    rating_avg = data["rating"] / data["rating_counter"] if data["rating_counter"] > 0 else 0
    print(f'- {plant}; Rarity: {data["rarity"]}; Rating: {rating_avg:.2f}')

