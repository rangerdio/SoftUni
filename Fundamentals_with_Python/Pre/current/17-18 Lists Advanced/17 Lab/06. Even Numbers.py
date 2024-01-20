number_list = input().split(", ")
print(number_list)
index_list = [number_list[element] for element in number_list if element % 2 == 0]
print(number_list)
