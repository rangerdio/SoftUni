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


number, target_position = 1234, 7
# number, target_position = int(input()), int(input())
new_number_7_111_as_mask = 7 << target_position

print(pos_int_to_binary(number))
print(pos_int_to_binary(new_number_7_111_as_mask))
result = new_number_7_111_as_mask ^ target_position
print(result)
