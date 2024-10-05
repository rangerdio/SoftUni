def binary_digit_count(decemical_number: int, binary_digit: int):
    counter = 0
    bin_num = []
    while True:
        if decemical_number == 0:
            bin_num.append("Binary number is: ")
            bin_num = bin_num[::-1]
            print("".join(bin_num))
            return counter
        remainder = decemical_number % 2
        bin_num.append(str(remainder))
        if remainder == binary_digit:
            counter += 1
        decemical_number //= 2


number = int(input())
bin_digit = int(input())
print(binary_digit_count(number, bin_digit))
