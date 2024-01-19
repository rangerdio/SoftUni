wagons = [0] * int(input())
print(wagons)

while True:
    command = input()
    if command == "End":
        break
    command_list = [command.split()]
    print(command_list)
