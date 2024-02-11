def merge_(words_, command):
    new_words = []
    for index in range(len(words_)):
        if command[1] < index < command[2] + 1:

    return "asd"


string = "Ivo Johny Tony Bony Mony"
words = string.split()
print(words)
current_cmd_list = ["merge", "0", "3"]
words = merge_(words, current_cmd_list)
print(words)
print(current_cmd_list)
