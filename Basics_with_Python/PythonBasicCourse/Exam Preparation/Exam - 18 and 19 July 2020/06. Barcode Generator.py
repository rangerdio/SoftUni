start_range = int(input())
end_range = int(input())
start_range_str = str(start_range)
end_range_str = str(end_range)

num1_start_int = int(start_range_str[0])
num1_end_int = int(end_range_str[0])
num2_start_int = int(start_range_str[1])
num2_end_int = int(end_range_str[1])
num3_start_int = int(start_range_str[2])
num3_end_int = int(end_range_str[2])
num4_start_int = int(start_range_str[3])
num4_end_int = int(end_range_str[3])

for num1 in range(num1_start_int, num1_end_int + 1):
    if num1 % 2 == 0:
        continue
    for num2 in range(num2_start_int, num2_end_int + 1):
        if num2 % 2 == 0:
            continue
        for num3 in range(num3_start_int, num3_end_int + 1):
            if num3 % 2 == 0:
                continue
            for num4 in range(num4_start_int, num4_end_int + 1):
                if num4 % 2 == 0:
                    continue
                print(f"{num1}{num2}{num3}{num4}", end=" ")
