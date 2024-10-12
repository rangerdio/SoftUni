size = int(input())
board = []
gambler_position = []
money = 100
jackpot = False
game_over = False

for row in range(size):
    line = list(input())
    if 'G' in line:
        gambler_position = [row, line.index('G')]
    board.append(line)

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

while True:
    command = input()
    if command == 'end':
        break
    row, col = gambler_position
    new_row = row + directions[command][0]
    new_col = col + directions[command][1]

    if not 0 <= new_row < size and not 0 <= new_col < size:
        game_over = True
        break
    else:
        if board[new_row][new_col] == '-':
            gambler_position = [new_row, new_col]
            board[row][col] = '-'
            board[new_row][new_col] = 'G'

        elif board[new_row][new_col] == 'W':
            money += 100
            gambler_position = [new_row, new_col]
            board[row][col] = '-'
            board[new_row][new_col] = 'G'

        elif board[new_row][new_col] == 'P':
            money -= 200
            gambler_position = [new_row, new_col]
            board[row][col] = '-'
            board[new_row][new_col] = 'G'
            if money <= 0:
                game_over = True
                break

        elif board[new_row][new_col] == 'J':
            money += 100000
            gambler_position = [new_row, new_col]
            board[row][col] = '-'
            board[new_row][new_col] = 'G'
            jackpot = True
            break

if jackpot:
    print(f'You win the Jackpot!')
if game_over:
    print('Game over! You lost everything!')
else:
    print(f'End of the game. Total amount: {money}$')
    for row in board:
        print(''.join(row))
