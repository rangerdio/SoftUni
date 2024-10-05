winner_name = ""
winner_score = 0
old_name = ""
old_score = 0

while True:
    name = input()
    if name == "Stop":
        break
    current_score = 0
    for index, number1 in enumerate(name):
        num1 = int(input())
        if num1 == ord(number1):
            current_score += 10
        else:
            current_score += 2
    if current_score >= winner_score:
        winner_name = name
        winner_score = current_score

print(f"The winner is {winner_name} with {winner_score} points!")