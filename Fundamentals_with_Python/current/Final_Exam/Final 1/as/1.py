text = input()
while True:
    line = input()
    if line == "For Azeroth":
        break
    line = line.split()
    command = line[0]

    if command == "GladiatorStance":
        text = text.upper()
        print(text)

    elif command == "DefensiveStance":
        text = text.lower()
        print(text)

    elif command == "Dispel":
        index, letter = int(line[1]), line[2]
        if index < 0 or index >= len(text):
            print('Dispel too weak.')
        else:
            index_letter = text[index]
            text = text.replace(index_letter, letter, 1)
            print('Success!')
            # print(text)

    elif command == "Target" and line[1] == "Change":
        first_substring, second_substring = line[2], line[3]
        text = text.replace(first_substring, second_substring)
        print(text)

    elif command == "Target" and line[1] == "Remove":
        substring = line[2]
        if substring in text:
            text = text.replace(substring, "", 1)
            print(text)
    else:
        print("Command doesn't exist!")
