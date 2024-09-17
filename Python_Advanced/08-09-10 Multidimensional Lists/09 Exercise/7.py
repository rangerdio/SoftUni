from collections import deque
rows, cols = [int(x) for x in input().split()]
snake_data = input()
multiplier = rows * cols // len(snake_data) + 1
snake = snake_data * multiplier

snake = snake[:rows * cols]
snake = deque(list(snake))

matrix = [["*" for x in range(cols)] for row in range(rows)]

for row in range(rows):

    if row % 2 == 0:
        for col in range(cols):
            matrix[row][col] = snake.popleft()
    else:
        for col in range(cols - 1, -1, -1):
            matrix[row][col] = snake.popleft()

for row in range(rows):
    print(''.join(matrix[row]))
