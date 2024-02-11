def merge_(words_):
    return "asd"


def divide_(words_):
    return "asd"


string = "Ivo Johny Tony Bony Mony"
words = string.split()
while True:
    current_cmd = input()
    current_cmd_list = current_cmd.split()
    if current_cmd == "3:1":
        break
    elif current_cmd[0] == "merge":
        words = merge_(words)
    elif current_cmd[0] == "divide":
        words = merge_(words)
