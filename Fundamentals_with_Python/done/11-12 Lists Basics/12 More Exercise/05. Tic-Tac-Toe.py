line_1 = input().split()
line_2 = input().split()
line_3 = input().split()

winner_found = False
winner = "Draw!"

if (line_1[0] == line_2[1] == line_3[2] or line_1[2] == line_2[1] == line_3[0]) and line_1[0] != "0":  # Diagonal
    winner_found = True
    winner = line_2[1]

if (line_1[0] == line_1[1] == line_1[2]) and line_1[0] != "0":
    winner_found = True
    winner = line_1[0]

if (line_2[0] == line_2[1] == line_2[2]) and line_2[0] != "0":
    winner_found = True
    winner = line_2[0]

if (line_3[0] == line_3[1] == line_3[2]) and line_3[0] != "0":
    winner_found = True
    winner = line_3[0]

for index in range(3):
    if (line_1[index] == line_2[index] == line_3[index]) and line_1[index] != "0":
        winner_found = True
        winner = line_1[index]

if winner_found:
    if winner == "1":
        winner = "First player won"
    elif winner == "2":
        winner = "Second player won"
print(winner)
