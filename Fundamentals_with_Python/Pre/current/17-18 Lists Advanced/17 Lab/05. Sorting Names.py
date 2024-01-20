name_list = input().split(", ")
sorted_name_list = sorted(name_list, key=lambda x: (-len(x), x))
print(sorted_name_list)
