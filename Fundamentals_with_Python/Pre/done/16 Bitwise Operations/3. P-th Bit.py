def bit_at_pos_n(number: int, position: int):
    right_shifted_num = number >> position
    bit = right_shifted_num & 1
    return bit


num, pos = int(input()), int(input())
print(bit_at_pos_n(num, pos))
