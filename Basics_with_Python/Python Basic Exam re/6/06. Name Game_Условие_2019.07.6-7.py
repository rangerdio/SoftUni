player_name_length = 0
player_name = input()
pts_winner = 0
winner = ""

while player_name != "Stop":
    player_name_length = len(player_name)
    pts_current = 0
    for index, letter in enumerate(player_name):
        score = int(input())
        letter_num = ord(letter)
        if letter_num == score:
            pts_current += 10
        else:
            pts_current += 2

    if pts_current >= pts_winner:
        pts_winner = pts_current
        winner = player_name

    player_name = input()
print(f"The winner is {winner} with {pts_winner} points!")
