n = int(input())
for num in range(1000, 10000):
    small_or_big = False
    num_str = str(num)
    left = 0
    right = 0
    lucky = False
    for index, number in enumerate(num_str):
        if int(number) < 1 or int(number) > 9:
            small_or_big = True
            break
        if index < 2:
            left += int(number)
        elif 3 >= index >= 2:
            right += int(number)
    if left == right and n % left == 0 and not small_or_big:
        print(num, end=" ")
