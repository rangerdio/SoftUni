def abs_list(list_numbers: list):
    new_list = []
    for num in number_list:
        new_list.append(abs(num))
    return new_list


number_list = list(map(float, input().split()))
print(abs_list(number_list))



"""

numbers = map(float, input().split())
new_list = []
for num in numbers:
    new_list.append(abs(num))
print(new_list)

"""