from collections import deque
bees = deque([int(x) for x in input().split()])
nectar = deque([int(x) for x in input().split()])
symbols = deque([x for x in input().split()])

honey = 0

while bees and nectar:
    if nectar[-1] < bees[0]:
        nectar.pop()
        continue
    else:
        # collected

        if nectar[-1] == 0 and symbols[0] == '/':
            bees.popleft()
            nectar.pop()
            symbols.popleft()
            continue

        symbol_current = symbols.popleft()
        bee_current = bees.popleft()
        nectar_current = nectar.pop()

        dictionary = {
            '+': bee_current + nectar_current,
            '-': bee_current - nectar_current,
            '*': bee_current * nectar_current,
            '/': bee_current / nectar_current,
        }

        honey += abs(dictionary[symbol_current])

print(f'Total honey made: {honey}')

if bees:
    print(f'Bees left: {", ".join([str(x) for x in bees])}')
if nectar:
    print(f'Nectar left: {", ".join([str(x) for x in nectar])}')
