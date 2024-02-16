# import math
#
#
# def student_score(number_of_lectures_, additional_bonus_, student_attendances_):
#     total_bonus = student_attendances_ / number_of_lectures_ * (5 + additional_bonus_)
#     return total_bonus
#
#
# number_of_students, number_of_lectures, additional_bonus = int(input()), int(input()), int(input())
# results = []
# attendances = []
# for s in range(number_of_students):
#     student_attendances = int(input())
#     student_attendances = number_of_lectures if student_attendances > number_of_lectures else student_attendances
#     results.append(student_score(number_of_lectures, additional_bonus, student_attendances))
#     attendances.append(student_attendances)
#
# max_bonus = max(results)
# max_bonus_index = results.index(max(results))
# print(f"Max Bonus: {math.ceil(max_bonus)}.")
# print(f"The student has attended {attendances[max_bonus_index]} lectures.")

import sys
import math
max_result = -sys.float_info.max
max_result_attendances = 0
number_of_students, number_of_lectures, additional_bonus = int(input()), int(input()), int(input())
for student in range(number_of_students):
    student_attendances = int(input())
    student_attendances = number_of_lectures if student_attendances > number_of_lectures else student_attendances
    total_bonus = student_attendances / number_of_lectures * (5 + additional_bonus)
    if total_bonus > max_result:
        max_result = total_bonus
        max_result_attendances = student_attendances

print(f"Max Bonus: {math.ceil(max_result)}.")
print(f"The student has attended {max_result_attendances} lectures.")
