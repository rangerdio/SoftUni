def register(parking_: dict, username: str, plate: str):
    return


def unregister(parking_: dict, username: str):
    return


n = int(input())
parking = {}
for _ in range(n):
    command_list = input().split()
    if command_list[0] == "register":
        register(parking, command_list[1], command_list[2])
    elif command_list[0] == "unregister":
        unregister(parking, command_list[1])

print(parking)
