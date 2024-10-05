n = int(input())
students = {}

for i in range(n):
    name, grade = input().split()
    if name not in students:
        students[name] = [float(grade)]
    else:
        students[name].append(float(grade))


for element, grade in students.items():
    avr_grade = sum(grade)/len(grade)
    formatted_grade = ' '.join(f"{x:.2f}" for x in grade)
    print(f"{element} -> {formatted_grade} (avg: {avr_grade:.2f})")
