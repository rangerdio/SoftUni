def odd_and_even_sum(num_string: str):
    odd_sum = 0
    even_sum = 0
    for char in range(len(num_string)):
        if int(num_string[char]) % 2 == 0:
            even_sum += int(num_string[char])
        else:
            odd_sum += int(num_string[char])
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number_string = input()
print(odd_and_even_sum(number_string))
