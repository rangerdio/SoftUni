def search(pool: list, idx_1: int, idx_2: int, current_attempt: int):
    current_attempt += 1
    valid_list = []
    for _ in range(len(pool)):
        valid_list.append(_)

    if (idx_1 == idx_2) or (idx_1 not in valid_list and idx_2 not in pool):
        print("Invalid input! Adding additional elements to the board")
        item_to_insert = "-" + str(current_attempt) + "a"
        insert_index = len(pool) // 2
        pool.insert(insert_index, item_to_insert)
        pool.insert(insert_index, item_to_insert)

    else:
        if pool[idx_1] == pool[idx_2]:
            print(f"Congrats! You have found matching elements - {pool[idx_1]}!")
            item_to_remove = pool[idx_1]
            pool.remove(item_to_remove)
            pool.remove(item_to_remove)
        else:
            print("Try again!")
    return [pool, current_attempt]


sequence_list = input().split()
print(sequence_list)
attempts = 0

while True:
    command = input()
    if command == "end":
        print("Sorry you lose :(")
        print(f"{' '.join(sequence_list)}")
        break
    index_1 = int(command.split()[0])
    index_2 = int(command.split()[1])
    result = search(sequence_list, index_1, index_2, attempts)
    sequence_list = result[0]

    print(sequence_list)

    attempts = result[1]
    if not sequence_list:
        print(f"You have won in {attempts} turns!")
        break
