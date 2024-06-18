def merge_(words_, command):
    start_index = int(command[1])
    end_index = int(command[2])

    if start_index >= len(words_) - 1:
        return words_
    elif int(command[2]) >= len(words_) + 2 > start_index:
        end_index = len(words_)

    new_words_string = ""
    for index in range(len(words_)):
        if start_index <= index <= end_index:
            new_words_string += words_[index]
        else:
            word_mod = "  " + words_[index] + "  "
            new_words_string += word_mod
    # print(f"test before split: {new_words_string}")
    return new_words_string.split()


def dividing_word(word: str, partitions_: int):
    if len(word) % partitions_ == 0:
        new_word_string = ""
        # print(f"2) inside dividing_word: {word}, magic_lenght: {magic_lenght}")
        cnt = 1
        for index in range(len(word)):
            if cnt <= 2:
                new_word_string += word[index]
                cnt += 1
            else:
                cnt = 1
                new_word_string += "  " + word[index]
                cnt += 1
        # print(f"3) inside dividing_word, just after divide: {new_word_string}")
        return new_word_string.split("  ")
    else:  # if len(word) != 0
        magic_lenght = len(word) // partitions_
        partitions_up_to = partitions_ - 1
        counter = 0
        counter2 = 1
        second_part = ""
        first_part = ""

        for index in range(len(word)):
            counter += 1

            if counter2 == partitions_up_to:
                second_part = word[-magic_lenght - 1:]
                print(f"3.3) second part of dividing word {second_part}")

            if counter <= magic_lenght:
                first_part += word[index]
            elif counter > magic_lenght:
                first_part += "  "
                first_part += word[index]
                counter = 1
                counter2 += 1
        print(f"3.3 first part of dividing string {first_part}")
        new_word_string = first_part + second_part
        print(new_word_string)
    return new_word_string


def divide_(words_: list, command: list):
    divide_index_number = int(command[1])
    partitions = int(command[2])
    divide_word = words_[divide_index_number]
    print(f"1) inside divide_ word to be divided: {divide_word}")
    divided_string_list = dividing_word(divide_word, partitions)
    # print(divided_string_list)
    # print(f"4) inside divide, after dividing_word, the divided string: {divided_string}")
    divide_result = words_[:divide_index_number] + divided_string_list
    # print(divide_result)
    return divide_result


# string = "abcd efgh ijkl mnop qrst uvwx yz"
words = input().split()
while True:
    current_cmd = input()
    current_cmd_list = current_cmd.split()
    if current_cmd == "3:1":
        break
    elif current_cmd_list[0] == "merge":
        words = merge_(words, current_cmd_list)
        # print(words)
        # print(f' after merge {" ".join(words)}')
    elif current_cmd_list[0] == "divide":
        words = divide_(words, current_cmd_list)
        print(words)
        print(f'after divide: {" ".join(words)}')

print(" ".join(words))
