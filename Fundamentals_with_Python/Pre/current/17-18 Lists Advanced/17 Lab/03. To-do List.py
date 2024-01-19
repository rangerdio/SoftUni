todo_list = [0] * 10
while True:
    todo = input()
    if todo == "End":
        break
    current_todo = todo.split("-")
    # print(current_todo)
    todo_list.insert(int(current_todo[0]) - 1, current_todo[1])
    todo_list.pop(int(current_todo[0]))
    # print(todo_list)
for index, element in todo_list:
    if element == 0:
        todo_list.pop(index)
print(todo_list)
