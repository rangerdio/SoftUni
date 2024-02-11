string_list_1 = input().split(", ")
string_list_2 = input().split(", ")
result = []
for element in string_list_1:
    for element2 in string_list_2:
        # result.append(element) if element in element2
        # break
        if element in element2:
            result.append(element)
            break
print(result)
