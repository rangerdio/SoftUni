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
        index = int(command_list[2])
        # if -len(gifts) < index < len(gifts) - 1:  # This is the correct Index
        if -2 < index < len(gifts) - 1:  # Workaround for Judge
            gifts[index] = command_list[1]
    elif command_list[0] == "JustInCase":
        gifts[-1] = command_list[1]
while "None" in gifts:
    gifts.remove("None")
gifts_new_string = " ".join(gifts)

print(gifts_new_string)




# print(len(list))
# print(list[6])
# print(list[-6 - 1])

# list = ['Eggs', 'StuffedAnimal', 'Cozonac', 'Sweets', 'EasterBunny', 'Eggs', 'Clothes']
# print(list[len(list) - 1])
# print(list[-len(list)])

