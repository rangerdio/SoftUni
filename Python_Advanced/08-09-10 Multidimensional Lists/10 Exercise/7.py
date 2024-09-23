presents = int(input())
n = int(input())
neighborhood = []
santa_position = []
nice_present_given = 0
nice_kids = 0

for row in range(n):
    current_row = input().split()
    if "S" in current_row:
        santa_position = [row, current_row.index("S")]
    nice_kids += current_row.count("V")
    neighborhood.append(current_row)

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}


while presents > 0:
    command = input()
    if command == "Christmas morning":
        break
    new_row = santa_position[0] + directions[command][0]
    new_col = santa_position[1] + directions[command][1]

    if 0 <= new_row < n and 0 <= new_col < n:

        if neighborhood[new_row][new_col] == "V":   # nice kid receive present
            nice_present_given += 1
            presents -= 1
            neighborhood[new_row][new_col] = "-"

        elif neighborhood[new_row][new_col] == "C":

            for value in directions.values():
                n_row, n_col = new_row + value[0], new_col + value[1]
                if neighborhood[n_row][n_col] in "V":
                    presents -= 1
                    neighborhood[n_row][n_col] = "-"
                    nice_present_given += 1
                    if presents == 0:
                        break
                elif neighborhood[n_row][n_col] == 'X':
                    presents -= 1
                    neighborhood[n_row][n_col] = '-'
                    if presents == 0:
                        break

        elif neighborhood[new_row][new_col] == "X":
            neighborhood[new_row][new_col] = "-"

        neighborhood[santa_position[0]][santa_position[1]] = '-'
        santa_position = [new_row, new_col]
        neighborhood[new_row][new_col] = 'S'

if presents < 1 and nice_kids - nice_present_given > 0:
    print('Santa ran out of presents!')
for row in range(n):
    print(' '.join(neighborhood[row]))

if nice_present_given >= nice_kids:
    print(f'Good job, Santa! {nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids - nice_present_given} nice kid/s.')
