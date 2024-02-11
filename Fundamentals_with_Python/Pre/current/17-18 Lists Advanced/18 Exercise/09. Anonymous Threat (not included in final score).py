def merge_(words_, command):
    new_words_string = ""
    for index in range(len(words_)):
        if int(command[1]) <= index <= int(command[2]):
            new_words_string += words_[index]
        else:
            word_mod = " " + words_[index] + " "
            new_words_string += word_mod
    return new_words_string.split()


def divide_(words_, command):
    return "asd"


string = "Ivo Johny Tony Bony Mony"
words = string.split()
while True:
    current_cmd = input()
    current_cmd_list = current_cmd.split()
    if current_cmd == "3:1":
        break
    elif current_cmd[0] == "merge":
        words = merge_(words, current_cmd_list)
    elif current_cmd[0] == "divide":
        words = merge_(words, current_cmd_list)
