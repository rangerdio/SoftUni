num = int(input())
num_string = str(num)

sorted_string = sorted(num_string, reverse=True)

for index, digit in enumerate(sorted_string):
    print(digit, end="")

# sorted_number = "".join(sorted_string)
# print(sorted_number)
