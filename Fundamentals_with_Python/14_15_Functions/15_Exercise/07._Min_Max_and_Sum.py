def mms(string):
    numbers = list(map(int, string.split()))
    min_function = min(numbers)
    max_function = max(numbers)
    sum_function = sum(numbers)
    return min_function, max_function, sum_function


numbers_str = input()
minn, maxx, numm = mms(numbers_str)
print(f"The minimum number is {minn}")
print(f"The maximum number is {maxx}")
print(f"The sum number is: {numm}")
