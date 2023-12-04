n = int(input())
for num in range(1, n + 1):
    num_string = str(num)
    numbers_sum = 0
    for index, number in enumerate(num_string):
        numbers_sum += int(number)
    if numbers_sum == 5 or numbers_sum == 7 or numbers_sum == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
