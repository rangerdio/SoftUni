# tail = input()
# body = input()
# head = input()
# my_list = [head, body, tail]
# print(my_list)

my_list = [input(), input(), input()]
my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)
