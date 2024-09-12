n = int(input())
even_set = set()
odd_set = set()
for row in range(1, n + 1):
    name = input()
    aski_sum = 0
    for char in name:
        aski_sum += ord(char)
    divided_number = aski_sum // row

    if divided_number % 2 == 0:
        even_set.add(divided_number)
    else:
        odd_set.add(divided_number)

sum_odd_set = sum(odd_set)
sum_even_set = sum(even_set)

if sum_odd_set == sum_even_set:
    union = odd_set.union(even_set)
    print(*union, sep=', ')
elif sum_odd_set > sum_even_set:
    difference = odd_set.difference(even_set)
    print(*difference, sep=', ')
else:
    symmetric_difference = odd_set.symmetric_difference(even_set)
    print(*symmetric_difference, sep=', ')


