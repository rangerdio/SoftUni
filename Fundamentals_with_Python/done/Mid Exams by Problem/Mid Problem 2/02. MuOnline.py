def clear_room(hp: int, bitcoins: int, command: str, value: int):
    # print(command, value)

    if command == "potion":

        if hp < 100:
            if hp + value <= 100:
                hp += value
                print(f"You healed for {value} hp.")
            else:  # hp + value > 100
                print(f"You healed for {abs(hp - 100)} hp.")
                hp = 100
            print(f"Current health: {hp} hp.")

    elif command == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")

    else:
        monster = command

        hp -= value
        if hp > value:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
    return [hp, bitcoins]


start_bitcoins = 0
start_health = 100
rooms = input().split("|")
room_counter = 0
for room in rooms:
    room_counter += 1
    current_data = clear_room(start_health, start_bitcoins, room.split()[0], int(room.split()[1]))
    current_hp = current_data[0]
    current_bitcoin = current_data[1]
    start_bitcoins, start_health = current_bitcoin, current_hp

    if start_health <= 0:
        print(f"Best room: {room_counter}")
        break

if start_health > 0:
    print("You've made it!")
    print(f"Bitcoins: {start_bitcoins}")
    print(f"Health: {start_health}")
