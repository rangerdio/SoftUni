def count_students(courses_: dict):
    result_dict = {}
    for course_name in courses_.values():
        if course_name not in result_dict:
            result_dict[course_name] = 1
        else:
            result_dict[course_name] += 1
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
    print(f"{course}: {hits[course]}")
    for name in courses.keys():
        if courses[name] == course:
            print(f"-- {name}")