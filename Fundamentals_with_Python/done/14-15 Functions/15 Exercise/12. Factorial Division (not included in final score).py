def factorial_division(number_1, number_2):
    factorial_nuber_1 = 1
    factorial_nuber_2 = 1
    for num in range(1, number_1 + 1):
        factorial_nuber_1 *= num
    for num in range(1, number_2 + 1):
        factorial_nuber_2 *= num
    return f"{(factorial_nuber_1 / factorial_nuber_2):.2f}"


first_number = int(input())
second_number = int(input())
print(factorial_division(first_number, second_number))
