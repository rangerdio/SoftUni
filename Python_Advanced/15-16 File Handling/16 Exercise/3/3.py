while True:
    data = input()
    if data == "End":
        break
    # print(data)
    command, filename, *args = data.split('-')
    # print(command, filename, *args)
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
        pass
    elif command == "Delete":
        pass
