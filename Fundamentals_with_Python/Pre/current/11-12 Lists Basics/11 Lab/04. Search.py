string_list = []
n = int(input())
word = input()
for i in range(n):
    current_string = input()
    string_list.append(current_string)
print(string_list)
filtered_list = []
for i in range(len(string_list)):
    element = string_list[i]
    if word in element:
        filtered_list.append(element)
print(filtered_list)

# string_list = []
# n = int(input())
# word = input()
# for i in range(n):
#     current_string = input()
#     string_list.append(current_string)
# print(string_list)
# for i in range(len(string_list) - 1, -1, -1):
#     element = string_list[i]
#     if word not in element:
#         string_list.remove(element)
# print(string_list)
