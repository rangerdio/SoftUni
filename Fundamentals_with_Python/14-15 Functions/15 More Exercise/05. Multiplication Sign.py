def multiplication_sign(input_list: list):
    negative = 0
    if 0 in input_list:
        return "zero"
    for element in input_list:
        if element < 0:
            negative += 1
    if negative % 2 == 1:
        return "negative"
    else:
        return "positive"


numbers = []
for i in range(3):
    numbers.append(int(input()))
print(multiplication_sign(numbers))
