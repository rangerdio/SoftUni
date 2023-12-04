start_number = int(input())
end_number = int(input())

for number in range(start_number, end_number + 1):
    str_number = str(number)
    odd_sum = 0
    even_sum = 0
    for ind, num in enumerate(str_number):
        if ind % 2 == 0:
            odd_sum += int(num)
        else:
            even_sum += int(num)
    if odd_sum == even_sum:
        print(number, end=" ")
    else:
        continue
