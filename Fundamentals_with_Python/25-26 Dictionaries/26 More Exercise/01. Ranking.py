def ranking(students_: list, submission_dict_: dict):
    for student_ in sorted(students_):
        print(f"Ranking:\n{student_}")
        values_to_use = []  # export list so to sort the fucking data
        for inside_dict in submission_dict_.values():
            if student_ in inside_dict.keys():
                values_to_use.append(inside_dict[student_])
        values_to_use_sorted = sorted(values_to_use, reverse=True)

        for value_ in values_to_use_sorted:
            for submission__, inside_dict in submission_dict_.items():
                key_ = ""
                for key, value in inside_dict.items():
                    if value == value_:
                        key_ = key
                print(f"# {submission__} -> {key_}")
    return


contests_dict = {}
submissions_dict = {}

while True:
    contest_string_list = input().split(":")
    if contest_string_list[0] == "end of contests":
        break
    contest, password = contest_string_list[0], contest_string_list[1]
    contests_dict[contest] = password

while True:
    submission_string_list = input().split("=>")
    if submission_string_list[0] == "end of submissions":
        break
    contest, password, username, points = submission_string_list[0], \
        submission_string_list[1], submission_string_list[2], int(submission_string_list[3])
    if contest in contests_dict and contests_dict[contest] == password:
        if contest not in submissions_dict:
            submissions_dict[contest] = {}
        if username not in submissions_dict[contest] or points > submissions_dict[contest][username]:
            submissions_dict[contest][username] = points

print(contests_dict)
print(submissions_dict)

students = []   # get students
students_results = {}   # get total results for students
for contest_values in submissions_dict.values():
    [students.append(key) for key in contest_values if key not in students]

for student in students:
    total_points = 0
    for values in submissions_dict.values():
        if student in values:
            total_points += values[student]
    students_results[student] = total_points

winner = ""
for student in students_results.keys():
    winner = max(students_results, key=students_results.get)

print(f"Best candidate is {winner} with total {students_results[winner]} points.")

print(students)
print(students_results)


print(ranking(students, submissions_dict))
