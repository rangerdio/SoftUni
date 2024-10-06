def softuni_students(*args, **kwargs):
    registration_data = args
    courses_passed = kwargs
    # print(registration_data)
    # print(courses_passed)
    passed = {}
    invalid = []

    for course_id, username in registration_data:
        if course_id in courses_passed.keys():
            passed[username] = courses_passed[course_id]
        else:
            invalid.append(username)
    passed_sorted = sorted(passed.items(), key=lambda x: x[0])
    invalid_sorted = sorted(invalid)
    result = ''
    for username, course in passed_sorted:
        result += f'*** A student with the username {username} has successfully finished the course {course}!\n'
    if invalid_sorted:
        result += f'!!! Invalid course students: {", ".join(invalid_sorted)}'
    return result


# print(softuni_students(
#     ('id_1', 'Kaloyan9905'),
#     id_1='Python Web Framework',
# ))

# print(softuni_students(
#     ('id_7', 'Silvester1'),
#     ('id_32', 'Katq21'),
#     ('id_7', 'The programmer'),
#     id_76='Spring Fundamentals',
#     id_7='Spring Advanced',
# ))

# print(softuni_students(
#     ('id_22', 'Programmingkitten'),
#     ('id_11', 'MitkoTheDark'),
#     ('id_321', 'Bobosa253'),
#     ('id_08', 'KrasimirAtanasov'),
#     ('id_32', 'DaniBG'),
#     id_321='HTML & CSS',
#     id_22='Machine Learning',
#     id_08='JS Advanced',
# ))
