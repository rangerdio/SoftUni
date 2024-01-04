def bit_at_pos_1(number: int, position: int):
    right_shifted_num = number >> position
    bit = right_shifted_num & 1
    return bit


num = int(input())
pos = 1
print(bit_at_pos_1(num, pos))
