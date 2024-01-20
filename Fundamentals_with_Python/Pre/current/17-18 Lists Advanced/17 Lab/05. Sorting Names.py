name_list = input().split(", ")
print(name_list)
sorted_name_list = sorted(name_list, key=lambda x: (-len(x), x))
print(sorted_name_list)