def urgent(groceries: list, item: str):
    if item not in groceries:
        groceries.insert(0, item)
    return groceries


def unnecessary(groceries: list, item: str):
    if item in groceries:
        groceries.remove(item)
    return groceries


def correct(groceries: list, old_item: str, new_item: str):
    if old_item in groceries:
        old_item_index = groceries.index(old_item)
        groceries[old_item_index] = new_item
    return groceries


def rearrange(groceries: list, item: str):
    if item in groceries:
        item_index = groceries.index(item)
        groceries.append(groceries.pop(item_index))
    return groceries


groceries_list = input().split("!")
while True:
    command = input()
    if command == "Go Shopping!":
        break
    else:
        command_list = command.split()

        if command_list[0] == "Urgent":
            groceries_list_result = urgent(groceries_list, command_list[1])
            groceries_list = groceries_list_result

        elif command_list[0] == "Unnecessary":
            groceries_list_result = unnecessary(groceries_list, command_list[1])
            groceries_list = groceries_list_result

        elif command_list[0] == "Correct":
            groceries_list_result = correct(groceries_list, command_list[1], command_list[2])
            groceries_list = groceries_list_result

        elif command_list[0] == "Rearrange":
            groceries_list_result = rearrange(groceries_list, command_list[1])
            groceries_list = groceries_list_result

print(", ".join(groceries_list))
