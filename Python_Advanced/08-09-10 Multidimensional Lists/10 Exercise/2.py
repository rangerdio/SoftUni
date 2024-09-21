rows = int(input())
cols = 0
matrix = []
for row in range(rows):
    inside = []
    for x in input().split():
        inside.append(int(x))
    cols = len(inside)
    matrix.append(inside)

while True:
    command_list = input().split()
    if command_list[0] == "END":
        break
    else:
        command, row, col, value = command_list[0], int(command_list[1]), int(command_list[2]), int(command_list[3])

    if not (0 <= row < rows and 0 <= col < cols):
        print("Invalid coordinates")
        continue
    matrix[row][col] += value if command == "Add" else - value

for row in matrix:
    print(*row)
