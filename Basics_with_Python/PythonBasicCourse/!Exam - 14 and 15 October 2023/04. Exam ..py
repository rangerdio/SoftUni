students_quantity = int(input())
counter_fail = 0
counter_34 = 0
counter_45 = 0
counter_top = 0
grades_all = 0

for student in range(1, students_quantity + 1):
    grade = float(input())
    if grade >= 2.00 and grade <= 2.99:
        counter_fail += 1
    elif grade >= 2.00 and grade <= 3.99:
        counter_34 += 1
    elif grade >= 4.00 and grade <= 4.99:
        counter_45 += 1
    elif grade >= 5.00:
        counter_top += 1
    grades_all += grade

group1 = counter_top / students_quantity * 100
group2 = counter_45 / students_quantity * 100
group3 = counter_34 / students_quantity * 100
group4 = counter_fail / students_quantity * 100
average = grades_all / students_quantity
print(f"Top students: {group1:.2f}%")
print(f"Between 4.00 and 4.99: {group2:.2f}%")
print(f"Between 3.00 and 3.99: {group3:.2f}%")
print(f"Fail: {group4:.2f}%")
print(f"Average: {average:.2f}")
