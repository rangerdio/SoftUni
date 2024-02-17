def search(pool: list, idx_1: int, idx_2: int, current_attempt: int):
    current_attempt += 1

    if idx_1 == idx_2 or idx_1 < 0 or idx_2 < 0 or idx_1 >= len(pool) or idx_2 >= len(pool):
        print("Invalid input! Adding additional elements to the board")
        item_to_insert = "-" + str(current_attempt) + "a"
        insert_index = len(pool) // 2
        pool.insert(insert_index, item_to_insert)
        pool.insert(insert_index + 1, item_to_insert)

    else:
        if pool[idx_1] == pool[idx_2]:
            print(f"Congrats! You have found matching elements - {pool[idx_1]}!")
            item_to_remove = pool[idx_1]
            pool.remove(item_to_remove)
            pool.remove(item_to_remove)
        else:
            print("Try again!")
    return pool, current_attempt


sequence_list = input().split()
attempts = 0

while True:
    command = input()
    if command == "end":
        print("Sorry you lose :(")
        print(" ".join(sequence_list))
        break
    index_1, index_2 = map(int, command.split())
    result = search(sequence_list, index_1, index_2, attempts)
    sequence_list, attempts = result

    if not sequence_list:
        print(f"You have won in {attempts} turns!")
        break
