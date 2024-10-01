size = int(input())
maze = []
player_position = []
HEALTH_MAX = 100
for row in range(size):
    line = list(input())
    if 'P' in line:
        player_position = [row, line.index('P')]
    maze.append(line)

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

health = HEALTH_MAX
danger_passed = False
while True:
    command = input()
    new_row, new_col = player_position[0] + directions[command], player_position[1] + directions[command]
    if not (0 <= new_row <= size and 0 <= new_col <= size):
        if maze[new_row][new_col] == 'M':
            pass
        elif maze[new_row][new_col] == 'H':
            pass
        elif maze[new_row][new_col] == 'X':
            pass
        elif maze[new_row][new_col] == '':
            pass
    else:
        continue

if health <= 0:
    print('Player is dead. Maze over!')
elif health >= 0 and danger_passed:
    print('Player escaped the maze. Danger passed!')
print(f"Player's health: {health} units")

for maze_line in maze:
    print(''.join(x for x in maze_line))
