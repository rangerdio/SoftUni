name = ''
score = 0

while True:
    name = input()
    if name == 'Stop':
        break
    current_player_score = 0
    for letter in name:
        current_num = int(input())
        current_player_score += 10 if current_num == ord(letter) else 2

    if current_player_score >= score:
        name = name
        score = current_player_score

print(f"The winner is {name} with {score} points!")
