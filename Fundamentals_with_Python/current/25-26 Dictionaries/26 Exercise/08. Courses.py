def count_students(courses_: dict):
    result_dict = {}
    for name_ in courses_.values():
        if name_ not in result_dict:
            result_dict[name_] = 1
        else:
            result_dict[name_] += 1
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
