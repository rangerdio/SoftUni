course_data = {}
while True:
    line = input().split(" : ")
    if line[0] == "end":
        break
    course_name, student_name = line[0], line[1]
    if course_name not in course_data:
        course_data[course_name] = [student_name]
    else:
        course_data[course_name].append(student_name)

for course in course_data.keys():
    print(f'{course}: {len(course_data[course])}')
    for name in course_data[course]:
        print(f'-- {name}')
