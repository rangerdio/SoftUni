coffe = 0
while True:
    command = input()
    command_lower = command.lower()
    if command == "END":
        break
    if command_lower == "coding":
        if command == "coding":
            coffe += 1
        else:
            coffe += 2
    elif command_lower == "dog" or command_lower == "cat":
        if command == "dog" or command == "cat":
            coffe += 1
        else:
            coffe += 2
    elif command_lower == "movie":
        if command == "movie":
            coffe += 1
        else:
            coffe += 2

if coffe > 5:
    print("You need extra sleep")
else:
    print(coffe)
