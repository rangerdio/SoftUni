message = input()

while True:
    command = input().split(":|:")
    if command[0] == "Reveal":
        break

    if command[0] == "InsertSpace":
        index = int(command[1])
        # letter = message[index]
        # message = message.replace(letter, " " + letter, 1)
        message = message[:index] + " " + message[index:]
        print(message)

    elif command[0] == "Reverse":
        substring = command[1]

        if substring not in message:
            print('error')
        else:
            message = message.replace(substring, "", 1)
            message += substring[::-1]
            print(message)

    else:  # ChangeAll
        substring, replacement = command[1], command[2]
        message = message.replace(substring, replacement, -1)
        print(message)

print(f'You have a new text message: {message}')
