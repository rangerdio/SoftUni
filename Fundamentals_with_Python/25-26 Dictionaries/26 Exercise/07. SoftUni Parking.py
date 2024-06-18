def register(parking_: dict, username: str, plate: str):
    if username not in parking_.keys():
        parking_[username] = plate
        print(f"{username} registered {plate} successfully")
    else:   # user parked car in parking already
        print(f"ERROR: already registered with plate number {plate}")
    return parking_


def unregister(parking_: dict, username: str):
    if username not in parking_.keys():
        print(f"ERROR: user {username} not found")
    else:   # user have car in parking, remove it
        parking_.pop(username)
        print(f"{username} unregistered successfully")
    return parking_


n = int(input())
parking = {}
for _ in range(n):
    command_list = input().split()
    if command_list[0] == "register":
        parking = register(parking, command_list[1], command_list[2])
    elif command_list[0] == "unregister":
        unregister(parking, command_list[1])

for element in parking.keys():
    print(f"{element} => {parking[element]}")