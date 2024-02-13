def gather(journal: list, command_list: list):
    command = command_list[0]
    item = command_list[1]

    if command == "Collect":
        [journal.append(item) for element in journal if item not in journal]

    elif command == "Drop":
        [journal.remove(item) for element in journal if item in journal]  # all existence or just one?

    elif command == "Renew":
        if item in journal:
            item_index = journal.index(item)
            journal.append(journal.pop(item_index))

    elif command == "Combine Items":
        old_item, new_item = item.split(":")[0], item.split(":")[1]
        new_item_index = journal.index(old_item) + 1 if old_item in journal else 0
        journal.insert(new_item_index, new_item) if new_item_index else 0

    return journal


journal_list = input().split(", ")
result_journal = []

while True:
    cmd = input()
    if cmd == "Craft!":
        break
    command_input = cmd.split(" - ")
    result_journal = gather(journal_list, command_input)
    journal_list = result_journal

print(", ".join(result_journal))
