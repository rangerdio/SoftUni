from collections import deque

hazelnuts = 0
field = []
size = int(input())
commands = deque(input().split(', '))
squirrel_row = None
squirrel_col = None

for row in range(size):
    line = list(input())
    if 's' in line:
        squirrel_row = row
        squirrel_col = line.index('s')
    field.append(line)

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}
done = False
while commands:
    command = commands.popleft()
    next_squirrel_row = squirrel_row + directions[command][0]
    next_squirrel_col = squirrel_col + directions[command][1]

    if not (0 <= next_squirrel_row < size and 0 <= next_squirrel_col < size):
        print('The squirrel is out of the field.')
        done = True
        break
    elif field[next_squirrel_row][next_squirrel_col] == '*':
        squirrel_row, squirrel_col = next_squirrel_row, next_squirrel_col
    elif field[next_squirrel_row][next_squirrel_col] == 't':
        print('Unfortunately, the squirrel stepped on a trap...')
        done = True
        break
    elif field[next_squirrel_row][next_squirrel_col] == 'h':
        hazelnuts += 1
        field[next_squirrel_row][next_squirrel_col] = '*'
        squirrel_row, squirrel_col = next_squirrel_row, next_squirrel_col
        if hazelnuts == 3:
            print('Good job! You have collected all hazelnuts!')
            done = True
            break
if not done:
    print('There are more hazelnuts to collect.')
print(f'Hazelnuts collected: {hazelnuts}')
