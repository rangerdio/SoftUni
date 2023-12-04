kozunaks = int(input())
cnt_grade = 0
baker_points = 0
old_baker_points = 0
winner = ""

for koz in range(kozunaks):
    baker_name = input()
    command = input()

    while command != "Stop":
        grade = int(command)
        cnt_grade += 1
        baker_points += grade

        command = input()
    print(f"{baker_name} has {baker_points} points.")
    if baker_points > old_baker_points:
        old_baker_points = baker_points
        winner = baker_name
        print(f"{baker_name} is the new number 1!")

    baker_points = 0
print(f"{winner} won competition with {old_baker_points} points!")
