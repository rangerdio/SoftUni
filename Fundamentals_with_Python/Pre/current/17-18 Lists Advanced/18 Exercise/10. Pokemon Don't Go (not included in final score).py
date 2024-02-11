def merge_(words_: list, command: list):

    return "asd"


string = "Ivo Johny Tony Bony Mony"
words = string.split()
print(words)
while True:
    current_cmd = input()
    current_cmd_list = current_cmd.split()
    print(current_cmd_list)
    if current_cmd == "3:1":
        break
    elif current_cmd[0] == "merge":
        words = merge_(words, current_cmd_list)
    elif current_cmd[0] == "divide":
        words = merge_(words, current_cmd_list)