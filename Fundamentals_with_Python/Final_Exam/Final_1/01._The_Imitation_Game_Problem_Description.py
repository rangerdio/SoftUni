message = input()

while True:
    command = input().split("|")
    if command[0] == "Decode":
        break

    if command[0] == "Move":
        number_letters = int(command[1])
        letters = message[:number_letters]
        message = message[number_letters:] + letters

    elif command[0] == "Insert":
        index, value = int(command[1]), command[2]
        message = message[:index] + value + message[index:]

    else:  # "ChangeAll":
        substring, replacement = command[1], command[2]
        message = message.replace(substring, replacement)

print(f'The decrypted message is: {message}')
