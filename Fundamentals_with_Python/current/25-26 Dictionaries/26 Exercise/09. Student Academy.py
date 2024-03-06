n = int(input())
grades = {}
for i in range(n):
    name, grade = input(), float(input())
    if grade >= 4.50:
        grades[name] = grade
