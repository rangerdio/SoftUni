raw_key = input()
activation_key = ''

while True:
    line = input().split(">>>")
    if line[0] == "Generate":
        break
    command = [0]

    if command == "Contains":
        substring = line[1]
        pass
    elif command == "Flip":
        letter_types = line[1]
        start_index = line[2]
        end_index = line[3]
        pass
    else:   # else command is Slice
        start_index = line[2]
        end_index = line[3]
        pass

print(f'Your activation key is: {activation_key}')
