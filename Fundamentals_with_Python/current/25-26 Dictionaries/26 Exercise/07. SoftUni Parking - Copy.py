def register(database: dict, username: str, license_plate: str):
    if username in database.keys():
        if license_plate != database[username]:
            print(f'ERROR: already registered with plate number {license_plate}')
        else:
            print(f'{username} registered {license_plate} successfully')
    else:
        database[username] = [license_plate]
        print(f'{username} registered {license_plate} successfully')

    return database


def unregister():
    return


n = int(input())
parking = {}

for i in range(n):
    command = input().split()
    if command[0] == "register":
        registration = register(parking, command[1], command[2])
        parking = registration
    else:
        if command[1] not in parking.keys():
            print(f'ERROR: user {command[1]} not found')
        else:
            del parking[command[1]]
            print(f'{command[1]} unregistered successfully')

for user in parking.keys():
    print(f'{user} => {parking[user][0]}')
