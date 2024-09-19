from collections import deque
n, m = [int(x) for x in input().split()]

matrix = []
player_start_positions = []
bunny_start_positions = []
for row in range(n):
    current_row = list(input())
    if "P" in current_row:
        # player_start_positions.append([row, current_row.index("P")])
        player_start_positions = [row, current_row.index("P")]
    for element in current_row:
        if element == "B":
            bunny_start_positions.append([row, current_row.index(element)])
    matrix.append(current_row)

commands = deque(list(input()))
print(matrix)
print(player_start_positions)
print(bunny_start_positions)
print(commands)
