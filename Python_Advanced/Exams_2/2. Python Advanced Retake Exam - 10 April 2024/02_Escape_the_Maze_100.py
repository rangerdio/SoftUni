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
    row, col = player_position
    command = input()
    new_row = row + directions[command][0]
    new_col = col + directions[command][1]

    if 0 <= new_row < size and 0 <= new_col < size:
        if maze[new_row][new_col] == 'M':
            health -= 40
            # print(health)
            if health <= 0:
                health = 0
                maze[row][col] = '-'
                maze[new_row][new_col] = 'P'
                break
            else:
                maze[row][col] = '-'
                maze[new_row][new_col] = 'P'

        elif maze[new_row][new_col] == 'H':
            health += 15
            if health > HEALTH_MAX:
                health = HEALTH_MAX
            maze[row][col] = '-'
            maze[new_row][new_col] = 'P'

        elif maze[new_row][new_col] == 'X':
            danger_passed = True
            maze[row][col] = '-'
            maze[new_row][new_col] = 'P'
            break

        elif maze[new_row][new_col] == '-':
            maze[row][col] = '-'
            maze[new_row][new_col] = 'P'

        player_position = new_row, new_col
    else:
        continue

if health <= 0:
    print('Player is dead. Maze over!')
elif health >= 0 and danger_passed:
    print('Player escaped the maze. Danger passed!')
print(f"Player's health: {health} units")

for maze_line in maze:
    print(''.join(x for x in maze_line))
