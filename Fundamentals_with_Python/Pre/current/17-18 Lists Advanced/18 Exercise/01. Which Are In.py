string_list_1 = input().split(", ")
string_list_2 = input().split(", ")
result_list = [element for element in string_list_1 if element in [element2 for element2 in string_list_2]]
print(result_list)
