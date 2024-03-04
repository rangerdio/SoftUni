def search(name: str, phonebook: dict):
    if name in phonebook.keys():
        return f"{name} -> {phonebook[name]}"
    else:
        return f"Contact {name} does not exist."


book = {}
while True:
    command = input().split("-")

    if command[0].isdigit():
        command = int(command[0])
        break

    book[command[0]] = command[1]

for i in range(command):
    print(search(input(), book))
