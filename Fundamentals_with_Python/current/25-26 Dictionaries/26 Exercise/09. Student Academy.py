n = int(input())
grades = {}
grade_counter = {}
for i in range(n):
    name, grade = input(), float(input())
    if name not in grades.keys():
        grades[name] = grade
        grade_counter[name] = 1
    else:   # exists
        grades[name] += grade
        grade_counter[name] += 1

average = 0
for name in grades.keys():
    grades[name] /= grade_counter[name]
    average += grades[name]

average /= len(grades)

for name in grades.keys():
    if grades[name] >= 4.50:
        print(f"{name} -> {grades[name]:.2f}")
