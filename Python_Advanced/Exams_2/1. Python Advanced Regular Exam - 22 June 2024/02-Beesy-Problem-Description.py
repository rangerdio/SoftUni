size = int(input())
matrix = []
bee_position = []
hive_position = []
energy = 15
total_nectar = 0
is_hive = False
is_energy_restored = False

for row in range(size):
    line = list(input())
    if 'B' in line:
        bee_position.append(row)
        bee_position.append(line.index('B'))
    if 'H' in line:
        if 'H' in line:
            hive_position.append(row)
            hive_position.append(line.index('H'))
    matrix.append(line)

# size = 5
# matrix = [['-', '-', 'B', '-', '-'],
#           ['H', '-', '9', '8', '7'],
#           ['-', '4', '8', '1', '2'],
#           ['5', '-', '-', '-', '-'],
#           ['2', '-', '-', '-', '-']]
# bee_position = [0, 2]
# hive_position = [1, 0]


directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

while energy >= 0:
    energy -= 1
    command = input()
    bee_row, bee_col = bee_position
    new_row = (bee_row + directions[command][0]) % size
    new_col = (bee_col + directions[command][1]) % size

    if matrix[new_row][new_col] == 'H':
        is_hive = True
        matrix[bee_row][bee_col] = "-"
        bee_position = [new_row, new_col]
        matrix[new_row][new_col] = 'B'
        break
    elif matrix[new_row][new_col] == '-':
        matrix[bee_row][bee_col] = "-"
        bee_position = [new_row, new_col]
        matrix[new_row][new_col] = 'B'

    else:
        total_nectar += int(matrix[new_row][new_col])
        matrix[bee_row][bee_col] = "-"
        bee_position = [new_row, new_col]
        matrix[new_row][new_col] = 'B'

    if energy == 0 and total_nectar < 30:
        break
        pass
    elif energy == 0 and total_nectar >= 30 and not is_energy_restored:
        energy += abs(total_nectar - 30)
        total_nectar = 30
        is_energy_restored = True
    elif energy == 0 and total_nectar >= 30 and is_energy_restored:
        break

if is_hive and total_nectar >= 30:
    print(f'Great job, Beesy! The hive is full. Energy left: {energy}')
elif is_hive and total_nectar < 30:
    print('Beesy did not manage to collect enough nectar.')

if not is_hive:
    print('This is the end! Beesy ran out of energy.')

for row in matrix:
    print(''.join(x for x in row))
