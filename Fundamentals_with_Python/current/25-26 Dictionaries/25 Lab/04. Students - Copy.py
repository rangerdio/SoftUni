dictionary = {}
while True:
    data = input().split(":")
    if data[0].islower():
        course_to_search = data[0]
        break
    dictionary[data[1]] = [{"name": data[0]}, {"course": data[2]}]

for student_id, results in dictionary.items():
    if course_to_search in results[1].values():
        print(f"{results[0]['name']} - {student_id}")
