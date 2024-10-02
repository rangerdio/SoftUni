import os

while True:
    data = input()
    if data == "End":
        break
    command, filename, *args = data.split('-')
    if command == "Create":
        with open(filename, 'w') as my_file:
            my_file.write('')
    elif command == "Add":
        try:
            with open(filename, 'a') as my_file:
                my_file.write(f'{"".join(args)}\n')
        except FileNotFoundError:
            with open(filename, 'w') as my_file:
                my_file.write(f'{"".join(args)}\n')

    elif command == "Replace":
        try:
            with open(filename, 'r') as my_file:
                content = my_file.read()
                content = content.replace(args[0], args[1])
                my_file.close()
            with open(filename, 'w') as my_file:
                my_file.write(content)
        except FileNotFoundError:
            print('An error occurred')

    elif command == "Delete":
        try:
            os.remove(filename)
        except FileNotFoundError:
            print('An error occurred')
