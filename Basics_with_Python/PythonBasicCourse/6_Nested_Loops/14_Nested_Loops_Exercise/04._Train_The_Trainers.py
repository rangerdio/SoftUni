jury = int(input())
presentation_name = input()
grades_sum = 0
presentation_counter = 0
student_grades_total = 0
while presentation_name != "Finish":
    for _ in range(1, jury + 1):
        grade = float(input())
        grades_sum += grade
    average_presentation_grade = grades_sum / jury
    print(f"{presentation_name} - {average_presentation_grade:.2f}.")
    grades_sum = 0
    presentation_counter += 1
    student_grades_total += average_presentation_grade
    presentation_name = input()
average_student_grade = student_grades_total / presentation_counter
print(f"Student's final assessment is {average_student_grade:.2f}.")
