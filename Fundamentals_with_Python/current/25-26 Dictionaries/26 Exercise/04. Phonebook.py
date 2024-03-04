def search(name: str, phonebook: dict):
    return


book = {}
while True:
    command = input().split("-")

    if command[0].isdigit():
        command = int(command[0])
        break

    book[command[0]] = command[1]

for i in range(command):
    print(search(input(), book))
