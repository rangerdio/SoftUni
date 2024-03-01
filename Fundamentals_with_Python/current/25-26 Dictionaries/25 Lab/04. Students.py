search_with = ""
list_students = []
while True:
    command = input()
    if ":" not in command:
        search_with = " ".join(command.split("_"))
        break
    name, id, course = command.split(":")
    # course = "_".join(course.split(" "))
    dict_students = {"name": name, "id": id, "course": course}
    list_students.append(dict_students)

for element in list_students:
    if search_with == element["course"]:
        print(f"{element['name']} - {element['id']}")

# print(search_with)
# for element in list_students:
#     print(element)
