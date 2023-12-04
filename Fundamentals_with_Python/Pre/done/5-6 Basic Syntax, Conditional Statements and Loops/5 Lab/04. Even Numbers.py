n = int(input())
is_all_even = True
for i in range(n):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        is_all_even = False
        break
# if is_all_even:
#     print(f"All numbers are even.")
else:
    print(f"All numbers are even.")