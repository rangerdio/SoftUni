a1 = int(input())
a2 = int(input())
n = int(input())

for first_num in range(a1, a2 - 1 + 1):
    first_str = chr(first_num)
    if first_num % 2 != 1:
        continue
    for second_num in range(1, n - 1 + 1):
        for third_num in range(1, int(n / 2 - 1) + 1):
            fourth_num = first_num

            if (second_num + third_num + fourth_num) % 2 == 1:
                print(f"{first_str}-{second_num}{third_num}{fourth_num}")
