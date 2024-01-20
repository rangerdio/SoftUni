number_list = list(map(int, input().split(", ")))
index_list = [number_list.index(element) for element in number_list if element % 2 == 0]
print(index_list)
