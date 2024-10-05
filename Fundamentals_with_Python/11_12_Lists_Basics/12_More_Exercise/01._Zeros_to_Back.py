my_list = input().split(", ")

for index in range(len(my_list)):
    my_list[index] = int(my_list[index])
cnt = my_list.count(0)

for i in range(cnt):
    my_list.remove(0)
    my_list.append(0)
print(my_list)
