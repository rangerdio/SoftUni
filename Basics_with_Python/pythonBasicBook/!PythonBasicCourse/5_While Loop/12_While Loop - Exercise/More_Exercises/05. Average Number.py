n = int(input())
nn = n
numbers_sum = 0
while n > 0:
    number = int(input())
    numbers_sum += number
    n -= 1
average= numbers_sum / nn
print(f"{average:.2f}")