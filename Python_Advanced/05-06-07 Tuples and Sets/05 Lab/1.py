
numbers = tuple(float(f'{float(number):.1f}') for number in input().split(' '))
dict_ = {}

for number in numbers:
    # if number not in dict_.keys():
    #     dict_[number] = 0
    dict_[number] = numbers.count(number)

for key, value in dict_.items():
    print(f'{key} - {value} times')
