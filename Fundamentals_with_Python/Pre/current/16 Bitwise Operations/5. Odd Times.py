number_list = list(map(int, input().split()))
# print(number_list)
index = 0
result = 0
while index < len(number_list):
    result = result ^ number_list[index]
    index += 1
print(result)
