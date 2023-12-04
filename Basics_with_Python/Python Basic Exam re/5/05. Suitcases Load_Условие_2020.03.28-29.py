available_capacity = float(input())
command = input()
is_full = False
loaded_counter = 0
c = 0

while command != "End":
    case_volume = float(command)
    c += 1
    if c % 3 == 0:
        case_volume *= 1.1
    available_capacity -= case_volume
    if available_capacity <= 0:
        is_full = True
        break

    loaded_counter += 1
    command = input()

if command == "End":
    print("Congratulations! All suitcases are loaded!")
elif is_full:
    print("No more space!")
print(f"Statistic: {loaded_counter} suitcases loaded.")
