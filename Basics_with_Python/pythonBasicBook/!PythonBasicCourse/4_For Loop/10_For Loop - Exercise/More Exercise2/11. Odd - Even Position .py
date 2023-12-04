import sys
odd_min = sys.maxsize
odd_max = - sys.maxsize
even_min = sys.maxsize
even_max = - sys.maxsize
odd_sum = 0
even_sum = 0
odd_count = 0
even_count = 0
n = int(input())
for n in range(1, n+1):
    number = float(input())
    if n % 2 != 0:
        odd_count += 1
        odd_sum += number
        if number <= odd_min:
            odd_min = number
        if number >= odd_max:
            odd_max = number
    else:
        even_count += 1
        even_sum += number
        if number <= even_min:
            even_min = number
        if number >= even_max:
            even_max = number

print(f"OddSum={odd_sum:.2f},")
if odd_count >= 1:
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
else:
    print(f"OddMin=No,")
    print(f"OddMax=No,")
print(f"EvenSum={even_sum:.2f},")
if even_count >= 1:
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")
else:
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
