def get_sequence(quantity: int):
    numbers = [0, 0, 1]
    for i in range(quantity - 1):
        numbers.append(numbers[-1] + numbers[-2] + numbers[-3])
    numbers.remove(0)
    numbers.remove(0)
    return " ".join(str(element) for element in numbers)


qty = int(input())
print(get_sequence(qty))
