name = input()
average_sum = 0
poor_count = 0
terminated = False
terminated_class = 0
grade = False
for n in range(1, 13):
    grad = float(input())
    if grad < 4:
        poor_count += 1
        grad = float(input())
        if grad < 4:
            terminated_class = n
            terminated = True
            break
    average_sum += grad

if terminated:
    print(f"{name} has been excluded at {terminated_class} grade")
else:
    grade = average_sum / 12
    print(f"{name} graduated. Average grade: {grade:.2f}")
