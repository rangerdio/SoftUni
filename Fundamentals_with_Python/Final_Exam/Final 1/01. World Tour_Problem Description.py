message = input()

while True:
    command = input().split(":")
    if command[0] == "Travel":
        break

    if command[0] == "Add Stop":
        index, string = int(command[1]), command[2]
        if 0 <= index <= len(message) - 1:
            message = message[:index] + string + message[index:]
        print(message)

    elif command[0] == "Remove Stop":
        start_index, end_index = int(command[1]), int(command[2])
        if (0 <= start_index <= len(message) - 1) and (0 <= end_index <= len(message) - 1):
            message = message[:start_index] + message[end_index + 1:]
        print(message)

    else:  # Switch
        old_string, new_string = command[1], command[2]
        message = message.replace(old_string, new_string)
        print(message)
print(f'Ready for world tour! Planned stops: {message}')
