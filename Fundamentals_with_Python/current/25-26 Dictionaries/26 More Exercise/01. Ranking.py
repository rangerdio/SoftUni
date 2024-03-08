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

students = []
for contest_values in submissions_dict.values():
    [students.append(key) for key in contest_values]

print(students)
