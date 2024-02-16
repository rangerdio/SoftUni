def student_score(number_of_lectures_, additional_bonus_, student_attendances_):
    total_bonus = student_attendances_ / number_of_lectures_ * (5 + additional_bonus_)
    return total_bonus


number_of_students, number_of_lectures, additional_bonus = int(input()), int(input()), int(input())
results = []
attendances = []
for s in range(number_of_students):
    student_attendances = int(input())
    results.append(student_score(number_of_lectures, additional_bonus, student_attendances))
    attendances.append(student_attendances)

max_bonus = max(results)
max_bonus_index = results.index(max(results))
print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {attendances[max_bonus_index]} lectures.")
