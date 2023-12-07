gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break
    command_list = command.split()      # split the command to list so to access the elements (sub-commands)
    if command_list[0] == "OutOfStock":
        for gifts_index in range(len(gifts)):
            if command_list[1] == gifts[gifts_index]:
                gifts[gifts_index] = "None"  # if gift in command is in gifts, change their values to "None"
    elif command_list[0] == "Required":
        if int(command_list[2]) < len(gifts):  # if command [2] is < len(gifts)
            index = int(command_list[2])
            gifts[index] = command_list[1]
    elif command_list[0] == "JustInCase":
        gifts[-1] = command_list[1]
while "None" in gifts:
    gifts.remove("None")
gifts_new_string = " ".join(gifts)

print(gifts_new_string)
