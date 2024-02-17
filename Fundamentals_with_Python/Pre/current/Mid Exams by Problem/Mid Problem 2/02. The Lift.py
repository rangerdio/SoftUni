def lift_cabin(queue: int, lift: list):
    number_of_cabins = len(lift)
    total_space = 4 * number_of_cabins
    is_full = False
    is_no_man = False
    mark = 0
    for man in range(1, queue + 1):
        if sum(lift) == total_space:
            is_full = True
            mark = man
            break

        for i in range(len(lift)):
            if lift[i] == 4:
                continue
            else:
                lift[i] += 1
                break

        if man == queue:
            is_no_man = True

    if is_full and not is_no_man:
        lift_str = [str(element) for element in lift]
        print(f"There isn't enough space! {queue - mark + 1} people in a queue!")
        print(f'{" ".join(lift_str)}')
    elif is_no_man and not is_full:
        lift_str = [str(element) for element in lift]
        print("The lift has empty spots!")
        print(f'{" ".join(lift_str)}')
    else:
        lift_str = [str(element) for element in lift]
        print(" ".join(lift_str))
    return


waiting_queue = int(input())
lift_current_state = list(map(int, input().split()))

lift_cabin(waiting_queue, lift_current_state)

