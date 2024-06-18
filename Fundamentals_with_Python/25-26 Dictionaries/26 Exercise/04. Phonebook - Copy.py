phonebook = {}
criteria = []
n = 0
while True:
    contact = input().split("-")
    if contact[0].isnumeric():
        n = int(contact[0])
        break
    phonebook[contact[0]] = contact[1]


for i in range(n):
    criteria.append(input())

for name in criteria:
    if name in phonebook.keys():
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')
