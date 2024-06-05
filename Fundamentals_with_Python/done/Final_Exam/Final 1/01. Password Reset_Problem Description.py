password = input()
while True:
    command = input().split(" ")
    if command[0] == "Done":
        break

    if command[0] == "TakeOdd":
        new = ""
        for index in range(1, len(password), 2):
            new += password[index]
        password = new
        print(password)

    elif command[0] == "Cut":
        index, length = int(command[1]), int(command[2])
        end_index = index + length - 1
        substring = password[index:end_index + 1]
        password = password.replace(substring, "", 1)
        print(password)

    else:  # Substitute
        substring, substitute = command[1], command[2]
        # while substring in password:
        if substring in password:
            password = password.replace(substring, substitute, - 1)
            print(password)
        else:
            print('Nothing to replace!')

print(f'Your password is: {password}')
