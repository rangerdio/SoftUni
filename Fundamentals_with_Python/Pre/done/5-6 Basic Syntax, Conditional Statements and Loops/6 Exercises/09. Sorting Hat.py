while True:
    name = input()
    if name == "Welcome!":
        break
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    name_length = len(name)

    if name_length < 5:
        print(f"{name} goes to Gryffindor.")
    elif 5 == name_length:
        print(f"{name} goes to Slytherin.")
    elif 6 == name_length:
        print(f"{name} goes to Ravenclaw.")
    elif 6 < name_length:
        print(f"{name} goes to Hufflepuff.")

if not name == "Voldemort":
    print("Welcome to Hogwarts.")
