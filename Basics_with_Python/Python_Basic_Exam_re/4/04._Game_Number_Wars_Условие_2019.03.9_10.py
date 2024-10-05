player_one = input()
player_two = input()
points_p1 = 0
points_p2 = 0
is_number_wars = False
is_p1_win = False

player_one_card = input()
while player_one_card != "End of game":
    player_one_card = int(player_one_card)
    player_two_card = int(input())

    if player_one_card > player_two_card:
        points_p1 += player_one_card - player_two_card
    if player_two_card > player_one_card:
        points_p2 += player_two_card - player_one_card
    if player_one_card == player_two_card:
        is_number_wars = True
        player_one_card = input()
        player_two_card = input()
        if player_one_card > player_two_card:
            is_p1_win = True
            break
        else:
            break
    player_one_card = input()

if player_one_card == "End of game":
    print(f"{player_one} has {points_p1} points")
    print(f"{player_two} has {points_p2} points")
if is_number_wars:
    print("Number wars!")
    if is_p1_win:
        print(f"{player_one} is winner with {points_p1} points")
    else:
        print(f"{player_two} is winner with {points_p2} points")
