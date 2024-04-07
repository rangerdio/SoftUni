def plunder(database: dict):
    return database


def prosper(database: dict):
    return database


city_data = {}
while True:
    line = input().split("||")
    if line[0] == "Sail":
        break
    city, people, gold = line[0], line[1], line[2]

    if city not in city_data.keys():
        city_data[city] = {"population": int(people), "gold": int(gold)}
    else:
        city_data[city]["population"] += int(people)
        city_data[city]["gold"] += int(gold)


# print(city_data)

while True:
    line = input().split("=>")
    if line[0] == "End":
        break
    event = line[0]
    if event == "Plunder":
        city, people, gold = line[1], line[2], line[3]
        city_data = plunder(city_data)
    elif event == "Prosper":
        city, gold = line[1], line[2]
        city_data = prosper(city_data)
