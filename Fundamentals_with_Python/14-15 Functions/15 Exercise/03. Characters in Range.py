def characters(char_1: str, char_2: str) -> str:
    start_number_ch = ord(char_1)
    end_num_ch = ord(char_2)
    result_list = []
    for char in range(start_number_ch + 1, end_num_ch):
        result_list.append(chr(char))
    return " ".join(result_list)


character_1 = input()
character_2 = input()
print(characters(character_1, character_2))
