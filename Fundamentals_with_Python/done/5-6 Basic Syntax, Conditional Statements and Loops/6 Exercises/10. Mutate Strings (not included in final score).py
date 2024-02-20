string_1 = input()
string_2 = input()
str_length = len(string_2)
uniq_list = [string_1]

for i in range(str_length):
    slice1 = string_2[:i + 1]
    slice2 = string_1[i + 1:]
    magic = slice1 + slice2
    if magic in uniq_list:
        continue
    else:
        print(magic)
        uniq_list.append(magic)
