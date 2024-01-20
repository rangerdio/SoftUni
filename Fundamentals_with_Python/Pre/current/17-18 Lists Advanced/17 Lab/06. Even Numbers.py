number_list = list(map(int, input().split(", ")))
index_list = [index for index, element in enumerate(number_list) if element % 2 == 0]
print(index_list)
