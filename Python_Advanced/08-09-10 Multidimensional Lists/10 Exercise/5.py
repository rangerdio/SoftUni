from collections import deque
n = int(input())
wonderland = []
alice_initial_coordinates = []
rabbit_initial_coordinates = []

for row in range(n):
    line = input().split(" ")
    if "A" in line:
        alice_initial_coordinates = [row, line.index('A')]
    if "R" in line:
        rabbit_initial_coordinates = [row, line.index('R')]
    wonderland.append(line)

alice_current_row, alice_current_col = alice_initial_coordinates
bags = 0

while True:

    current_command = input()
    if not current_command:
        break

    if current_command == "up":
        alice_next_row = alice_current_row - 1
        alice_next_col = alice_current_col
    elif current_command == "down":
        alice_next_row = alice_current_row + 1
        alice_next_col = alice_current_col
    elif current_command == "left":
        alice_next_row = alice_current_row
        alice_next_col = alice_current_col - 1
    else:
        alice_next_row = alice_current_row
        alice_next_col = alice_current_col + 1

    if not (0 <= alice_next_row < n and 0 <= alice_next_col < n):
        print("Alice didn't make it to the tea party.")
        break
    else:
        wonderland[alice_current_row][alice_current_col] = "*"
        if rabbit_initial_coordinates == [alice_next_row, alice_next_col]:
            print("Alice didn't make it to the tea party.")
            wonderland[alice_next_row][alice_next_col] = "*"
            break
        elif wonderland[alice_next_row][alice_next_col] == ".":
            wonderland[alice_current_row][alice_current_col] = "*"
            alice_current_row = alice_next_row
            alice_current_col = alice_next_col
        elif wonderland[alice_next_row][alice_next_col] == "*":
            alice_current_row = alice_next_row
            alice_current_col = alice_next_col
        else:
            bags += int(wonderland[alice_next_row][alice_next_col])
            # wonderland[alice_current_row][alice_current_col] = "*"
            wonderland[alice_next_row][alice_next_col] = "*"
            alice_current_row = alice_next_row
            alice_current_col = alice_next_col
            if bags >= 10:
                print("She did it! She went to the party.")
                break
for row in range(n):
    print(" ".join(wonderland[row]))
