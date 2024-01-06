def pos_int_to_binary(decemical_number: int):
    bin_num = []
    while True:
        if decemical_number == 0:
            while len(bin_num) < 32:
                bin_num.append("0")

            bin_num = bin_num[::-1]
            return "".join(bin_num)
        remainder = decemical_number % 2
        bin_num.append(str(remainder))
        decemical_number //= 2


pos_int = int(input())
print(pos_int_to_binary(pos_int))
