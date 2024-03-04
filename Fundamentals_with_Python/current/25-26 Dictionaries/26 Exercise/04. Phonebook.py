def search(name: str, phonebook: dict):
    pass


book = {}
while True:
    command = input().split("-")

    if command[0].isdigit():
        command = int(command)
        break

    book[command[0]] = command[1]

for i in range(command):
    search(input(), book)
