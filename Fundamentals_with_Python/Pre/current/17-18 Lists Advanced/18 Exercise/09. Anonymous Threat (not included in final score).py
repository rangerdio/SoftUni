def merge_(words_: list, command: list):
    start_index = int(command[1])
    end_index = int(command[2])

    if start_index >= len(words_) - 1:
        return words_
    elif end_index >= len(words_) + 2 > start_index:
        end_index = len(words_)

    new_words_string = ""
    for index in range(len(words_)):
        if start_index <= index <= end_index:
            new_words_string += words_[index]
        else:
            word_mod = "  " + words_[index] + "  "
            new_words_string += word_mod
    return new_words_string.split()


def dividing_word(word: str, partitions_: int):
    if len(word) % partitions_ == 0:
        new_word_string = ""
        cnt = 1
        for index in range(len(word)):
            if cnt <= 2:
                new_word_string += word[index]
                cnt += 1
            else:
                cnt = 1
                new_word_string += "  " + word[index]
                cnt += 1
        return new_word_string.split("  ")

    else:  # if len(word) != 0
        magic_lenght = len(word) // partitions_
        counter = 0
        first_part = ""

        for index in range(len(word) - magic_lenght - 1):
            counter += 1

            if counter <= magic_lenght:
                first_part += word[index]
            elif counter > magic_lenght:
                first_part += "  "
                first_part += word[index]
                counter = 1
        second_part = word[-magic_lenght - 1:]
        new_word_string = first_part + "  " + second_part

    return new_word_string.split("  ")


def divide_(words_: list, command: list):
    divide_index_number = int(command[1])
    partitions = int(command[2])
    divide_word = words_[divide_index_number]
    divided_string_list = dividing_word(divide_word, partitions)
    divide_result = words_[:divide_index_number] + divided_string_list
    return divide_result


words = input().split()
while True:
    current_cmd = input()
    current_cmd_list = current_cmd.split()
    if current_cmd == "3:1":
        break
    elif current_cmd_list[0] == "merge":
        words = merge_(words, current_cmd_list)

    elif current_cmd_list[0] == "divide":
        words = divide_(words, current_cmd_list)

print(" ".join(words))
