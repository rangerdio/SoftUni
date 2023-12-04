start_range = int(input())
end_range = int(input())
start = 0
end = 0

start_range_str = str(start_range)
end_range_str = str(end_range)

start_int_1 = int(start_range_str[0])
start_int_2 = int(start_range_str[1])
start_int_3 = int(start_range_str[2])
start_int_4 = int(start_range_str[3])
end_int_1 = int(end_range_str[0])
end_int_2 = int(end_range_str[1])
end_int_3 = int(end_range_str[2])
end_int_4 = int(end_range_str[3])
barcode_line = ""

for num1 in range(start_int_1, end_int_1 + 1):
    if num1 % 2 == 0:
        continue
    for num2 in range(start_int_2, end_int_2 + 1):
        if num2 % 2 == 0:
            continue
        for num3 in range(start_int_3, end_int_3 + 1):
            if num3 % 2 == 0:
                continue
            for num4 in range(start_int_4, end_int_4 + 1):
                if num4 % 2 == 0:
                    continue
                num1_str = str(num1)
                num2_str = str(num2)
                num3_str = str(num3)
                num4_str = str(num4)
                barcode_line += num1_str + num2_str + num3_str + num4_str + " "
print(barcode_line)
