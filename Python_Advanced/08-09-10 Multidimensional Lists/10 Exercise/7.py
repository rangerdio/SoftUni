from collections import deque
presents = int(input())
n = int(input())
santa_position = []
nice_present_given = 0
neighborhood = []
nice_kids = 0

for row in range(n):
    current_row = input().split()
    if "S" in current_row:
        santa_position = [row, current_row.index("S")]
    nice_kids += current_row.count("V")
    neighborhood.append(current_row)

# print(neighborhood)
# print(santa_coordinates)
# print(nice_kids)

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

for _ in range(n):
    command = input()
    if command == "Christmas morning":
        break
    new_row = santa_position[0] + directions[command][0]
    new_col = santa_position[1] + directions[command][1]

    if 0 <= new_row < n and 0 <= new_col < n:
        neighborhood[santa_position[0]][santa_position[1]] = '-'
        santa_position = [new_row, new_col]

        if neighborhood[new_row][new_col] == "V":   # nice kid receive present
            nice_present_given += 1
            presents -= 1
            neighborhood[new_row][new_col] = "-"
            if presents == 0:
                break

        elif neighborhood[new_row][new_col] == "X":
            neighborhood[new_row][new_col] = "-"
            continue

        elif neighborhood[new_row][new_col] == "C":
            cookie_row = new_row
            cookie_col = new_col
            for key, value in directions.items():
                if neighborhood[cookie_row + value[0]][cookie_col + value[1]] == 'V':  # neighbor of cookie location
                    presents -= 1
                    neighborhood[cookie_row + value[0]][cookie_col + value[1]] = '-'
                    nice_present_given += 1
                    if presents == 0:
                        break
                elif neighborhood[cookie_row + value[0]][cookie_col + value[1]] == 'X':
                    presents -= 1
                    neighborhood[cookie_row + value[0]][cookie_col + value[1]] = '-'
                    if presents == 0:
                        break
            if presents == 0:
                break

santa_position = [new_row, new_col]
neighborhood[new_row][new_col] = 'S'

if presents == 0:
    print('Santa ran out of presents!')
for row in range(n):
    print(' '.join(neighborhood[row]))

if nice_present_given >= nice_kids:
    print(f'Good job, Santa! {nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids - nice_present_given} nice kid/s.')
