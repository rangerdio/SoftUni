input_number = int(input())

for check in range(1111, 9999 + 1):
    str_check = str(check)
    special = True
    for index, number in enumerate(str_check):
        if int(number) == 0 or input_number % int(number) != 0:
            special = False
    if special:
        print(check, end=" ")
