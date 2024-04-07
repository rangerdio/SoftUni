key = input()

while True:
    line = input().split(">>>")
    if line[0] == "Generate":
        break
    command = line[0]
    if command == "Contains":
        substring = line[1]
        if substring in key:
            print(f'{key} contains {substring}')
        else:
            print('Substring not found!')

    elif command == "Flip":
        letter_types = line[1]
        start_index = int(line[2])
        end_index = int(line[3])

        if letter_types == "Upper":
            key = key[:start_index] + key[start_index: end_index].upper() + key[end_index:]
        else:
            key = key[:start_index] + key[start_index: end_index].lower() + key[end_index:]
        print(key)

    elif command == "Slice":
        start_index = int(line[1])
        end_index = int(line[2])
        key = key[:start_index] + key[end_index:]

        print(key)

print(f'Your activation key is: {key}')
