students_total = int(input())
grade_var = 0
a = 0
b = 0
c = 0
d = 0
for _number in range(1, students_total + 1):
    grade = float(input())
    grade_var += grade
    if 2.00 <= grade <= 2.99:
        a += 1
    elif 3.00 <= grade <= 3.99:
        b += 1
    elif 4.00 <= grade <= 4.99:
        c += 1
    elif grade >= 5.00:
        d += 1
average = grade_var / students_total
d *= 100/students_total
c *= 100/students_total
b *= 100/students_total
a *= 100/students_total
print(f"Top students: {d:.2f}%")
print(f"Between 4.00 and 4.99: {c:.2f}%")
print(f"Between 3.00 and 3.99: {b:.2f}%")
print(f"Fail: {a:.2f}%")
print(f"Average: {average:.2f}")
