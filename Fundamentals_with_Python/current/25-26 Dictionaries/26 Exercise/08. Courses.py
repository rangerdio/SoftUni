def count_students(courses_: dict):
    result_dict = {}
    for name in courses_.values():
        if name not in result_dict:
            result_dict[name] = 1
        else:
            result_dict[name] += 1
    return result_dict


courses = {}
while True:
    command = input()
    if command == "end":
        break
    command = command.split(" : ")
    courses[command[1]] = command[0]

# print(courses)
hits = count_students(courses)

for course in hits.keys():
    print(hits[course])
    for name in courses.keys():
        if courses[name] == course:
            print(f"-- {name}")
