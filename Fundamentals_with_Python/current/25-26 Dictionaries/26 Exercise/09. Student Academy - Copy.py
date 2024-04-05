grades = {}
n = int(input())
for i in range(n):
    name = input()
    grade = float(input())
    if name not in grades:
        grades[name] = [grade]
    else:
        grades[name].append(grade)

successful_grades = {}
for name in grades.keys():
    average = sum(grades[name]) / len(grades[name])
    if average >= 4.50:
        successful_grades[name] = average
for name, grade in successful_grades.items():
    print(f'{name} -> {grade:.2f}')
