todo_list = [0] * 10
while True:
    todo = input()
    if todo == "End":
        break
    current_todo = todo.split()
    print(current_todo)
    # todo_list.insert((int(current_todo[0]) - 1),current_todo[1])
