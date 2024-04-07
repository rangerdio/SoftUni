raw_key = input()
activation_key = raw_key

while True:
    line = input().split(">>>")
    if line[0] == "Generate":
        break
    command = line[0]

    if command == "Contains":
        substring = line[1]
        if substring in activation_key:
            print(f'{activation_key} contains {substring}".')
        else:
            print('Substring not found!')

    elif command == "Flip":
        command_letters = ""
        letter_types = line[1]
        start_index = int(line[2])
        end_index = int(line[3])

        if letter_types == "Upper":
            activation_key = activation_key[:start_index] + \
                             activation_key[start_index + 1: end_index - 1].upper() + activation_key[end_index:]
        else:
            activation_key = activation_key[:start_index] + \
                             activation_key[start_index + 1: end_index - 1].lower() + activation_key[end_index:]
        print(activation_key)
    else:   # else command is Slice
        print("asd")
        start_index = int(line[1])
        end_index = int(line[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

print(f'Your activation key is: {activation_key}')
