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

cnt = sum(1 for element in todo_list if element == 0)
while 0 in todo_list:
    todo_list.remove(0)
print(todo_list)
