# train = [0] * int(input())
wagons = int(input())
train = []
train.extend(0 for element in range(wagons))

while True:
    command = input()
    if command == "End":
        print(train)
        break
    command_list = command.split()
    if command_list[0] == "add":
        train[-1] += int(command_list[1])
    elif command_list[0] == "insert":
        train[int(command_list[1])] += int(command_list[2])
    elif command_list[0] == "leave":
        train[int(command_list[1])] -= int(command_list[2])
