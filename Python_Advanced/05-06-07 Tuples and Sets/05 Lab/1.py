numbers = tuple([float(x) for x in input().split(' ')])

dictionary = {}

for number in numbers:
    if number not in dictionary:
        dictionary[number] = numbers.count(number)

for number, value in dictionary.items():
    print(f"{number} - {value} times")
