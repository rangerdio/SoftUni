nominated = False
actor = input()
academy_points = float(input())
total_points = academy_points
n = int(input())
length = 0
for number in range(1, n + 1):
    evaluator_name = input()
    evaluator_points = float(input())
    length = len(evaluator_name)
    evaluator_points *= length/2
    total_points += evaluator_points
    if total_points > 1250.5:
        nominated = True
        break
if nominated:
    print(f"Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {actor} you need {(abs(total_points - 1250.5)):.1f} more!")
